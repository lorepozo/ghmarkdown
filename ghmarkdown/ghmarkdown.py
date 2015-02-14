"""
ghmarkdown
==========

The complete command-line tool for (GitHub-flavored) markdown
"""

import argparse
import hashlib
import base64
import sys
import os
import requests

__version__ = "1.0.1"

_ROOT = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] == 3:
    universal_inp = input
else:
    universal_inp = raw_input

description = "The complete command-line tool for GitHub-flavored markdown"
usage = """
  ghmarkdown [--help] [--login] [--bare] [--silent] [--input MD]
             [--output HTML | --serve [--port PORT]]
"""
parser = argparse.ArgumentParser(description=description, usage=usage)
gh_url = 'https://api.github.com'
silent = False
mdhash = None


class Login:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.good = True

    def auth(self):
        """ Returns auth token """
        return (self.username, self.password) if self.good else None

    def devalue(self):
        self.good = False


class RequestError(Exception):
    pass


def html_from_markdown(markdown):
    """ Takes raw markdown, returns html result from GitHub api """

    if login:
        r = requests.get(gh_url+"/rate_limit", auth=login.auth())
        if r.status_code >= 400:
            if r.status_code != 401:
                err = RequestError('Bad HTTP Status Code: %s' % r.status_code)
                raise err
            sys.stderr.write('Unauthorized. Proceeding without login...')
            login.devalue()

    headers = {'content-type': 'text/plain', 'charset': 'utf-8'}

    r = requests.post(gh_url + "/markdown/raw", data=markdown,
                      auth=login.auth(), headers=headers)
    if r.status_code >= 400 and r.status_code != 403:
            err = RequestError('Bad HTTP Status Code: %s' % r.status_code)
            raise err

    if not silent:
        sys.stdout.write("\n%s requests remaining, resets in %d minutes\n"
                         % rate_limit_info())
    return r.text.replace("\n\n", "\n")

def standalone(html):
    """ Returns complete html document given markdown html """
    with open(_ROOT + '/ceiling.dat', 'r') as ceiling:
        with open(_ROOT + '/floor.dat', 'r') as floor:
            top = "".join(ceiling.readlines())
            bottom = "".join(floor.readlines())
            return top + html + bottom


def changed_file():
    global mdhash

    if inputfile is None:
        return None
    with open(inputfile, "r") as markdown:
        data = "".join(markdown.readlines())
    m = hashlib.md5()
    m.update(data)
    new_hash = m.hexdigest()
    if new_hash == mdhash:
        return None
    mdhash = new_hash
    return data


def run_server(port=8000):
    """ Runs server on port with html response """
    import BaseHTTPServer

    class HTMLHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_HEAD(s):
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()

        def do_GET(s):
            global html

            data = changed_file()
            if data is not None:
                html = html_from_markdown(data)
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write(standalone(html))

    class SilentHTMLHandler(HTMLHandler):
        def log_message(self, format, *args):
            return

    port = int(port)
    server_class = BaseHTTPServer.HTTPServer
    handler = SilentHTMLHandler if silent else HTMLHandler
    httpd = server_class(("localhost", port), handler)
    if not silent:
        print("Hosting server on port %d. Ctrl-c to exit" % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    if not silent:
        print("Shutting down server")


def rate_limit_info():
    """ Returns (requests_remaining, minutes_to_reset) """
    import json
    import time

    r = requests.get(gh_url + "/rate_limit", auth=login.auth())
    out = json.loads(r.text)
    mins = (out["resources"]["core"]["reset"]-time.time())/60
    return out["resources"]["core"]["remaining"], mins


def main():
    global parser
    global login
    global silent
    global html
    global mdhash
    global inputfile

    parser.add_argument('--version', action='store_true',
                        help='input markdown file (otherwise STDIN)')
    parser.add_argument('--input', '-i', metavar='MD',
                        help='input markdown file (otherwise STDIN)')
    parser.add_argument('--output', '-o', metavar='HTML',
                        help='output html file (otherwise STDOUT)')
    parser.add_argument('--login', '-l', action='store_true',
                        help='allows for more requests')
    parser.add_argument('--bare', '-b', action='store_true',
                        help='disable standalone html (gives fragment)')
    parser.add_argument('--silent', '-q', action='store_true',
                        help='silences server output and rate information')
    parser.add_argument('--serve', '-s', action='store_true',
                        help='locally serve parsed markdown')
    parser.add_argument('--port', '-p', metavar='PORT')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        exit()

    inputfile = args.input
    if args.input:
        with open(args.input, 'r') as markdown:
            data = "".join(markdown.readlines())
    else:
        try:
            data = "".join(sys.stdin.readlines())
        except KeyboardInterrupt:
            exit()

    if args.login:
        from getpass import getpass

        username = universal_inp("GitHub username: ")
        password = getpass()
        login = Login(username, password)
    else:
        login = Login()

    silent = args.silent
    html = html_from_markdown(data)
    m = hashlib.md5()
    m.update(data)
    mdhash = m.hexdigest()

    if not args.bare:
        html = standalone(html)
    if args.serve:
        run_server(args.port or '8000')
    elif args.output:
        with open(args.output, 'w') as out:
            out.write(html)
    else:
        sys.stdout.write(html)

if __name__ == '__main__':
    main()

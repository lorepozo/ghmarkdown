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

__version__ = "2.0.2"

_ROOT = os.path.abspath(os.path.dirname(__file__))

description = "The complete command-line tool for GitHub-flavored markdown"
usage = """
  ghmarkdown [--help | --version] [--login] [--bare] [--verbose] [--input MD]
             [--output HTML | --serve [--port PORT]]
"""
parser = argparse.ArgumentParser(description=description, usage=usage)
gh_url = 'https://api.github.com'
verbose = False
mdhash = None
inputfile = None


def title():
    return "ghmarkdown" if inputfile is None else inputfile.split("/")[-1]


def html_title():
    return "<title>%s</title>" % title()


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
            if verbose:
                sys.stderr.write('Unauthorized. Proceeding without login...\n')
            login.devalue()

    headers = {'content-type': 'text/plain', 'charset': 'utf-8'}

    r = requests.post(gh_url + "/markdown/raw", data=markdown.encode('utf-8'),
                      auth=login.auth(), headers=headers)
    if r.status_code >= 400 and r.status_code != 403:
            err = RequestError('Bad HTTP Status Code: %s' % r.status_code)
            raise err

    if verbose:
        sys.stderr.write("%s requests remaining, resets in %d minutes\n"
                         % rate_limit_info())
    return r.text


def standalone(body):
    """ Returns complete html document given markdown html """
    with open(_ROOT + '/html.dat', 'r') as html_template:
        head = html_title()
        html = "".join(html_template.readlines()) \
                 .replace("{{HEAD}}", head) \
                 .replace("{{BODY}}", body)
        return html


def changed_file():
    global mdhash

    if inputfile is None:
        return None
    with open(inputfile, "r") as markdown:
        data = "".join(markdown.readlines())
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    new_hash = m.hexdigest()
    if new_hash == mdhash:
        return None
    mdhash = new_hash
    return data


def run_server(port=8000):
    """ Runs server on port with html response """
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class VerboseHTMLHandler(BaseHTTPRequestHandler):
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
            s.wfile.write(standalone(html).encode('utf-8'))

    class SilentHTMLHandler(VerboseHTMLHandler):
        def log_message(self, format, *args):
            return

    port = int(port)
    server_class = HTTPServer
    handler = VerboseHTMLHandler if verbose else SilentHTMLHandler
    try:
        httpd = server_class(("localhost", port), handler)
    except PermissionError:
        sys.stderr.write("Permission denied\n")
        sys.exit(1)
    if verbose:
        print("Hosting server on port %d. Ctrl-c to exit" % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    if verbose:
        print("\rShutting down server")


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
    global verbose
    global html
    global mdhash
    global inputfile

    parser.add_argument('--version', action='store_true')
    parser.add_argument('--input', '-i', metavar='MD',
                        help='input markdown file (otherwise STDIN)')
    parser.add_argument('--output', '-o', metavar='HTML',
                        help='output html file (otherwise STDOUT)')
    parser.add_argument('--login', '-l', action='store_true',
                        help='allows for more requests')
    parser.add_argument('--bare', '-b', action='store_true',
                        help='disable standalone html (gives fragment)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='displays server output and rate information')
    parser.add_argument('--serve', '-s', action='store_true',
                        help='locally serve parsed markdown')
    parser.add_argument('--port', '-p', metavar='PORT')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    inputfile = args.input
    if args.input:
        if os.path.isfile(args.input):
            with open(args.input, 'r', encoding='utf-8') as markdown:
                data = "".join(markdown.readlines())
        else:
            sys.stderr.write("Input file doesn't exist\n")
            sys.exit(1)
    else:
        try:
            data = "".join(sys.stdin.readlines())
        except KeyboardInterrupt:
            print()
            sys.exit(1)

    if args.login:
        from getpass import getpass

        try:
            username = input("GitHub username: ")
            password = getpass()
            login = Login(username, password)
        except KeyboardInterrupt:
            print()
            sys.exit(1)
    else:
        login = Login()

    verbose = args.verbose
    html = html_from_markdown(data)
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    mdhash = m.hexdigest()

    if not args.bare:
        html = standalone(html)
    if args.serve:
        run_server(args.port or '8000')
    elif args.output:
        with open(args.output, 'w') as out:
            out.write(html)
    else:
        print(html)


if __name__ == '__main__':
    main()

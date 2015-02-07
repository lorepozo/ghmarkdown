# ghmarkdown
The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

ghmarkdown is much more honed-in than [pandoc](http://johnmacfarlane.net/pandoc), a **massive** tool with *far* more conversion capabilities (but lacking its own hosting capabilities).

## Features

- Host your markdown locally to easily view your changes!
- Easy to [install](#installation)
- Easy to [use](#usage)
- Works on Mac, Linux, and Windows

## Installation
```bash
pip install ghmarkdown
```

## Usage
Run your markdown on a local server:
```bash
# these do the same thing
$ ghmarkdown -s -i my_file.md
$ ghmarkdown --serve --input my_file.md
$ cat my_file.md | ghmarkdown --serve
```

Parse your markdown to HTML locally:
```bash
# these do the same thing
$ ghmarkdown -i my_file.md -o my_page.html
$ ghmarkdown --input my_file.md --output my_page.html
$ cat my_file.md | ghmarkdown > my_page.html
```

Write markdown directly into stdin, and serve it:

<pre>
$ ghmarkdown --serve
# Hello there, _user_!
```python
def foo(bar):
    raise ZeroDivisionError()
```
&lt;Ctrl-d&gt;
Hosting server on port 8000
</pre>


Use `ghmarkdown --help` to see all available commands and parameters


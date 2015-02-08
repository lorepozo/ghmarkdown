# ghmarkdown
The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

ghmarkdown's `--serve` feature let's you locally view your markdown __live__, so you can view your changes as you work!

![example usage gif](http://i.imgur.com/WUCWpOM.gif)

## Features

- Host your markdown locally to easily view your changes _as you make them_!
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
$ ghmarkdown -si my_file.md
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


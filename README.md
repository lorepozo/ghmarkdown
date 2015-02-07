# ghmarkdown
The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

## Features

- Easy to [install](https://github.com/lukedmor/ghmarkdown#installation)
- Easy to [use](https://github.com/lukedmor/ghmarkdown#usage)
- Works on Mac, Linux, and Windows

## Installation
```bash
pip install ghmarkdown
```

## Usage
Run your markdown on a local server:
```bash
$ ghmarkdown --serve --input my_file.md
$ # or, with more bash:
$ cat my_file.md | ghmarkdown --serve
```

Save your markdown locally:
```bash
$ ghmarkdown --input my_file.md --output my_page.html
$ # or, with more bash:
$ cat my_file.md | ghmarkdown > my_page.html
```

Write markdown directly into stdin:

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

## Similar

- https://github.com/msabramo/setuptools-markdown -- this will call `pandoc` on the fly for you to transform Markdown to reST when you register the package with PyPI. So you can write your README exclusively in Markdown and have the description still render nicely on PyPI. Requires pandoc. 

- https://github.com/msabramo/pydocverter -- this is similar to your package, but it uses Docverter, which is a Web service that uses pandoc and Calibre to transform and render documents with various formats, including Markdown. 

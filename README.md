# ghmarkdown
The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

## Features

- Easy to [install](https://github.com/karan/joe#installation)
- Easy to [use](https://github.com/karan/joe#usage)
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
$ cat my_file.md | ghmarkdown | my_page.html
```

Use `ghmarkdown --help` to see all available commands and parameters

# ghmarkdown

![PyPi version](https://pypip.in/v/ghmarkdown/badge.svg)
![License](https://pypip.in/license/ghmarkdown/badge.svg)

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
$ cat my_file.md | ghmarkdown --serve # doesn't update changes
```

Parse your markdown to HTML locally:
```bash
# these do the same thing
$ ghmarkdown -i my_file.md -o my_page.html
$ ghmarkdown --input my_file.md --output my_page.html
$ cat my_file.md | ghmarkdown > my_page.html
```

To refresh the local server automatically, use `ghmarkdown --auto`, which will refresh every 2 seconds to view changes at (almost) the same time you save

Use `ghmarkdown --help` to see all available commands and parameters

GitHub limits usage of its api, so if you want more than 60 req/hr use `--login` (you'll get 5000 req/hr!)


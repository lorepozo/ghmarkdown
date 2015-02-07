ghmarkdown
==========

The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

Features
--------

-  Easy to `install <https://github.com/lukedmor/ghmarkdown#installation>`__
-  Easy to `use <https://github.com/lukedmor/ghmarkdown#usage>`__
-  Works on Mac, Linux and Windows

Installation
------------

.. code:: bash

    $ pip install ghmarkdown


Usage
-----

Run your markdown on a local server:

.. code:: bash

    $ ghmarkdown --serve --input my_file.md
    $ # or, with more bash:
    $ cat my_file.md | ghmarkdown --serve


Save your markdown locally:

.. code:: bash

    $ ghmarkdown --input my_file.md --output my_page.html
    $ # or, with more bash:
    $ cat my_file.md | ghmarkdown | my_page.html


Use `ghmarkdown --help` to see all available commands and parameters
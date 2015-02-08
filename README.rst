ghmarkdown
==========

The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

ghmarkdown's `--serve` feature let's you locally view your markdown **live**, so you can view your changes as you work!

.. figure:: http://i.imgur.com/WUCWpOM.gif
   :alt: example usage gif

Features
--------

-  Host your markdown locally to easily view your changes *as you make them*!
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

    # these do the same thing
    $ ghmarkdown -si my_file.md
    $ ghmarkdown --serve --input my_file.md
    $ cat my_file.md | ghmarkdown --serve


Parse your markdown to HTML locally:

.. code:: bash

    # these do the same thing
    $ ghmarkdown -i my_file.md -o my_page.html
    $ ghmarkdown --input my_file.md --output my_page.html
    $ cat my_file.md | ghmarkdown > my_page.html


Write markdown directly into stdin, and serve it:

.. code::

    $ ghmarkdown --serve
    # Hello there, _user_!
    ```python
    def foo(bar):
        raise ZeroDivisionError()
    ```
    <Ctrl-d>
    Hosting server on port 8000


Use ``ghmarkdown --help`` to see all available commands and parameters


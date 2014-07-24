My Website
==========

My personal website which I'm in the process of moving from Joomla to Pelican.

Normally - the website is built and published automatically via [travis-ci](https://travis-ci.org/jonathanhood/website).

To build the website manually - just use the provided requirements.txt and virtualenv:
 
    > pip install virtualenv
    > git clone https://github.com/jonathanhood/website.git
    > cd website
    > git submodule init
    > git submodule update
    > virtualenv venv
    > source venv/bin/activate
    > pip install -r requirements.txt
    > make html

From that point forward, just use the established virtualenv to build:

    > cd <path/to/website>
    > source venv/bin/activate
    > make html

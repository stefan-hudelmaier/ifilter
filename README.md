# ifilter
Command line tool for interactively filtering lines in a pipe

## Quick start

    git clone https://github.com/stefan-hudelmaier/ifilter.git
    sudo setup.py install

## Example

Delete selected files in a directory

    find . | ifilter | xargs rm

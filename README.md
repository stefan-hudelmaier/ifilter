# ifilter
Command line tool for interactively filtering lines in a pipe

## Installation

    sudo pip install ifilter

## Example

Delete selected files in a directory

    find . -type f | ifilter | xargs rm

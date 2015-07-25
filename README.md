# ifilter
Command line tool for interactively filtering lines in a pipe

## Installation

    sudo pip install ifilter

## Examples

Delete selected files in a directory

    find . -type f | ifilter | xargs rm

Update a version in specific files

    ls *.xml | ifilter | xargs sed -i 's|1.0.0|1.1.0|'

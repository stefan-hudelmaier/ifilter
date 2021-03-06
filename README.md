# ifilter
Command line tool for interactively filtering lines in a pipe (inspired 
by git rebase --interactive). It will open the stdin it receives in an 
editor (it uses $EDITOR and $VISUAL and falls back to vi) and output 
it again, along with any modifications. If a line is prefixed with # 
it get's ignored.

![screencast](https://github.com/stefan-hudelmaier/ifilter/blob/master/resources/screencast.gif)

## Installation

    sudo pip install ifilter

## Examples

Delete selected files in a directory:

    find . -type f | ifilter | xargs rm

Update a version in specific files:

    ls *.xml | ifilter | xargs sed -i 's|1.0.0|1.1.0|'

Creating a .gitignore file:

    find . | ifilter > .gitignore

import sys
import tempfile
import os
from subprocess import call
import argparse

# TODO:
# Handle infinite input (/dev/null)
# Add docopt


guide = """# Remove or modify lines.
# Lines that are prefixed with the # character are filtered out.
# When you are done, save the file and exit.
"""

description = \
"""Interactively filter lines in a pipe.

Example: Delete selected files in a directory

    find . | ifilter | xargs rm
"""

def get_editor():

    if "EDITOR" in os.environ:
        return os.environ["EDITOR"]

    if "VISUAL" in os.environ:
        return os.environ["VISUAL"]

    return "vi"

def main():

    parser = argparse.ArgumentParser(
            prog='ifilter',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=description)

    # Currently args are unused
    args = parser.parse_args()

    s = sys.stdin.read()

    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(guide)
    f.write(s)
    f.close()

    editor = get_editor()

    call("</dev/tty >/dev/tty %s %s " % (editor, f.name), shell=True)

    with open(f.name, "r") as f:
      for line in f.readlines():
        if not line.startswith("#"):
          print line,

    os.remove(f.name)

if __name__ == "__main__":
    main()

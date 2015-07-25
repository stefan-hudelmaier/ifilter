import sys
import tempfile
import os
from subprocess import call

# TODO:
# Handle infinite input (/dev/null)
# Use EDITOR env variable
# Add setup.py
# Use main method
# Add docopt
# Add documentation at top

def main():

	s = sys.stdin.read()

	f = tempfile.NamedTemporaryFile(delete=False)
	f.write(s)
	f.close()

	call("</dev/tty >/dev/tty vi " + f.name, shell=True)
	#call("</dev/tty >/dev/tty nano " + f.name, shell=True)

	with open(f.name, "r") as f:
		for line in f.readlines():
			if not line.startswith("#"):
				print line,

	os.remove(f.name)

if __name__ == "__main__":
	main()

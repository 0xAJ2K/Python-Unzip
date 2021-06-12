#!/usr/bin/env python3
import argparse
from zipfile import PyZipFile

def error():
     parser.print_help()
     quit()

parser = argparse.ArgumentParser(description='Args')
requiredNamed = parser.add_argument_group('Required Arguments')
parser.add_argument("-f", dest="file", help="The ZIP file to unzip.")
args = parser.parse_args()

try:
	pzf = PyZipFile(args.file)
	pzf.extractall()
except:
	error()

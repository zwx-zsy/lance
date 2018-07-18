#!/usr/bin/env python
# coding: utf-8
# Date  : 2018-07-16 10:40:08
# Author: b4zinga
# Email : b4zinga@outlook.com
# Func  :

from lib.cmdline import cmdLineParser
from lib.loader import loadPlugin


def main():
	args = cmdLineParser()

	if args.target:
		url = args.target
	if args.module:
		plugin = args.module
	else:
		plugin=None

		
	loadPlugin(url=url, poc=plugin)
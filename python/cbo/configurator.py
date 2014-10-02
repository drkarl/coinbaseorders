#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ConfigParser, inspect

conf = ConfigParser.ConfigParser()
conf.read("./conf/cbo.conf")

def getPath(name):
	path = conf.get('path', name)
	if not os.path.exists(path):
		os.makedirs(path)
	return path

def mysqlString():
	return 'mysql://%s:%s@%s/%s' % (conf.get('mysql', 'user'), conf.get('mysql','password'), conf.get('mysql','ip'), conf.get('mysql','db'))

def getGmailAuth(key):
	if conf.get('services','email') != 'gmail':
		return None
	return conf.get('gmail', key)

def getDebugEmail():
	return conf.get('debug', 'email')

def isDebugOn():
	return conf.get('debug', 'enabled')
#!/usr/bin/env python

import os
import subprocess

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PATH_TO_CRONJOB = os.path.join(SCRIPT_DIRECTORY, '.crontab')
PATH_TO_JVR = os.path.join(SCRIPT_DIRECTORY, 'jvr.py')

def get_crontab():
	crontab = open(PATH_TO_CRONJOB, 'w')
	crontab.write('*/5 * * * * ' + PATH_TO_JVR)
	crontab.close()
	return crontab.name

if __name__ == '__main__':
	print PATH_TO_JVR
	make_executable = subprocess.Popen(['chmod', '+x', PATH_TO_JVR], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
	print make_executable

	print get_crontab()

	final_path_cronjob = os.path.join(os.environ.get('HOME'), '.crontab')
	activate_cronjob = subprocess.Popen(['crontab', final_path_cronjob], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
	print activate_cronjob

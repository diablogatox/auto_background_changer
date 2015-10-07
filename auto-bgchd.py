#!/usr/bin/python3
import argparse
import os
import sys
import time

from daemon_util import *

parser = argparse.ArgumentParser(description='random wallpaper changer')
parser.add_argument('-dir', dest='bg_dir', type=str, help='wallpaper directory')
parser.add_argument('-intv', dest='intv', type=int, default=60, help='interval of changing wallpaper')
args = parser.parse_args()

if is_daemon_start() == False:
	from bgch_core import *
	try:
		bg_core_obj = BgChCore(bgdir = args.bg_dir, interval = args.intv)
		daemonize(bg_core_obj.main_func)
	except Exception as e:
		print('Error: {0}'.format(e))
else:
	print ('auto-bgchd is already running...')

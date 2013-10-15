#!/usr/bin/env python

import os

CONVERT_FORMAT_LIST = ['mkv', 'avi']

def ensure_path(path):
  try: 
    os.makedirs(path)
  except OSError:
    if not os.path.isdir(path):
        raise

def get_format(file_path):
  format = os.path.splitext(file_path)[1]
  format = format.replace('.', '')
  return format.lower()

def should_handle_format(video):
  format = get_format(video)
  if format in CONVERT_FORMAT_LIST:
    return True
  else:
    return False

if __name__ == '__main__':
  ensure_path('/Users/jzucker/PVR/Processing')
  ensure_path('/Users/jzucker/PVR/Processing')
  ensure_path('/Users/jzucker/PVR/Rejects')

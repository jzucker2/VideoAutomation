#!/usr/bin/env python

import os
import datetime

CONVERT_FORMAT_LIST = ['mkv', 'avi']
SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
LOG_FOLDER = os.path.join(SCRIPT_DIRECTORY, 'Logs')

def ensure_path(path):
  try: 
    os.makedirs(path)
  except OSError:
    if not os.path.isdir(path):
        raise

def get_log_path():
  ensure_path(LOG_FOLDER)
  current_time = datetime.date.today()
  current_time_string = current_time.strftime('%m-%d-%Y')
  log_file = 'jvr.log.' + current_time_string + '.txt'
  return os.path.join(LOG_FOLDER, log_file)

def log(log_message):
  log_path = get_log_path()
  with open(log_path, 'a') as log:
    log_line = str(datetime.datetime.today()) + ':  ' + str(log_message) + '\n'
    log.write(log_line)

def get_conversion_formats():
  return CONVERT_FORMAT_LIST

def get_format(file_path):
  format = os.path.splitext(file_path)[1]
  format = format.replace('.', '')
  return format.lower()

def should_handle_format(video, formats):
  format = get_format(video)
  if format in formats:
    return True
  else:
    return False

if __name__ == '__main__':
  ensure_path('/Users/jzucker/PVR/Processing')
  ensure_path('/Users/jzucker/PVR/Processing')
  ensure_path('/Users/jzucker/PVR/Rejects')
  
  log('hey now')
  log('what up, buttercup')

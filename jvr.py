#!/usr/bin/env python

import os

import jvr_helper
import video
import queue_handler
import completed_folder_handler

script_location = os.path.dirname(os.path.realpath(__file__))
QUEUE_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Queue')
PROCESSING_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Processing')
REJECT_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Rejects')
CONVERTED_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Converted')
WATCH_FOLDER = os.path.join(os.environ.get('HOME'), 'PVR/Completed')

def main():
  jvr_helper.log('start jvr')
  completed_downloads_folder_handler = completed_folder_handler.CompletedFolderHandler(queue_folder=QUEUE_FOLDER, watch_folder=WATCH_FOLDER)
  completed_downloads_folder_handler.move_to_queue()
  queue = queue_handler.QueueHandler(queue_folder=QUEUE_FOLDER, processing_folder=PROCESSING_FOLDER, reject_folder=REJECT_FOLDER, converted_folder=CONVERTED_FOLDER)
  queue.process()

if __name__ == '__main__':
  main()
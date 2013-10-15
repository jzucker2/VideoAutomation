#!/usr/bin/env python

import video_collector
import video

import os

script_location = os.path.dirname(os.path.realpath(__file__))
QUEUE_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Queue')
WATCH_FOLDER = os.path.join(os.environ.get('HOME'), 'PVR/Completed')

class CompletedFolderHandler():
  def __init__(self, **kwargs):
    self.queue_folder = kwargs.get('queue_folder', QUEUE_FOLDER)
    self.watch_folder = kwargs.get('watch_folder', WATCH_FOLDER)
    self.video_collector = video_collector.VideoListCollector(watch_folder=self.watch_folder)
  def move_to_queue(self):
    new_videos_list = self.video_collector.get_all_new_videos()
    for new_video in new_videos_list:
      new_video.move(self.queue_folder, True)



def main():
  completed_folder_handler = CompletedFolderHandler()
  completed_folder_handler.move_to_queue()


if __name__ == '__main__':
  main()
#!/usr/bin/env python

import jvr_helper
import video

import os


WATCH_FOLDER = os.path.join(os.environ.get('HOME'), 'PVR/Completed')

class VideoListCollector():
  def __init__(self, **kwargs):
    self.watch_folder = kwargs.get('watch_folder', WATCH_FOLDER)
    self.videos = []
  def get_full_path(self, item):
    return os.path.join(self.watch_folder, item)
  def get_all_video_folders(self):
    video_folders = []
    for folder in os.listdir(self.watch_folder):
      if os.path.isdir(self.get_full_path(folder)):
        video_folders.append(self.get_full_path(folder))
    return video_folders
  def add_video_from_folder(self, folder):
    for item in os.listdir(folder):
      full_path = os.path.join(folder, item)
      if (jvr_helper.should_handle_format(item)) and (item.find('sample') ==-1) and not (os.path.isdir(full_path)):
        #full_path = os.path.join(folder, item)
        self.videos.append(video.Video(source=full_path))
  def get_all_new_videos(self):
    video_folders = self.get_all_video_folders()
    for folder in video_folders:
      self.add_video_from_folder(folder)
    # now add loose videos
    self.add_video_from_folder(self.watch_folder)
    return self.videos

if __name__ == '__main__':
  video_collector = VideoListCollector(watch_folder='/Users/jzucker/PVR/Completed')
  new_videos = video_collector.get_all_new_videos()
  for video in new_videos:
    print video.source
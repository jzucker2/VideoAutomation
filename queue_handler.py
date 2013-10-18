#!/usr/bin/env python

import os

import video
import converter
import jvr_helper

script_location = os.path.dirname(os.path.realpath(__file__))
QUEUE_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Queue')
PROCESSING_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Processing')
REJECT_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Rejects')
CONVERTED_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Converted')

class QueueHandler:
  def __init__(self, **kwargs):
    self.queue_folder = kwargs.get('queue_folder', QUEUE_FOLDER)
    self.processing_folder = kwargs.get('processing_folder', PROCESSING_FOLDER)
    self.reject_folder = kwargs.get('reject_folder', REJECT_FOLDER)
    self.converted_folder = kwargs.get('converted_folder', CONVERTED_FOLDER)
    self.converter = converter.Converter(processing_folder=self.processing_folder, converted_folder=self.converted_folder)
  def get_videos(self):
    return [video.Video(source=(os.path.join(self.queue_folder, video_path))) for video_path in os.listdir(self.queue_folder)]
    #return [video.Video(source=video_path) for video_path in os.listdir(self.queue_folder)]
  def remove_video(self, old_video):
    os.unlink(old_video.source)
  def process_video(self, new_video):
    jvr_helper.log('process_video')
    jvr_helper.log(new_video.source)
    if (new_video == None) or (new_video.source == '.DS_Store'):
      return
    jvr_helper.log('move new_video')
    new_video.move(self.processing_folder)
    jvr_helper.log('finish move')
    jvr_helper.log(new_video.source)
    if self.converter.convert(new_video, self.converted_folder):
      jvr_helper.log('success, now remove')
      self.remove_video(new_video)
    else:
      jvr_helper.log('failure')
      new_video.move(self.reject_folder)
  def process(self):
    videos = self.get_videos()
    jvr_helper.log(videos)
    for new_video in videos:
      self.process_video(new_video)


if __name__ == '__main__':
  print 'main'
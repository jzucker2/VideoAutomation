#!/usr/bin/env python

import os
import subprocess

import jvr_helper
import video

PROCESSING_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Processing')
CONVERTED_FOLDER = os.path.join(os.environ.get('HOME'), 'Movies/Converted')

class Converter:
  def __init__(self, **kwargs):
    self.processing_folder = kwargs.get('processing_folder', PROCESSING_FOLDER)
    self.converted_folder = kwargs.get('converted_folder', CONVERTED_FOLDER)
  def get_command(self, new_video):
    command = ['/usr/local/bin/ffmpeg', '-i', new_video.source]
    if new_video.get_format() == 'mkv':
      command.extend(['-y', '-f', 'mp4', '-vcodec', 'copy', '-ac', '2', '-c:a', 'libfaac'])
    elif new_video.get_format() == 'avi':
      command.extend(['-vcodec', 'libx264'])
    else:
      jvr_helper.log('unrecognized format: ' + new_video.get_format())
      raise 'unrecognized format'
    jvr_helper.log(new_video.get_destination(self.converted_folder))
    #command.append(new_video.get_destination(self.converted_folder))
    command.append(new_video.get_converted_file_path(self.converted_folder))
    return command

  def convert(self, new_video, destination_directory):
    jvr_helper.log('------------')
    new_video.move(self.processing_folder)
    jvr_helper.log('self.processing_folder')
    jvr_helper.log(os.listdir(self.processing_folder))
    jvr_helper.log(self.get_command(new_video))
    jvr_helper.log(' '.join(self.get_command(new_video)))
    jvr_helper.log('new video.source: ' + new_video.source)
    jvr_helper.log('original copy exists: ' + str(new_video.exists()))
    conversion = subprocess.Popen(self.get_command(new_video), stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
    jvr_helper.log('conversion ended')
    jvr_helper.log(conversion)
    jvr_helper.log('------------')
    return True


def main():
  print 'main'

if __name__ == '__main__':
  main()
#!/usr/bin/env python

import os
import jvr_helper
import shutil

class Video:
  def __init__(self, **kwargs):
    self.source = kwargs.get('source')
    #self.destination = kwargs.get('destination', None)
  def get_file(self):
    return os.path.basename(self.source)
  def get_filename(self):
    return os.path.splitext(self.get_file())[0]
  def exists(self):
    return os.path.exists(self.source)
  def get_format(self):
    return jvr_helper.get_format(self.source)
    # format = os.path.splitext(self.source)[1]
    # format = format.replace('.', '')
    # return format.lower()
  def get_destination(self, directory):
    return os.path.join(directory, self.get_file())
  def get_directory(self):
    return os.path.dirname(self.source)
  def move(self, destination_directory, deleteSourceDirectory=False):
    jvr_helper.log('move')
    jvr_helper.log(deleteSourceDirectory)
    jvr_helper.ensure_path(destination_directory)
    destination = self.get_destination(destination_directory)
    jvr_helper.log('destination: ' + destination)
    jvr_helper.log('now try to move')
    jvr_helper.log('self.source: ' + self.source)
    shutil.move(self.source, destination)
    if deleteSourceDirectory:
      shutil.rmtree(self.get_directory())
    self.source = destination
  def get_converted_file_path(self, destination_directory):
    jvr_helper.ensure_path(destination_directory)
    file_name = self.get_filename() + '.m4v'
    return os.path.join(destination_directory, file_name)


def main():
  video = Video(source='/Users/jzucker/test.s02.e01.MKV')
  #print video.source
  #print video.destination
  #print video.get_filename()
  #print os.path.splitext(video.source)[1]
  print 'video.source'
  print video.source
  print 'get_format'
  print video.get_format()
  print 'get_file'
  print video.get_file()
  print 'get_filename'
  print video.get_filename()
  print 'get_destination'
  print video.get_destination('/Users/jzucker/queue/')


if __name__ == '__main__':
  main()
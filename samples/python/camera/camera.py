"""
Copyright (c) 2022 Continental Autonomous Mobility Germany GmbH
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import argparse
import os
import sys
# import the opencv library
import cv2
import numpy as np
import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

import time

sys.path.insert(1, os.path.join(sys.path[0], '../../../datatypes_python'))
import SensorNearData.SurroundViewImage.SurroundViewImage_pb2 as SV

class RawImageHandler():
  def __init__(self, topic_name):
    self.sub = ProtoSubscriber(topic_name, SV.SurroundViewImage)
    callback = lambda topic_name, video_frame, time : self.on_image(video_frame, time)

  def get_image(self):
    ret, video_frame, time = self.sub.receive()
    if ret > 0:
      data = video_frame.data
      #image = np.zeros((data.width, data.height,3),  np.uint8)
      image = np.frombuffer(data.imageData, np.uint8)
      image = image.reshape((data.height, data.width, 3))
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      return [True, image]
    return [False, None]



def main(args):
  # print eCAL version and date
  print("eCAL {} ({})\n".format(ecal_core.getversion(), ecal_core.getdate()))
  
  # initialize eCAL API
  ecal_core.initialize(sys.argv, "opencv python viewer")
  image_handler = RawImageHandler(args.topic_name)

  while ecal_core.ok():
    [has_image, image] = image_handler.get_image()
    if has_image:
      cv2.imshow('camera image', image)
    cv2.waitKey(1)
  ecal_core.finalize()


def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument("--topic-name", dest="topic_name", help="topic name to subscribe", default='SvcImageFrontRgbPb')
  return parser

if __name__ == "__main__":
  parser = create_parser()
  args = parser.parse_args()
  main(args)  
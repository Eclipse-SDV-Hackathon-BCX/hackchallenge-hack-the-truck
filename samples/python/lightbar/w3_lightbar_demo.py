"""
Copyright (c) 2022 Continental Autonomous Mobility Germany GmbH
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time

import ecal.core.core as ecal_core
from ecal.core.publisher import ProtoPublisher

import W3Lightbar_pb2

def main():
  ecal_core.initialize([], "test_w3_lightbar")
  pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
  
  pb_msg = W3Lightbar_pb2.W3LightbarRequest()
  
  wait_time = 3

  while ecal_core.ok():
    pb_msg.Clear();
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.take_down = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.alley_light_left = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.alley_light_right = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.red_warning_light = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.three_sixty_degree_colour_2 = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
  
    pb_msg.Clear();
    pb_msg.front_colour_2 = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.turn_signal_left = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.turn_signal_right = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
    pb_msg.Clear();
    pb_msg.take_down = True;
    pb_msg.alley_light_left = True;
    pb_msg.alley_light_right = True;
    pb_msg.red_warning_light = True;
    pb_msg.three_sixty_degree_colour_2 = True;
    pb_msg.front_colour_2 = True;
    pb_msg.turn_signal_left = True;
    pb_msg.turn_signal_right = True;
    pub.send(pb_msg)
    time.sleep(wait_time)
    
  ecal_core.finalize()

if __name__ == "__main__":
  main()

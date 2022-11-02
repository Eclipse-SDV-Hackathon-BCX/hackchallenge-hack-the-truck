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

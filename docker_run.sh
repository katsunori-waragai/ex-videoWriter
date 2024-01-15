#!/bin/bash
sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v ~/github/yolox-docker:/root/yolox/yolox_data -v /tmp/.X11-unix/:/tmp/.X11-unix opencv:100
  

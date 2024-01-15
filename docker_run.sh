#!/bin/bash
sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v ~/github/ex-videoWriter:/root/ex-videoWriter -v /tmp/.X11-unix/:/tmp/.X11-unix opencv:100
  

#!/bin/bash

xhost +local:docker

docker run --privileged --rm -it \
  --env DISPLAY=$DISPLAY \
  --env="QT_X11_NO_MITSHM=1" \
  -v /dev/video0:/dev/video0:ro \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro  \
  -v $PWD:/code \
   narenm/opencv:3.3.0 bash

xhost -local:docker

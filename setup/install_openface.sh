#!/bin/bash

# Install OpenCV and other dependencies
apt-get update
apt-get install -y cmake git libboost-all-dev
apt-get install -y libopencv-dev python3-opencv
apt-get install -y libeigen3-dev libgtk2.0-dev

# Clone OpenFace repository
git clone https://github.com/TadasBaltrusaitis/OpenFace.git

# Build OpenFace
cd OpenFace
mkdir build
cd build
cmake ..
make

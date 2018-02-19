# 2018-ptmr: Installation from Source Code

First install the dependencies:
- [Install CMake](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-cmake.md)
- [Install YARP](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
- [Install OpenRAVE](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-openrave.md)

Additionally, this project depends on YCM to download and build external packages. Although this process is intended to run automatically during the CMake configuration phase, you may still want to install YCM and said packages by yourself. In that respect, refer to [Install YCM](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-ycm.md) and to the installation guides of any package listed below:

- [color-debug](https://github.com/roboticslab-uc3m/color-debug)

### Install 2018-ptmr on Ubuntu (working on all tested versions)

Our software integrates the previous dependencies. Note that you will be prompted for your password upon using `sudo` a couple of times:

```bash
cd  # go home
mkdir -p repos; cd repos  # create $HOME/repos if it does not exist; then, enter it
git clone https://github.com/roboticslab-uc3m/2018-ptmr.git  # Download 2018-ptmr software from the repository
cd 2018-ptmr; mkdir build; cd build; cmake ..  # Configure the 2018-ptmr software
make -j$(nproc)  # Compile
sudo make install  # Install :-)
sudo ldconfig  # Just in case...
cd  # go home
```

For CMake `find_package(ROBOTICSLAB_OPENRAVE_YARP_PLUGINS REQUIRED)`, you may also be interested in adding the following to your `~/.bashrc` or `~/.profile`:
```bash
export ROBOTICSLAB_OPENRAVE_YARP_PLUGINS_DIR=$HOME/repos/2018-ptmr/build  # Points to where OPENRAVE_YARP_PLUGINSConfig.cmake is generated upon running CMake
```

For additional options use `ccmake` instead of `cmake`.

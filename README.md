# pynoxim
Pynoxim is not Python bindings of [noxim](https://github.com/davidepatti/noxim) but Python script to run noxim in a simple and better way. Noxim is written by Dr. Davide Patti and his team which simulates a wired or wireless network-on-chip (NoC). Noxim uses YAML based configuration to run a network-on-chip simulation, at a time, you can only run one network configuration. As we know that we require simulations performed at different packet injection rate (PIR), different routing algorithm. If we will run simulations creating different YAML files for all desired parameters, we will have to create and edit various YAML config files. Pynoxim is written to minimize this work and speed up the result acquisition and plotting. 

Different parameters can be given ranges and different standard plots can be generated quick. Pynoxim simply generates the YAML config files (using pyyaml module) for the parametric analysis and runs it through noxim. After simulation it records the results in a csv file (using numpy module) and also generates plot files using matplotlib module. Pynoxim is cross-platform script. Only Noxim is required to be compiled for desired platform.

Pynoxim is written as a course  project (for 'Design and Test of Multi-core chips') by Rounak Singh under [Dr. Amlan Ganguly](https://www.rit.edu/kgcoe/staff/amlan-ganguly) at Rochester Institute of Technology, Rochester, NY, USA.


## Prerequisites
1) noxim -- compile it using the script or instructions found here. https://github.com/davidepatti/noxim
2) Install python > version 3.5. https://www.python.org/downloads/ Make sure that you have updated version of pip and setuptools.
3) Matplotlib -- python module for plotting
4) pyyaml -- python module for YAML
5) numpy -- python module for numerical matrices and analysis.

Run the following command to install remaining dependency.
```bash
$ pip3 install matplotlib pyyaml numpy
```
If you have python 2 also installed on your system, make sure that you are using python3 by using 
```bash
$ python3 ./pynoxim.py
```
or enter following at the bottom of the ~/.bashrc file. It will make 'python' and 'pip' to point to python version 3.x

    alias python=python3
    alias pip=pip3


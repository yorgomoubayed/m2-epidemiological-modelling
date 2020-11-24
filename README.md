# Project features
* Describes the SIRC (susceptible-infectious-recovered-carrier) epidemiological model.
* Integrates the model equations in python code.
* Describes the system's parameters and their influences by solving the system of ordinary differential equations for different initial conditions and different parameter values.

# Repository contents
This repository contains essential scripts for running SIRC model simulations as well as supplementary scripts to run SIR model simulations: 

* sirc.py: provides a python implementation of the SIRC model's ODEs.
* sirc.R: provides an R implementation of the SIRC model's ODEs.
* sir.py: provides a python implementation of the SIR model's ODEs.
* sirsirc.yml: a conda environment provided to setup and install the required libraries to run python simulations for sir and sirc models.

# Before running simulations
To setup the conda environment with dependancies, run the following:
~~~
conda env create -f sirsirc.yml
~~~

# References



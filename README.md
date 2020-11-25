# Project features
* Describes the SIRC (susceptible-infectious-recovered-carrier) epidemiological model.
* Integrates the model equations in python code.
* Describes the system's parameters and their influences by solving the system of ordinary differential equations for different initial conditions and different parameter values.

# Repository contents
This repository contains essential scripts for running SIRC model simulations as well as supplementary scripts to run SIR model simulations: 

* sirsirc.yml: a conda environment provided to setup and install the required libraries to run python simulations for SIR and SIRC models.
* sirc.py: provides a python implementation of the SIRC model's ODEs.
* sirc.R **(1)**: provides an R implementation of the SIRC model's ODEs.
* sir.py **(2)**: provides a python implementation of the SIR model's ODEs.

# Before running simulations
To setup the conda environment with dependancies, download the sirsirc.yml file and run the following:
~~~
conda env create -f sirsirc.yml
~~~

# References

* (1) <https://rstudio-pubs-static.s3.amazonaws.com/111132_79dd08ebb42e4e2d927c4a88729b72bd.html>         
* (2) <https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/>        
* Jinde Cao, Yi Wang, Abdulaziz Alofi, Abdullah Al-Mazrooei, Ahmed Elaiw, **Global stability of an epidemic model with carrier state in heterogeneous networks**, IMA Journal of Applied Mathematics, Volume 80, Issue 4, August 2015, Pages 1025–1048.     
* **Modelling Epidemics**, Lecture 5: Deterministic compartmental epidemiological models in homogeneous populations, Andrea Doeschl-Wilson
* **Lectures on Mathematical Modelling of Biological Systems**, G. Bastin, 2018


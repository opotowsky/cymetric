#! /usr/bin/env python

import os
import sqlite3
import tables
import numpy as np
from tools import safe_call 

def change_input(ref_input, growth_factor):
    """Changes a growth factor of the Growth Region of the input file.

    Args:
        ref_input: The path to the reference input file 
	growth_factor: A tuple of (growth factor, initial y value).

    Returns:
        A path to a file with an updated growth factor.
    """
    growth_factor = growth_factor[0]
    y_init = growth_factor[1]

    # A file to be created
    new_sim = ref_input.split(".xml")[0] + "_" + str(growth_factor[0]) + \
              "_" + ".xml"
    sim = open(new_sim, "w")
    ref = open(ref_input, "r")
    
    # Change the growth factor value in the input file
    # need more robust method for initial y value
    for f in ref:
        if f.count("params"):
            f = f.split("<")[0] + "<params>" + str(growth_factor) + \
                " " + str(y_init) + "</params>\n"
        # write the rest of the file
        sim.write(f)
    
    # Closing open files
    ref.close()
    sim.close()

    return new_sim

def rm_out(outfile):
    """
    Deletes an output simulation file
    """
    # Removes output files
    if os.path.exists(outfile):
        os.remove(outfile)

def test_facilities():
    """
    Diff growth factors for otherwise equivalent sims to study
    effect of facility # on cymetric processing time
    """
    
    # Simulation input file for performance testing
    ref_input = "./testing.xml"
    # Growth factors to change the number of facilities in each sim
    growth_factors = [(0, 10000), (0.5, 10000), (1, 10000)]
    # Output files
    #outfiles = ["output_temp.h5", "output_temp.sqlite"]
    outfiles = ["output_temp.sqlite"]

    for gf in growth_factors:
        for outfile in outfiles:
	    rm_out(outfile)
	    sim_input = change_input(ref_input, gf)
            cmd = ["cyclus", "-o", outfile, "--input-file", sim_input]
            safe_call(cmd)
	    
	    # Cym processing stuff goes here
	    print('something')
    return


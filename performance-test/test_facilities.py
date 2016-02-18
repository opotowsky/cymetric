#! /usr/bin/env python

import os
import sqlite3
import tables
import numpy as np
from tools import safe_call, rm_file, change_input, fill_defaults

def test_facilities():
    """
    Diff growth factors for otherwise equivalent sims to study
    effect of facility # on cymetric processing time
    """
    
    # Simulation input file for performance testing
    ref_input = "./testing.xml"
    # Growth factors to change the number of facilities in each sim
    growth_factors = ["0 10000", "0.5 10000", "1 10000"]
    # Output files
    #outfiles = ["output_temp.h5", "output_temp.sqlite"]
    outfiles = ["output_temp.sqlite"]
    searchfor="GRUYERE"
    for gf in growth_factors:
        for outfile in outfiles:
            rm_file(outfile)
            db = outfile.split(".sqlite")[0] + "_" + str(gf) + ".sqlite"
            sim_input = change_input(ref_input, gf, searchfor)
            full_input = fill_defaults(sim_input)
            cmd = ["cyclus", "-o", db, "--input-file", full_input]
            safe_call(cmd)
#            rm_file(full_input)      

            # Cym processing stuff goes here
            print('something')
            rm_file(db)
    return

test_facilities()

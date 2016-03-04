#! /usr/bin/env python

import os
import sqlite3
import tables
import numpy as np
from tools import safe_call, rm_file, change_input, cym_time

def test_facilities():
    """
    Diff growth factors for otherwise equivalent sims to study
    effect of facility # on cymetric processing time
    """
    # Simulation input file for performance testing
    ref_input = "./testing.xml"
    # Growth factors to change the number of facilities in each sim
    growth_factors = ["0 10000", "10 10000", "100 10000"]
    # Key for defaults dict
    key = "growrate"
    # Output files
    #outfiles = ["output_temp.h5", "output_temp.sqlite"]
    outfiles = ["output_temp.sqlite"]
    # Decay, yes and no
    decay = [False, True]
    # Write to db, yes and no
    dbwrite = ["--no-write", "--write"]

    times = []
    for gf in growth_factors:
        for outfile in outfiles:
            for d in decay:
                for w in dbwrite:
                    db = outfile.split(".sqlite")[0] + "_" + str(gf) + ".sqlite"
                    sim_input = change_input(ref_input, gf, key, d)
                    cmd = ["cyclus", "-o", db, "--input-file", sim_input]
                    safe_call(cmd)
                    rm_file(sim_input)      
                    
                    # Get some info on cymetric processing time
                    cym_cmd = ["cymetric", db, w, "-e", "Agents[:]"]
                    time = cym_time(cym_cmd)
                    times.append([gf, outfile, d, w, time])
                    rm_file(db)
    print times
    return

if __name__ == "__main__":
    test_facilities()

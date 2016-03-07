#! /usr/bin/env python

import os
import sqlite3
import tables
import numpy as np
from tools import safe_call, rm_file, change_input, cym_time, write_csv

def test_facilities(ref_input, outfile, decaybool, writeflag):
    """
    Diff growth factors for otherwise equivalent sims to study
    effect of facility # on cymetric processing time
    """
    # Growth factors to change the number of facilities in each sim
    growth_factors = ["0 10000", "10 10000", "100 10000"]
    # Key for defaults dict
    key = "growrate"
    times = []
    for gf in growth_factors:
        db = outfile.split(".sqlite")[0] + "_" + str(gf) + ".sqlite"
        sim_input = change_input(ref_input, gf, key, decaybool)
        cmd = ["cyclus", "-o", db, "--input-file", sim_input]
        safe_call(cmd)
        rm_file(sim_input)      
        
        # Get some info on cymetric processing time
        cym_cmd = ["cymetric", db, writeflag, "-e", "Agents[:]"]
        time = cym_time(cym_cmd)
#        times.append([gf, decaybool, writeflag, time])
        fachead = ['GrowthFactor', 'Decay', 'WriteFlag', 'Time']
        factime = {'GrowthFactor':gf, 'Decay':decaybool, 'WriteFlag':writeflag, 'Time':time}
        write_csv('facilitynum.csv', fachead, factime)    
        rm_file(db)
    return times

def main():
    # Simulation input file for performance testing
    ref_input = "./testing.xml"
    # Output files
    #outfiles = ["output_temp.h5", "output_temp.sqlite"]
    outfiles = ["output_temp.sqlite"]
    # Decay: yes and no
    decay = [False, True]
    # Write to db: yes and no
    dbwrite = ["--no-write", "--write"]

    for outfile in outfiles:
        for d in decay:
            for w in dbwrite:
                test_facilities(ref_input, outfile, d, w)

    return

if __name__ == "__main__":
    main()

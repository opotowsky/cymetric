#! /usr/bin/env python

import os
import sqlite3
import tables
import numpy as np
from tools import safe_call, rm_file, change_input, cym_time, write_csv, run_test

def test_timestep(ref_input, outfile, decaybool, writeflag):
    """
    """
    # Set of input parameters to change the simulation duration
    params = [["2400"], ["10000"], ["100000"], ["1000000"], ["5000000"]]
    # Key for defaults dict
    keys= ["simdur"]
    table = "Transactions[:]"
    colname = "TimestepDur"
    run_test(ref_input, outfile, decaybool, writeflag, params, keys, table, colname)
    return

def test_timestep(ref_input, outfile, decaybool, writeflag):
    """
    """
    # Set of input parameters to change the simulation duration
    params = [["2400"], ["10000"], ["100000"], ["1000000"], ["5000000"]]
    # Key for defaults dict
    keys= ["simdur"]
    table = "Transactions[:]"
    colname = "TimestepDur"
    run_test(ref_input, outfile, decaybool, writeflag, params, keys, table, colname)
    return

def test_facilities_initial(ref_input, outfile, decaybool, writeflag):
    """
    """
    # Two sets of input parameters to change the number of facilities in each sim
    params = [["10", "0 10000"], ["100", "0 100000"], ["1000", "0 1000000"], ["10000", "0 10000000"]]
    # Key for defaults dict
    keys= ["facnum", "growrate"]
    table = "Agents[:]"
    colname = "InitFacilityNum"
    run_test(ref_input, outfile, decaybool, writeflag, params, keys, table, colname)
    return

def test_facilities_growth(ref_input, outfile, decaybool, writeflag):
    """
    Diff growth factors for otherwise equivalent sims to study
    effect of facility # on cymetric processing time
    """
    # Growth factors to change the number of facilities in each sim
    params = [["0 10000"], ["10 10000"], ["100 10000"], ["1000 10000"], ["10000 10000"]]
    # Key for defaults dict
    keys = ["growrate"]
    table = "Agents[:]"
    colname = "GrowthFactor"
    run_test(ref_input, outfile, decaybool, writeflag, params, keys, table, colname)
    return

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
                #test_facilities_growth(ref_input, outfile, d, w)
                #test_facilities_initial(ref_input, outfile, d, w)
                test_timestep(ref_input, outfile, d, w)

    return

if __name__ == "__main__":
    main()

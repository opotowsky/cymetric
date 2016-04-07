#! /usr/bin/env python

import os
import tables
import numpy as np
from tools import safe_call, rm_file, change_input, cym_time, write_csv, table_count

def test_timestep():
    """
    """
    # Set of input parameters to change the simulation duration
    params = [["2400"], ["5000"], ["10000"], ["50000"], ["100000"], ["500000"]]
    # Key for defaults dict
    keys= ["simdur"]
    table = "TransactionQuantity[:]"
    colname = "TimestepDur"
    run_test(params, keys, table, colname)
    return

def test_facilities_initial():
    """
    """
    # Two sets of input parameters to change the number of facilities in each sim
    params = [["10", "0 10000"], ["100", "0 100000"], ["1000", "0 1000000"], ["5000", "0 5000000"]]
    # Key for defaults dict
    keys= ["facnum", "growrate"]
    table = "TransactionQuantity[:]"
    colname = "InitFacilityNum"
    run_test(params, keys, table, colname)
    return

def test_facilities_growth():
    """
    Diff growth factors for otherwise equivalent sims to study
    effect of facility # on cymetric processing time
    """
    # Growth factors to change the number of facilities in each sim
    params = [["0 10000"], ["10 10000"], ["100 10000"], ["1000 10000"], ["5000 10000"]]
    # Key for defaults dict
    keys = ["growrate"]
    table = "TransactionQuantity[:]"
    colname = "GrowthFactor"
    run_test(params, keys, table, colname)
    return

def run_test(params, keys, table, colname):
    """
    """
    # Simulation input file for performance testing
    ref_input = "./testing.xml"
    # Output files
    #outfiles = ["output_temp.h5", "output_temp.sqlite"]
    outfiles = ["output_temp.sqlite"]
    # Nucs tracked
    nucs = ['three', 'eight', 'nea_spent_uox']
    for outfile in outfiles:
        for param in params:
            for n in nucs:
                db = outfile.split(".sqlite")[0] + "_" + str(keys[0]) + "_" + str(param) + ".sqlite"
                sim_input = change_input(ref_input, param, keys, n)
                cmd = ["cyclus", "-o", db, "--input-file", sim_input]
                safe_call(cmd)
    
                # Get some info on cymetric processing time and save it to file
                dbwrite = ["--no-write", "--write"]
                for w in dbwrite:
                    cym_cmd = ["cymetric", db, w, "-e", table]
                    time = cym_time(cym_cmd)
                    size = os.path.getsize(db)
                    if w == "--write":
                        table_size = table_count(db, table)
                    else:
                        table_size = None 
                    head = [colname, 'NucsTracked', 'WriteFlag', 'Time', 'DbSize', 'TbSize']
                    data = {colname: param, 'NucsTracked': n,'WriteFlag': w, \
                            'Time': time, 'DbSize': size, 'TbSize': table_size}
                    write_csv(colname + '.csv', head, data)
                rm_file(sim_input)      
                rm_file(db)
    return

def main():
    test_facilities_growth()
    test_facilities_initial()
    test_timestep()
    return

if __name__ == "__main__":
    main()

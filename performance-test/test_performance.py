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
    params = [["10"], ["100"], ["1000"], ["2000"], ["5000"]]
    # Key for defaults dict
    keys= ["facnum"]
    table = "TransactionQuantity[:]"
    colname = "InitFacilityNum"
    run_test(params, keys, table, colname)
    return

def run_test(params, keys, table, colname):
    """
    """
    # Simulation input file for performance testing
    ref_input = "./testing.xml"
    # Output files
    outfiles = ["output_temp.h5", "output_temp.sqlite"]
    # Nucs tracked
    nucs = ['three', 'eight', 'nea_spent_uox']
    # Inventory tables
    inv = ['none', 'inv', 'inv_compact']
    for db in outfiles:
        for param in params:
            for i in inv:
                for n in nucs:
                    sim_input = change_input(ref_input, param, keys, n, i)
                    cmd = ["cyclus", "-o", db, "--input-file", sim_input]
                    safe_call(cmd)
        
                    # Get some info on cymetric processing time and save it to file
                    dbwrite = ["--no-write", "--write"]
                    dbtype = db.replace('output_temp.', '')
                    for w in dbwrite:
                        cym_cmd = ["cymetric", db, w, "-e", table]
                        time = cym_time(cym_cmd)
                        size = os.path.getsize(db)
                        if w == "--write" and dbtype == 'sqlite':
                            table_size = table_count(db, table)
                        else:
                            table_size = None 
                        head = [colname, 'DbType', 'Inventory', 'NucsTracked', 'WriteFlag', 'Time', 'DbSize', 'TbSize']
                        data = {colname: param, 'DbType': dbtype, 'Inventory': i, 'NucsTracked': n,'WriteFlag': w, \
                                'Time': time, 'DbSize': size, 'TbSize': table_size}
                        write_csv(colname + '.csv', head, data)
                    rm_file(sim_input)      
                    rm_file(db)
    return

def main():
    #test_facilities_initial()
    test_timestep()
    return

if __name__ == "__main__":
    main()

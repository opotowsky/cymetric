"""Tools for cymetric performance testing"""
import os
import subprocess
import time
import csv
import timeit
import sqlite3
from jinja2 import FileSystemLoader, Environment, Template

def change_input(ref_input, values, parameters, nucs, inv):
    """Changes a parameter in the input file.

    Args:
        ref_input: The path to the reference xml input file 
        value: A list of text values to be added into the xml template
        parameter: A list of text indicators in the template to replace a parameter
        nucs: A text entry to indicate how many nuclides are being tracked in the sim
        inv: A text entry to indicate whether or not to store an inventory table

    Returns:
        A path to a file with an updated input file parameter.
    """
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    defaults = {'growrate': '0 10000', 'simdur': '2400', 'cycletime': '18', \
                'outrecipe': 'three', 'decay': 'never', 'facnum': '10', \
                'expinv': 'false', 'expinv_compact': 'false'}
    ref = templateEnv.get_template(ref_input)
    # Update the defaults dict with the new value(s)
    for p, v in zip(parameters, values):
        defaults[p] = v
    # Update nuclides tracked if necessary
    if nucs != 'three':
        defaults['outrecipe'] = nucs
    # Store correct inv table
    if inv == 'inv':
        defaults['expinv'] = 'true'
    elif inv == 'inv_compact':
        defaults['expinv_compact'] = 'true'
    # Insert the defaults into the xml template
    sim = ref.render(defaults=defaults)
    # Save to a new file
    new_sim = ref_input.split(".xml")[0] + "_" + str(parameters) + ".xml"
    sim_file = open(new_sim, "w")
    for line in sim:
        sim_file.write(line)
    sim_file.close()

    return new_sim

def cym_time(cmd):
    """Gives time for execution of a command

    Args:
        cmd: A command line

    Returns:
        A value of time in seconds of the command execution
    """
    # Since function we time has an argument, it must be wrapped for timeit
    wrapped = wrapper(safe_call, cmd)
    t = timeit.Timer(wrapped).repeat(repeat=5, number=1)
    cym_time = min(t)
    return cym_time 

def wrapper(func, *args, **kwargs):
    """
    Wraps a function and its arguments into a function without arguments.
    """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def write_csv(filename, header, dictname):
    """
    csv
    """
    file_exists = os.path.isfile(filename)
    csvfile = filename
    with open(csvfile, 'a') as f:
        writer = csv.DictWriter(f, delimiter=',', fieldnames=header)
        if not file_exists:
            writer.writeheader()
        writer.writerow(dictname)

    return csvfile

def table_count(db, table):
    """
    Get number of rows in table
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM ' + table)
    info = c.fetchall()
    rows = info[0][0]
    conn.close()
                    
    return rows

def rm_file(file_path):
    """
    Deletes an output simulation file
    """
    # Removes output files
    if os.path.exists(file_path):
        os.remove(file_path)

def safe_call(cmd, shell=False, *args, **kwargs):
    """Checks that a command successfully runs with/without shell=True. 

    Args:
        cmd: A command line 

    Returns:
        Returns the process return code.
    """
    try:
        rtn = subprocess.call(cmd, shell=False, *args, **kwargs)
    except (subprocess.CalledProcessError, OSError):
        cmd = ' '.join(cmd)
        rtn = subprocess.call(cmd, shell=True, *args, **kwargs)
    return rtn     


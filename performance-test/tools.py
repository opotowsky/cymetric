"""Tools for cymetric performance testing"""
import os
import subprocess

def fill_defaults(ref_input):
    """Fills in default values for unvarying input params.

    Args:
        ref_input: The path to the reference input file 

    Returns:
        A path to a file ready to run in a simulation.
    """
    defaults = {'GRUYERE': '0 10000', 'GORGONZOLA': '2629846', 'GRANDCRU': '20000', 'GOUDA': '18'}

    # File keeps same name as old file
    new_sim = 'fullsim.sqlite'
    sim = open(new_sim, "w")
    ref = open(ref_input, "r")
    
    for key, param in defaults.iteritems():
        for f in ref:
            if key in f:
                sim.write(f.replace(key, param))
            else:
                sim.write(f)    

    # Closing open files
    ref.close()
    sim.close()

    return new_sim

def change_input(ref_input, parameter, search_text):
    """Changes a parameter in the input file.

    Args:
        ref_input: The path to the reference input file 
        parameter: A text value to replace the search text
        search_text: A text indicator of where to replace an input parameter

    Returns:
        A path to a file with an updated input file parameter.
    """
    # A file to be created
    new_sim = ref_input.split(".xml")[0] + "_" + str(parameter) + ".xml"
    sim = open(new_sim, "w")
    ref = open(ref_input, "r")
    
    # Change the value in the input file
    for f in ref:
        if search_text in f:
            sim.write(f.replace(search_text, parameter))
        else:
            sim.write(f)
    
    # Closing open files
    ref.close()
    sim.close()

    return new_sim

def rm_file(file_path):
    """
    Deletes an output simulation file
    """
    # Removes output files
    if os.path.exists(file_path):
        os.remove(file_path)

def safe_call(cmd, shell=False, *args, **kwargs):
    """Checks that a command successfully runs with/without shell=True. 
    Returns the process return code.
    """
    try:
        rtn = subprocess.call(cmd, shell=False, *args, **kwargs)
    except (subprocess.CalledProcessError, OSError):
        cmd = ' '.join(cmd)
        rtn = subprocess.call(cmd, shell=True, *args, **kwargs)
    return rtn     


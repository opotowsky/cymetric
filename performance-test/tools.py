"""Tools for cymetric performance testing"""
import os
import subprocess

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
    new_sim = ref_input.split(".xml")[0] + "_" + str(parameter) + \
              ".xml"
    sim = open(new_sim, "w")
    ref = open(ref_input, "r")
    
    # Change the value in the input file
    for f in ref:
        if search_text in f:
	    sim.write(f.replace(search_text, parameter))
	else:
  	    # write the rest of the file
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


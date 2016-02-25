"""Tools for cymetric performance testing"""
import os
import subprocess
from jinja2 import FileSystemLoader, Environment, Template

def change_input(ref_input, value, parameter):
    """Changes a parameter in the input file.

    Args:
        ref_input: The path to the reference xml input file 
        value: A text value to be added into the xml template
        parameter: A text indicator in the template to replace a parameter

    Returns:
        A path to a file with an updated input file parameter.
    """
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    defaults = {'growrate': '0 10000', 'dt': '2629846', 'assemsize': '20000', \
                'cycletime': '18', 'outrecipe': 'three'}
    ref = templateEnv.get_template(ref_input)
    defaults[parameter]=value
    sim = ref.render(defaults=defaults)
    new_sim = ref_input.split(".xml")[0] + "_" + str(parameter) + ".xml"
    sim_file = open(new_sim, "w")
    for line in sim:
        sim_file.write(line)
    sim_file.close()

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


"""Tools for cymetric performance testing"""
import os
import subprocess

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

def check_cmd(args, cwd, holdsrtn):
    """Runs a command in a subprocess and verifies that it executed properly.
    """
    if not isinstance(args, basestring):
        args = " ".join(args)
    print("TESTING: running command in {0}:\n\n{1}\n".format(cwd, args))
    f = tempfile.NamedTemporaryFile()
    env = dict(os.environ)
    env['_'] = subprocess.check_output(['which', 'cyclus'], cwd=cwd).strip()
    rtn = subprocess.call(args, shell=True, cwd=cwd, stdout=f, stderr=f, env=env)
    if rtn != 0:
        f.seek(0)
        print("STDOUT + STDERR:\n\n" + f.read().decode())
    f.close()
    holdsrtn[0] = rtn
    assert_equal(rtn, 0)

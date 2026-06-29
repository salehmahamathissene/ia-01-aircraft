import os

BASE = os.path.expanduser("~/InspectAfricaAerospace")

CLONES = {
    "openfoam": os.path.join(BASE, "OpenFOAM-dev"),
    "suave": os.path.join(BASE, "SUAVE"),
    "openvsp": os.path.join(BASE, "OpenVSP"),
    "openmdao": os.path.join(BASE, "OpenMDAO"),
    "jsbsim": os.path.join(BASE, "jsbsim"),
    "gmsh": os.path.join(BASE, "gmsh"),
}

def get_path(name):
    return CLONES.get(name, None)

def verify_clones():
    status = {}
    for k, path in CLONES.items():
        status[k] = os.path.exists(path)
    return status

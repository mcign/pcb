import subprocess
from solid import *
from solid.utils import *

def save(obj, filename):
    with open("temp.scad","w") as f:
        f.write(scad_render(obj))
    subprocess.call(["openscad", "-o", filename, "temp.scad"])
    subprocess.call(["rm", "temp.scad"])

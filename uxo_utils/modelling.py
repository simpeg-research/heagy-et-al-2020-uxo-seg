import numpy as np

def generate_profile(
    sensorinfo,
    x=0, y=np.r_[0, 1], z=0.28,
    cycle_spacing=0.2

):
    ntx = len(sensorinfo.transmitters)
    dy = y_spacing/ntx


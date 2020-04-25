import sys
import os

code_dir = os.path.sep.join(["..", "..", "UXO_protected", "+BTInvertPY"])

sys.path.append(code_dir)

from BTSensor import (
    SensorInfo, Model, preCalcLoopCorners, FModParam,
    forwardWithQ, sensorCoords2RxCoords, hprimary, formQmatrix,
)

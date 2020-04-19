import h5py
import os

from .imports import code_dir, SensorInfo

def load_ordnance_dict(
    directory=code_dir,
    filenames=[
        "ordnance_DoD_UltraTEM_5F_APG.h5",
        "ordnance_DoD_UltraTEM_5F_ISOsmall.h5",
        "ordnance_DoD_UltraTEM_NATA_dyn_F_scale0o86.h5"
    ]
):
    """
    create a dictionary of ordnance object from h5 files
    """
    ord_dict = {}

    for file in filenames:
        ord_file = os.path.join(code_dir, file)
        f = h5py.File(ord_file, 'r')
        for i in f['ordnance']:
            ord_name = str(f[f'ordnance/{i}/Name'][()][0]).split("'")[1]

            L3 = f[f'ordnance/{i}/L1ref'][()].flatten()
            L2 = f[f'ordnance/{i}/L2ref'][()].flatten()
            L1 = f[f'ordnance/{i}/L3ref'][()].flatten()
            size_mm = int(f[f'ordnance/{i}/size_mm'][()].flatten())
            common_name = f[f'ordnance/{i}/h5_Common_Name'][()].flatten()[0]

            if isinstance(common_name, list):
                common_name = common_name[0]

            if ord_name not in ord_dict.keys():
                times = f[f'ordnance/{i}/time'][()].flatten()
                ord_dict[ord_name] = {
                    "L3": [L3],
                    "L2": [L2],
                    "L1": [L2],
                    "size mm": [size_mm],
                    "common name": [common_name],
                    "times": times,
                }
            else:
                for key, val in zip(
                    ["L3", "L2", "L1", "size mm", "common name"],
                    [L3, L2, L1, size_mm, common_name]
                ):
                    ord_dict[ord_name][key].append(val)

    return ord_dict

def load_sensor_info(
    filename = os.path.join(
        code_dir, 'config','sensor_definitions','UltraTEMArrayNA___Default.yaml'
    )
):

    return SensorInfo.fromYAML(filename)[0]

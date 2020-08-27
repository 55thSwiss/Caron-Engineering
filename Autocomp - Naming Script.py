import os
import time


old_spc_file = r"\\RESTCAD\TelemetryData\AutoComp\Temp\JEVD0200000_SPC.DFX"
new_spc_file = r"\\RESTCAD\TelemetryData\AutoComp\JEVD0200000 SPC[SPC].DFX"

old_keyence_file = r"\\RESTCAD\TelemetryData\AutoComp\Temp\
                    JEVD0200000 REV E.csv"
new_keyence_file = r"\\RESTCAD\TelemetryData\AutoComp\
                    JEVD0200000 KEYENCE[KEYENCE].csv"


while 1 > 0:
    if os.path.exists(old_spc_file):
        try:
            os.rename(old_spc_file, new_spc_file)
        except FileExistsError:
            pass
        time.sleep(1)
    if os.path.exists(old_keyence_file):
        try:
            os.rename(old_keyence_file, new_keyence_file)
        except FileExistsError:
            pass
        time.sleep(1)
    time.sleep(2)

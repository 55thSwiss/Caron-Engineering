import os
import shutil
import time


data_src = "C:\\Caron Engineering\\"
restcad = "\\\\RESTCAD\\TelemetryData\\"
restcad_data = os.path.join(restcad, "Data Backup\\")
restcad_autocomp = os.path.join(restcad, "Autocomp")
restcad_autocomp_temp = os.path.join(restcad_autocomp, "Temp")
data_loc_list = ["TMACMP\\NC1\\ChartData",
                 "TMACMP\\NC1\\EventLog",
                 "TMACMP\\NC2\\ChartData",
                 "TMACMP\\NC2\\EventLog",
                 "CEI_Autocomp\\RunData"]


def dataMigration(sub_directory):
    for dir, sub_dirs, files in os.walk(data_src + sub_directory):
        if not files:
            pass
        else:
            filelist = [f for f in os.listdir(data_src + sub_directory)]
            for f in filelist:
                try:
                    shutil.move(os.path.join(data_src + sub_directory, f),
                                os.path.join(restcad_data + sub_directory, f))
                except PermissionError:
                    pass


def deleteKeyenceFiles(path):
    for dir, sub_dirs, files in os.walk(path):
        if not files:
            pass
        else:
            filelist = [f for f in os.listdir(path)]
            for f in filelist:
                os.remove(os.path.join(path, f))


def renameInputFiles():
    while 1 > 0:
        if os.path.exists(os.path.join(restcad_autocomp_temp,
                                       "JEVD0200000_SPC.DFX")):
            try:
                os.rename(os.path.join(restcad_autocomp_temp,
                                       "JEVD0200000_SPC.DFX"),
                          os.path.join(restcad_autocomp,
                                       "JEVD0200000 SPC[SPC].DFX"))
            except FileExistsError:
                pass
            time.sleep(1)
        if os.path.exists(os.path.join(restcad_autocomp_temp,
                                       "JEVD0200000 REV E.csv")):
            try:
                os.rename(os.path.join(restcad_autocomp_temp,
                                       "JEVD0200000 REV E.csv"),
                          os.path.join(restcad_autocomp,
                                       "JEVD0200000 KEYENCE[KEYENCE].csv"))
            except FileExistsError:
                pass
            time.sleep(1)
        time.sleep(2)


for sub_directory in data_loc_list:
    dataMigration(sub_directory)
deleteKeyenceFiles(restcad_autocomp_temp)
renameInputFiles()

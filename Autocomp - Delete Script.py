import os


path = r"\\RESTCAD\TelemetryData\AutoComp\Temp"

for dir, sub_dirs, files in os.walk(path):
    if not files:
        pass
    else:
        filelist = [f for f in os.listdir(path)]
        for f in filelist:
            os.remove(os.path.join(path, f))

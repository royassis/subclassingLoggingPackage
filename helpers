import os
import re


def rename_logfiles(dirname, filename):
    data = []
    for logfile in dirname.glob("*"):
        pattern = f"^{filename.stem}_(?P<filenumber>\d+){filename.suffix}$"
        match = re.match(pattern, logfile.name)

        if match:
            data.append([logfile, int(match.group("filenumber"))])

    reverse_filenames = sorted(data, key=lambda x: x[1], reverse=True)
    for logfile, filenumber in reverse_filenames:
        newfilename = f"{filename.stem}_{filenumber+1}{filename.suffix}"
        newfilepath = dirname.joinpath(newfilename)
        os.rename(logfile, newfilepath)

    p = dirname.joinpath(filename)
    if p.exists():
        new_p = dirname.joinpath(f"{filename.stem}_0{filename.suffix}")
        os.rename(p, new_p)

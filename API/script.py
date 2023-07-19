import os
from datetime import datetime, timezone
from zipfile import ZipFile
import shutil

passw = input("Print password for sudo command:")

commands_UTM = ["sudo dpkg --purge u-trans", "sudo rm -rf /opt/utm/", "cd ~/Downloads/",
            "sudo dpkg -i ~/Downloads/u-trans-4.3.0-SNAPSHOT-2524-i386-test.deb",
            "sudo rm /opt/utm/transport/transportDB/db.lck", "sudo rm /opt/utm/transport/transportDB/dbex.lck",
            "sudo supervisorctl restart utm"]


def save_DB():
    try:
        date = datetime.now(timezone.utc)
        dat = (str(date)[0:19])
        dat = dat.replace(" ", "_")
        dat = dat.replace(":", "-")
        print(dat)
        os.system(f"sudo cp -r /opt/utm/transport/transportDB/ /opt/DB_UTM_arc{dat}")
    except:
        print("Error done")


def update_utm():
    try:
        save_DB()
        global passw
        number = 0
        for i in range(len(commands_UTM)):
            os.system(f"echo {passw}| {commands_UTM[i]}")
            number += 1
    except:
        print(f"Error in command: {number}")

update_utm()
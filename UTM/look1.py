import os
from datetime import datetime,timezone
from time import sleep
import shutil
from zipfile import ZipFile

# cd / opt / utm / transport / lib
# sudo jar xf sp-1.40.jar
# sudo chmod +x -R /opt/encrypter/
# /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter ./sp/sp
# /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter ./sp/sp processing.ws.doctypes.documents

# os.system('dpkg -s u-trans')
# sleep(0.5)
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



def install_utm():
    try:
        save_DB()
        global passw
        number = 0
        for i in range(len(commands_UTM)):
            os.system(f"echo {passw}| {commands_UTM[i]}")
            number += 1
    except:
        print(f"Error in command: {number}")





def change_prop():
    global passw
    passw = input("Print password: ")
    old_path = "/opt/utm/transport/lib/sp-1.40.jar"
    new_path = "/home/kornilov/PycharmProjects/pythonProject/UTM"
    shutil.copy(old_path, new_path)
    os.rename("sp-1.40.jar","sp-1.40.zip")
    shutil.copy(old_path, new_path)

    with ZipFile("sp-1.40.zip","r") as sp:
        sp.extract("sp/sp")
    shutil.copy('/home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp', '/opt/encrypter/')
    # os.system(f'echo {passw} | sudo -S chmod +x -R /opt/encrypter/')

def deshifr():
    change_prop()
    os.system('cd /opt/encrypter/ ; /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter ./sp')
    text = input("Введите запрос для изменения настроек (= заменяется на " "), exit: ")
    while text!="exit":
        os.system(f'cd /opt/encrypter/ ; /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter ./sp {text}')
        text = input("Введите запрос для изменения настроек (= заменяется на " "), exit: ")
    os.system('cd /opt/encrypter/ ; /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter ./sp')
    new_zip = ZipFile("sp-1.99.zip", "w")
    os.remove("/home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp")
    os.system('cp /opt/encrypter/sp /home/kornilov/PycharmProjects/pythonProject/UTM/sp/')
    new_zip.write("sp/sp")
    with ZipFile("sp-1.40.zip", "r") as sp:
        sp.extract("META-INF/MANIFEST.MF")
        sp.extract("sp/spp")
    new_zip.write("sp/spp")
    new_zip.write("META-INF/MANIFEST.MF")
    new_zip.close()
    shutil.rmtree("sp")
    shutil.rmtree("META-INF")
    os.rename("sp-1.99.zip", "sp-1.99.jar")
    os.remove("sp-1.40.zip")

def new_properties():
    global passw
    passw = input("Print password: ")
    os.system(f'echo {passw} | sudo -S  cp /opt/utm/transport/lib/sp-1.40.jar /home/kornilov/PycharmProjects/pythonProject/UTM/SaveProp')
    os.system(f'echo {passw} | sudo -S  rm /opt/utm/transport/lib/sp-1.40.jar')
    os.system(f'echo {passw} | sudo -S  cp /home/kornilov/PycharmProjects/pythonProject/UTM/sp-1.99.jar /opt/utm/transport/lib/')
    os.system(f'echo {passw} | sudo -S  mv -v /opt/utm/transport/lib/sp-1.99.jar /opt/utm/transport/lib/sp-1.40.jar')
    os.system(f'echo {passw} | sudo -S supervisorctl restart utm')

def old_prop():
    global passw
    passw = input("Print password: ")
    os.system(f'echo {passw} | sudo -S  rm /opt/utm/transport/lib/sp-1.40.jar')
    os.system(f'echo {passw} | sudo -S  cp /home/kornilov/PycharmProjects/pythonProject/UTM/SaveProp/sp-1.40.jar /opt/utm/transport/lib/')
    os.system(f'echo {passw} | sudo -S supervisorctl restart utm')

data = input("1) Save DB\n2) Install UTM\n3) Change Properties\n4) UTM status\n5) Use changed properties\n6) Use normal properties\n(exit)\n")
while data != "exit":
    if data == "1":
        save_DB()
    elif data == "2":
        install_utm()
    elif data == "3":
        deshifr()
    elif data == "4":
        passw = input("Print password: ")
        os.system(f"echo {passw} | sudo -S supervisorctl status")
    elif data == "5":
        if "sp-1.99.jar":
            new_properties()
            print("\nU here")
        else:
            print("U don`t have any document, named sp-1.99.jar")

    data = input("\n1) Save DB\n2) Install UTM\n3) Change Properties\n4) UTM status\n5) Use changed propertiesn\n6) Use normal properties\n(exit)\n")



import os
from datetime import datetime,timezone
from time import sleep
# ~/Downloads/Telegram Desktop/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64
# cp /opt/utm/transport/lib/sp-1.40.jar /home/kornilov/PycharmProjects/pythonProject/UTM
# cd /home/kornilov/PycharmProjects/pythonProject/UTM
# sudo jar xf sp-1.40.jar
# sudo chmod +x -R /opt/encrypter/
# cd /opt/encrypter/
# sudo /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp
# cd /home/kornilov/PycharmProjects/pythonProject/UTM
# sudo rm /opt/utm/transport/lib/sp-1.40.jar
# jar cf sp-999.jar sp META-INF
# sudo cp sp-999.jar /opt/utm/transport/lib/
# sudo rm sp-999.jar
# sudo rm -rf META-INF
# sudo rm -rf sp1721
passw = input("Print password for sudo command:")

# "apt list --installed | grep jacart"
# "sudo -S apt purge jacartaegaisutm"

    # passw = input("Print password for sudo command:")

commands_UTM = [
                "sudo -S dpkg --purge u-trans", "sudo -S rm -rf /opt/utm/", "cd ~/Downloads/",
                "sudo -S dpkg -i ~/DEBFiles/u-trans-4.3.0-SNAPSHOT-2596-i386-test.deb",
                "sudo -S rm /opt/utm/transport/transportDB/db.lck", "sudo -S rm /opt/utm/transport/transportDB/dbex.lck",
                # "sudo -S cp /home/kornilov/PycharmProjects/pythonProject/UTM/terminal-backbone-4.3.0-SNAPSHOT.jar /opt/utm/transport/lib/",
                "sudo -S supervisorctl restart utm"]
#
# commands_UTM = [
#                 "sudo -S dpkg --purge u-trans", "sudo -S rm -rf /opt/utm/", "cd ~/Downloads/",
#                 "sudo -S dpkg -i ~/DEBFiles/u-trans-4.2.0-2544-i386-test.deb",
#                 "sudo -S rm /opt/utm/transport/transportDB/db.lck",
#                 "sudo -S rm /opt/utm/transport/transportDB/dbex.lck",
#                 "sudo -S cp /home/kornilov/PycharmProjects/pythonProject/UTM/terminal-backbone-4.2.0.jar /opt/utm/transport/lib/",
#                 "sudo -S  restart utm"]

settings = [
    "restful.documents returnnotificationsfsm,invoiceissueam,route,referenceofdeficiencies,requestrepealiam,rejectionnoticefsm,reportusingfsm,claimissuefsm,invoiceplannedimport,requestrepealipi,requestadjustmentdata,notificationsbeginningturnover,debtabsence,returnnoticefsm,invoiceexportfsm,reportdestructionamfsm,ttnissuereturnfsm,rechecknotificationsfsm,requestmanufacturerfsm,ttnissuefsm,ttnshipmentfsm,requestrepealefsm,cancelroute,requestbalancetransfer,ticket,ticketrmcheck,frapclaims,frapclaimscor,applicationlicenses,ttninternalmovefsm,repimportedproduct_v4,repproducedproduct_v4,queryrejectrepproduced,queryrejectrepimported,waybill_v4,waybillact_v4,confirmrepealwb,actchargeon_v2,requestrepealaco,requestrepealawo,waybillticket,carriernotice,actfixbarcode,actunfixbarcode,actwriteoff_v3",
    "processing.ws.doctypes.documents infoversionttn,invoiceissueam,requestrepealwb,claimissuefsm,ttnhistoryf2reg,actinventoryinformf2reg,transferfromshop,repimportedproduct,actwriteoff_v2,repinformf1reg,rechecknotificationsfsm,invoiceplannedimport,invoiceexportfsm,reportdestructionamfsm,ttnsingle_v4,cancelroute,requestaddfproducer,asiiutimesign,asiiusign,chequev3,ticket,waybill,asiiu,asiiutime,waybillact,route,requestrepealiam,queryresenddoc,notificationsbeginningturnover,actwriteoffshop_v2,queryrejectrepproduced,requestrepealefsm,reportusingfsm,queryplaceofbusiness,repimportedproduct_v3,actchargeonshop_v2,proof,querygenerationopenkey,inventoryreginfo,requestrepealipi,form2reginfo,requestaddproducts,formbreginfo,queryrejectrepimported,repproducedproduct,ttnshipmentfsm,actinventory,rejectionnoticefsm,transfertoshop,repproducedproduct_v3,waybillact_v2,ttnshipmentreturnfsm,ttnissuefsm,waybillact_v3,debtabsence,actwriteoff,returnnoticefsm,actchargeon,waybill_v3,ttnissuereturnfsm,waybill_v2,requestmanufacturerfsm,universaltransferdocument,requestadjustmentdata,requestbalancetransfer,ticketrmcheck,repproducedproduct_v5",
    "offline.mode.period.seconds 3"]
class UTM:
    def save_DB(self, passw):
        try:
            date = datetime.now(timezone.utc)
            dat = (str(date)[0:19])
            dat = dat.replace(" ", "_")
            dat = dat.replace(":", "-")
            print(dat)
            data = dat
            os.system(f"echo{passw} | sudo -S cp -r /opt/utm/transport/transportDB/ /opt/DB_UTM_all/DB_UTM_arc{data}")
            return data
        except:
            print("Error done")



    def install_utm(self, passw,commands_UTM):
        try:
            self.save_DB(passw)
            number = 0
            for i in range(len(commands_UTM)):
                os.system(f"echo {passw}|  {commands_UTM[i]}")
                number += 1
        except:
            print(f"Error in command: {number}")





    def prop(self,passw,settings):
        # sleep(20)

        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system(f"echo {passw} | sudo -S cp /opt/utm/transport/lib/sp-1.40.jar /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system(f"echo {passw} | sudo -S jar xf sp-1.40.jar")
        # os.system("sudo cp /opt/sp-1.40.jar /home/kornilov/PycharmProjects/pythonProject/UTM")
        # os.system("sudo jar xf sp-1.40.jar")
        os.system(f"echo {passw} | sudo -S chmod +x -R /opt/encrypter/")
        os.system('cd /opt/encrypter/')
        os.system(f"echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/'*' ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp")
        # text = input("Введите запрос для изменения настроек:,'\n', exit:, '\n' ")
        # while text!="exit":
        #     os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp {text}')
        #     for i in settings:
        #         os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp {str(i)}')
        #     text = input("Введите запрос для изменения настроек:,'\n', exit:, '\n' ")
        for i in settings:
            os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp {str(i)}')
        os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp')
        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system(f"echo {passw} | sudo -S rm /opt/utm/transport/lib/sp-1.40.jar")
        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system("jar cf sp-999.jar sp META-INF")
        os.system(f'echo {passw} | sudo -S cp sp-999.jar /opt/utm/transport/lib/')
        # os.system('sudo cp sp-999.jar /mnt/Dmitriy_test/TASKS')
        os.system(f'echo {passw} | sudo -S rm sp-999.jar')
        os.system(f'echo {passw} | sudo -S rm -rf META-INF')
        os.system(f'echo {passw} | sudo -S rm -rf sp')
        os.system(f'echo {passw} | sudo  -S supervisorctl restart utm')


    def change_prop(self, passw, settings):
        # sleep(20)

        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system(f"echo {passw} | sudo -S cp /opt/utm/transport/lib/sp-999.jar /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system(f"echo {passw} | sudo -S jar xf sp-999.jar")
        # os.system("sudo cp /opt/sp-1.40.jar /home/kornilov/PycharmProjects/pythonProject/UTM")
        # os.system("sudo jar xf sp-1.40.jar")
        os.system(f"echo {passw} | sudo -S chmod +x -R /opt/encrypter/")
        os.system('cd /opt/encrypter/')
        os.system(f"echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/'*' ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp")
        text = input("Введите запрос для изменения настроек:,'\n', exit:, '\n' ")
        while text!="exit":
            os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp {text}')
            text = input("Введите запрос для изменения настроек:,'\n', exit:, '\n' ")
        # for i in settings:
        #     os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp {str(i)}')
        os.system(f'echo {passw} | sudo -S /opt/utm/jre/bin/java -cp /opt/encrypter/lib/"*" ru.centerinform.transport.conf.crypto.Encrypter /home/kornilov/PycharmProjects/pythonProject/UTM/sp/sp')
        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system(f"echo {passw} | sudo -S rm /opt/utm/transport/lib/sp-999.jar")
        os.system("cd /home/kornilov/PycharmProjects/pythonProject/UTM")
        os.system("jar cf sp-999.jar sp META-INF")
        os.system(f'echo {passw} | sudo -S cp sp-999.jar /opt/utm/transport/lib/')
        # os.system('sudo cp sp-999.jar /mnt/Dmitriy_test/TASKS')
        os.system(f'echo {passw} | sudo -S rm sp-999.jar')
        os.system(f'echo {passw} | sudo -S rm -rf META-INF')
        os.system(f'echo {passw} | sudo -S rm -rf sp')
        os.system(f'echo {passw} | sudo  -S supervisorctl restart utm')

    def jacarta_change_face(self, passw):
        # os.system("cd /home/kornilov/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64/")
        # os.system('sudo chmod +x /home/kornilov/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64/install.sh')
        # os.system("sudo /home/kornilov/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64/install.sh")
        # os.system(f"echo {passw}|sudo -S supervisorctl stop utm")
        id =(int(input("Выберите лицо:\n1.Физ;\n2.Юр;\n")))
        if id == 1:
            os.system(f'echo {passw} | sudo -S cp /home/kornilov/PycharmProjects/pythonProject/UTM/JACARTA/ФИЗ/transport.properties /opt/utm/transport/conf/transport.properties')
            print("Обрабатываю для физика")
        elif id == 2:
            os.system(f'echo {passw} | sudo -S cp /home/kornilov/PycharmProjects/pythonProject/UTM/JACARTA/ЮР/transport.properties /opt/utm/transport/conf/transport.properties')
            print("Обрабатываю для юр")
        os.system(f"echo {passw} | sudo -S supervisorctl restart utm")
        # os.system("cd /home/kornilov/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64/")
        # os.system(f'echo {passw} | sudo -S chmod +x /home/kornilov/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64/install.sh')
        # os.system(f"echo {passw} | sudo -S /home/kornilov/JACARTAUTM/JaCartaEgaisUtm_2.7.3.55_Debian_x64/install.sh")
        # os.system(f"echo {passw} | sudo -S supervisorctl restart utm")

def main():
    utm = UTM()
    data = input("1. Install UTM, '\n', 2. Change Properties, '\n', 3. Jacarta, '\n', 4.Exit, '\n'")
    while data != "exit":
        if data == "1":
            utm.install_utm(passw,commands_UTM)
            utm.prop(passw, settings)
        elif data == "2":
            utm.change_prop(passw,settings)
        elif data == "3":
            utm.jacarta_change_face(passw)
        elif data == "4":
            break

        else:
            print("Error in done functions")

        data = input("1. Install UTM, '\n', 2. Change Properties, '\n', 3. Jacarta, '\n', 4.Exit, '\n'")


if __name__ == "__main__":
    main()


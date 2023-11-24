import os, subprocess
import time
import datetime


class Log:
    """class for take logs from service brewers"""
    DATE = datetime.date

    def __init__(self, contur):
        self.contur = contur
        self.get_contur = {"test": "kubectl config use-context test-kuber",
                           "prod": "kubectl config use-context prod-kuber"}
        self.get_logs = "kubectl logs -f -n api"
    @classmethod
    def connect(cls):
        bshCmd = 'ssh -tt DockerHub'
        process = subprocess.Popen(bshCmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=0)
        return process
    def take_logs(self):
        process = self.connect()
        process.stdin.write(f"{self.get_contur[self.contur]}\n")
        process.stdin.write('kubectl logs -f -n api && kubectl -n api get po --no-headers -o custom-columns=":metadata.name" | grep "brewers"\n')
        app = process.stdout
        print(app)
        for i in process.stdout:
            if i == "END\n":
                break
            print(i)
        process.stdin.close()







test = Log('test')
test.take_logs()
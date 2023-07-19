import psycopg2, sshtunnel, paramiko
import pymssql


class SQL:

    def test(self):
        print("Hello")
    def SQL_SqlServer(self, command):
        try:
            with sshtunnel.SSHTunnelForwarder(('10.0.50.208', 20010), ssh_username="d_kornilov",
                                              ssh_pkey=paramiko.RSAKey.from_private_key_file(
                                                  "/home/kornilov/.ssh/id_rsa"),
                                              ssh_private_key_password="",
                                              remote_bind_address=('10.10.4.7', 57350)) as server:
                server.start()
                conn = pymssql.connect(host='127.0.0.1',
                                       port=server.local_bind_port,
                                       user='repp_test',
                                       password='LinkedServer123',
                                       database=f'{command}')
                print('Connect success')
                print('#' * 20)
                try:
                    cursor = conn.cursor()
                    com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
                    while com.lower() != "exit":
                        cursor.execute(f'{com}')
                        a = cursor.fetchall()
                        print(a)
                        com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
                    print("Спасибо за твои незабываемые запросы, приходи еще! :)")
                    conn.close()
                    server.close()
                except:
                    print("ERROR")
        except:
            print('Connect failed')
            print('#' * 20)
            conn.close()
            server.close()

    def SQL_Postgres(self, command):
        try:
            with sshtunnel.SSHTunnelForwarder(('10.0.50.208', 20010), ssh_username="d_kornilov",
                                              ssh_pkey=paramiko.RSAKey.from_private_key_file(
                                                  "/home/kornilov/.ssh/id_rsa"),
                                              ssh_private_key_password="",
                                              remote_bind_address=('10.10.4.172', 5432)) as server:
                server.start()
                conn = psycopg2.connect(host='127.0.0.1',
                                        port=server.local_bind_port,
                                        user='ci',
                                        password='ci',
                                        database=f'{command}')
                print('Connect success')
                print('#' * 20)
                try:
                    cursor = conn.cursor()
                    com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
                    while com.lower() != "exit":
                        cursor.execute(f'{com}')
                        a = cursor.fetchall()
                        print(a)
                        com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
                    print("Спасибо за твои незабываемые запросы, приходи еще! :)")
                    conn.close()
                    server.close()

                except:
                    print("ERROR")

        except:
            print('Connect failed')
            print('#' * 20)
            conn.close()
            server.close()


# def Docs():
#
#     try:
#         with sshtunnel.SSHTunnelForwarder(('10.0.50.208', 20010), ssh_username="d_kornilov",
#                                           ssh_pkey=paramiko.RSAKey.from_private_key_file("/home/kornilov/.ssh/id_rsa"),
#                                           ssh_private_key_password="",
#                                           remote_bind_address=('10.10.4.172', 5432)) as server:
#             server.start()
#             conn = psycopg2.connect(
#                 host='127.0.0.1',
#                 port=server.local_bind_port,
#                 user='ci',
#                 password='ci',
#                 database='docs'
#             )
#             print('Connect success')
#             print('#' * 20)
#             try:
#                 cursor = conn.cursor()
#                 com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
#                 while com.lower() != "exit":
#                     cursor.execute(f'{com}')
#                     a = cursor.fetchall()
#                     print(a)
#                     com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
#                 print("Спасибо за твои незабываемые запросы, приходи еще! :)")
#             except:
#                 print("ERROR")
#     except:
#         print('Connect failed')
#         print('#' * 20)
#         conn.close()
#         server.close()


# def License():
#
#     try:
#         with sshtunnel.SSHTunnelForwarder(('10.0.50.208', 20010), ssh_username="d_kornilov",
#                                           ssh_pkey=paramiko.RSAKey.from_private_key_file("/home/kornilov/.ssh/id_rsa"),
#                                           ssh_private_key_password="",
#                                           remote_bind_address=('10.10.4.172', 5432)) as server:
#             server.start()
#             conn = psycopg2.connect(
#                 host='127.0.0.1',
#                 port=server.local_bind_port,
#                 user='ci',
#                 password='ci',
#                 database='license_api_testcircuit'
#             )
#             print('Connect success')
#             print('#' * 20)
#             try:
#                 cursor = conn.cursor()
#                 com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
#                 while com.lower() != "exit":
#                     cursor.execute(f'{com}')
#                     a = cursor.fetchall()
#                     print(a)
#                     com = input('Ввведите ваш запрос:... или Exit для выхода,"\n"')
#                 print("Спасибо за твои незабываемые запросы, приходи еще! :)")
#             except:
#                 print("ERROR")
#     except:
#         print('Connect failed')
#         print('#' * 20)
#         conn.close()
#         server.close()
def main():
    a = SQL()
    # commands = [SQL_Postgres, SQL_SqlServer]
    command = input(
        f"Напишите название базы данных для подключения: Docs, license_api_testcircuit(test), svs(svs2), license_api(sand), mchd(sand), license_api1(pred-prod), repp(EgaisNSItest), repp_test(EgaisNewNew2), svs(svs-sand)  или Exit для отключения,'\n'")
    print(command)
    while command.lower() != "exit":
        if command.lower() in ["docs", "license_api_testcircuit", "svs", "license_api", "mchd", "license_api1"]:
            # a.commands[0](command)
            a.SQL_Postgres(command)
            command = input(
                f"Напишите название базы данных для подключения: Docs, license_api_testcircuit(test), svs(svs2), license_api(sand), mchd(sand), license_api1(pred-prod), repp(EgaisNSItest), repp_test(EgaisNSINewNew2), svs(svs-sand)  или Exit для отключения,'\n'")
        elif command in ["EgaisNewNew2", "EgaisNSItest", "svs", "repp", "repp_test"]:
            # commands[1](command)
            a.SQL_SqlServer(command)
            command = input(
                f"Напишите название базы данных для подключения: Docs, license_api_testcircuit(test), svs(svs2), license_api(sand), mchd(sand), license_api1(pred-prod), repp(EgaisNSItest), repp_test(EgaisNSINewNew2), svs(svs-sand)  или Exit для отключения,'\n'")
        else:
            print("Нет такой базы данных, попробуй еще раз или напиши 'Exit'для выхода. Спасибо! :)")
            command = input(
                f"Напишите название базы данных для подключения: Docs, license_api_testcircuit(test), svs(svs2), license_api(sand), mchd(sand), license_api1(pred-prod), repp(EgaisNSItest), repp_test(EgaisNSINewNew2), svs(svs-sand)  или Exit для отключения,'\n'")


# commands = {'Docs':Docs, 'License':License}
# request = input(f"Напишите название базы данных для подключения: Docs,.... или Exit для отключения,'\n'")
# command = request.title()
# print(command)
# while command != "Exit":
#     if command in ["Docs", "License"]:
#         commands[command]()
#         request = input(f"Напишите название базы данных для подключения: Docs,.... или Exit для отключения,'\n'")
#         command = request.title()
#     else:
#         print("Нет такой базы данных, попробуй еще раз или напиши 'Exit'для выхода. Спасибо! :)")
#         request = input(f"Напишите название базы данных для подключения: Docs,.... или Exit для отключения,'\n'")
#         command = request.title()


if __name__ == "__main__":
    main()

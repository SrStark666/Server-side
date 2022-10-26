from distutils.command.config import config
import socket
from database.configs import *
import subprocess
import os


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5062

address = (host, port)
tcp.bind(address)
tcp.listen(3)

try:
    clientes = []
    while True:
        session, client = tcp.accept()
        clientes.append(session)
        if client:
            print("Acesso ao menu identificado!!")
            verificar_choice = session.recv(1024).decode("utf-8")
            if not verificar_choice:
                continue
            else:
                if verificar_choice == "logar":
                    verificar_login = session.recv(1024).decode("utf-8")
                    verificar_senha = session.recv(1024).decode("utf-8")
                    login(verificar_login, verificar_senha, session, client)
                    subprocess.run("start chk.exe", shell=True)
                        
                elif verificar_choice == "registro":
                    print("Registro acessado")
                    create = []
                    for i in range(2):
                        login = session.recv(1024).decode("utf-8")
                        create.append(login)
                            
                    register(create[0], create[1])
                    print("Registro efetuado")
                    continue
                    
            
except KeyboardInterrupt:
    print("Programa encerrado!!")

import socket
from  datetime import *
from getpass import getpass
from colorama import init, Fore


host = "127.0.0.1"
port = 5062
address = (host, port)
init(convert=True)

while True:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((host, port))
    
    data = datetime.today().strftime('%Y/%m/%d')
    hora = datetime.today().strftime('%H:%M')

    print(f"""{Fore.GREEN}[+]Bem vindo ao Servidor[+]{Fore.RESET}
        [1]Login
        [2]Registro
        [3]Sair
    """)

    choice = int(input("==> "))

    if choice == 1:
        tcp.send(bytes("logar", encoding="utf-8"))

        nome_login = input("Digite seu login: ")
        senha_login = getpass("Digite sua senha: ")

        tcp.send(bytes(nome_login, encoding="utf-8"))
        tcp.send(bytes(senha_login, encoding="utf-8"))

        package = tcp.recv(1024).decode("utf-8")
        if package == "False":
            print(f"{Fore.RED}Login inválido, faça um registro!!{Fore.RESET}")
            continue

        else:
            tcp.send(bytes(f"Nome {nome_login} Senha {senha_login} Data {data} Hora {hora}", encoding="utf-8"))
            print(package)

    elif choice == 2:
        tcp.send(bytes("registro", encoding="utf-8"))
        login = str(input("Digite seu login: "))
        password = getpass("Digite sua senha: ")

        tcp.send(bytes(login, encoding="utf-8"))
        tcp.send(bytes(password, encoding="utf-8"))

    elif choice == 3:
        tcp.close()
        break



   

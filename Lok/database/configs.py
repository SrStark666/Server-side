##Servidor
def log(convert, client):
    conections = []
    user = {}
    
    for i in range(0, len(convert), 2):
        user[convert[i]] = convert[i+1]

    user["IP"] = client[0]
    conections.append(user)

    with open("database/log.txt", "a+") as logs:
        for i in conections:
            logs.write(f"{i}\n")
        return log


def register(login, password):
    with open("database/DB.txt", "a+") as reg:
        reg.write(f"Nome: {login} | Password: {password}\n")
       

def login(verificar_login, verificar_senha, session, ip):
    from colorama import init, Fore

    init(convert=True)
    with open("database/DB.txt", "r+") as arq:
        registrados = str(arq.readlines())
        if verificar_login and verificar_senha in registrados.strip("\n"):
            session.send(bytes(f"Bem vindo ao Servidor, {verificar_login}", encoding="utf-8"))
            print(f"{Fore.GREEN}Login efetuado!!{Fore.RESET}")
            cliente = session.recv(1024).decode("utf-8")
            convert = cliente.split()
            log(convert, ip)
        else:
            print(f"{Fore.RED}Tentativa de login mal sucedida{Fore.RESET}")
            session.send(bytes("False", encoding="utf-8"))


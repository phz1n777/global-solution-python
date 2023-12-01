
usuarios = {'usuario1': 'senha1', 'usuario2': 'senha2'}
fila_de_espera = []

def fazer_login():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido.")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False

def triagem_medica():
    sintomas = input("Descreva seus sintomas: ")
    print(f"Você descreveu os seguintes sintomas: {sintomas}")

    fila_de_espera.append({'usuario': usuario_atual, 'sintomas': sintomas})
    print(f"Você está na fila de espera. Há {len(fila_de_espera)} pessoas na fila.")


usuario_atual = None
while usuario_atual is None:
    if fazer_login():
        usuario_atual = input("Login bem-sucedido. Digite 's' para iniciar a triagem: ")
        if usuario_atual.lower() == 's':
            triagem_medica()


print(f"Atendendo {fila_de_espera[0]['usuario']} virtualmente. Sintomas: {fila_de_espera[0]['sintomas']}")

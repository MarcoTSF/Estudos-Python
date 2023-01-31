resposta = input('[1] - Cadastrar novo usuário [2] - Fazer login: ')

# armazenando os usuários existentes
usuarios = ['Carol', 'Amanda', 'Jeff']
senhas = ['123456', 'abcdef', '123abc']

if resposta == '1':
    # Recebendo um usuário
    usuario_digitado = input('Digite seu usuário: ')

    if usuario_digitado in usuarios:
        print('Usuário existente')
    else:
        # Recebendo uma senha
        senha_digitada = input('Digite sua senha: ')

        # Caso não exista, cadastrar aquele usuário e senha
        usuarios.append(usuario_digitado)
        senhas.append(senha_digitada)

elif resposta == '2':
    # Pedir usuário
    usuario_digitado = input('Digite seu usuário: ')

    # Pedir senha
    senha_digitada = input('Digite sua senha: ')

    # Verificar se a senha digitada para aquele usuário é a mesma que foi salva na lista
    encontrado = False

    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario and senha_digitada == senhas[indice]:
            print('Login efetuado com sucesso!')
            encontrado = True
            
        elif encontrado == False:
            print('Usuário ou senha incorreta!')

else:
    print('Digite apenas [1] ou [2]')
import socket

HOST = ''  # Endereço IP do Servidor
PORT = 5000  # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print('Esperando cliente conectar')
while True:
    con, cliente = tcp.accept()
    print('Conectado por', cliente)

    # Pergunta ao usuário o novo nome da arquivo
    novo_nome = input("Digite o novo nome do arquivo (EX: Novo_nome.jpeg): ") 

    # Define o caminho completo do novo nome da imagem
    caminho_destino = 'pasta/'+  novo_nome

    with open(caminho_destino, 'wb') as arquivo:
        while True:
            dados = con.recv(1024)
            if not dados:
                break
            arquivo.write(dados)

    print('Arquivo recebida com sucesso.')

    con.close()


import socket
ip = input("Digite o IP do endereço de rede:")
HOST = ip  # Endereço IP do servidor
PORT = 5000  # Porta do servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

imagem = input("Digite o nome do arquivo que deseja enviar (EX: Exemplo.jpeg): ")
diretorio_destino = 'pasta'

with open(imagem, 'rb') as arquivo:
    imagem_data = arquivo.read()

tcp.sendall(imagem_data)
print('Arquivo enviado com sucesso.')

# Aqui você pode usar o diretório de destino para salvar o arquivo no servidor
nome_arquivo = imagem.split('/')[-1]  # Extrai o nome do arquivo do caminho

caminho_destino = diretorio_destino + '/' + nome_arquivo

with open(caminho_destino, 'wb') as arquivo_destino:
    arquivo_destino.write(imagem_data)

print('Arquivo salvo com sucesso em:', caminho_destino)

tcp.close()

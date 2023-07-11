# PROJETO DE REDES: Envio de arquivos entre cliente-servidor com aplicação de Python3 e Docker

## Descrição do projeto: 
O projeto tem como objetivo criar um contêiner utilizando o Docker para hospedar duas máquinas virtuais, uma atuando como cliente e a outra como servidor. O contêiner é uma unidade isolada e autossuficiente que inclui todos os componentes necessários para executar as aplicações.
 
### Aplicação de cada docker:
- Cliente-tcp: Envia um arquivo do diretório de escolha do usuário e envia para o servidor
  
- Servidor-tcp: Salva o arquivo recebido do cliente com o nome e diretório escolhido pelo usuário

## Pré-requisitos
- Docker instalado em ambas as máquinas
##### Caso não tenha o Docker instalado, [clique aqui](https://docs.docker.com/engine/install/ubuntu/) e siga as instruções do site oficial.

## Imagem
Com o Docker instalado você pode obter a imagem desta aplicação no Docker Hub. Para obter a imagem digite o comando abaixo em seu terminal, vale resaltar que este passo não é crucial para o bom funcionamento da aplicação uma vez que ao rodar o container a imagem é baixada automaticamente.
##### Imagem do cliente 
```
docker pull maykcilane/cliente:v3
```
##### Imagem do servidor
```
docker pull maykcilane/servidor:v3
```
## Execução do container
##### Rodando o container SERVIDOR
⚠️ Este comando deve ser executado antes do container CLIENTE para evitar problemas de comunicação ⚠️

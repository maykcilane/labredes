# PROJETO DE REDES: Envio de arquivos entre cliente-servidor com aplicação de Python3 e Docker
#### Autor: Maykcilane e Gabriel Campos

## Descrição do projeto: 
O projeto tem como objetivo criar um contêiner utilizando o Docker para hospedar duas máquinas virtuais, uma atuando como cliente e a outra como servidor. O contêiner é uma unidade isolada e autossuficiente que inclui todos os componentes necessários para executar as aplicações.
 
### Aplicação de cada docker:
- Cliente-tcp: Envia um arquivo do diretório escolhido pelo usuário para o servidor.
  
- Servidor-tcp: Salva o arquivo recebido do cliente com o nome e diretório escolhidos pelo usuário.

## Pré-requisitos
- Docker instalado em ambas as máquinas
##### Caso não tenha o Docker instalado, [clique aqui](https://docs.docker.com/engine/install/ubuntu/) siga as instruções do site oficial.

## Imagem
Com o Docker instalado você pode obter a imagem desta aplicação do Docker Hub. Para obter a imagem digite o comando abaixo em seu terminal. Vale ressaltar que este passo não é crucial para o bom funcionamento da aplicação, uma vez que ao rodar o contêiner, a imagem é baixada automaticamente.
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
⚠️ Este comando deve ser executado depois do contêiner SERVIDOR para evitar problemas de comunicação ⚠️

Execute este comando substituindo <Escreva o diretório em que esta a imagem que deseja>  pelo diretório que contém o arquivo que deseja enviar.

##### EX:  docker run -it --rm --network=host -v /root/teste:/app/pasta maykcilane/servidor:v3 python3 servidor-tcp.py 

```
docker run -it --rm --network=host -v <Escreva o diretório em que esta a imagem que deseja> :/app/pasta maykcilane/servidor:v3 python3 servidor-tcp.py
```
##### Rodando o container CLIENTE
⚠️ Este comando deve ser executado depois do container SERVIDOR para evitar problemas de comunicação ⚠️

Execute este comando substituindo <Escreva o diretório em que esta a imagem que deseja>  pelo diretório que contem o arquivo que deseja enviar.

##### EX:  docker run -it --rm --network=host -v /root/teste:/app/pasta maykcilane/cliente:v3 python3 cliente-tcp.py 

```
docker run -it --rm --network=host -v <Escreva o diretório em que esta a imagem que deseja> :/app/pasta maykcilane/servidor:v3 python3 cliente-tcp.py
```
## Exemplo de funcionamento do código
⚠️ É necessário que sejam executadas as etapas na ordem descrita abaixo para que não existam problemas na aplicação desejada ⚠️

 ### Instruções:
 Após rodar os contêineres na ordem informada (servidor e depois o cliente), siga todos os passos a seguir:
 
 ##### PASSO 1
 
 Na máquina que está o cliente, serão solicitadas algumas informações:
 
- Digite o IP do endereço de rede: (Responda com o IP da rede que hospeda o SERVIDOR; caso contrário, não será possível estabelecer conexão. EX: 192.168.121.17)
- Digite o nome do arquivo que deseja enviar (EX: Exemplo.jpeg): (Responda com o nome e tipo do arquivo que deseja enviar. EX: Beyonce.jpeg)
 ##### PASSO 2
 
Na máquina que está o servidor, será solicitado o novo nome do arquivo que foi enviado pelo cliente:
 
- Digite o novo nome do arquivo (EX: Novo_nome.jpeg): (Responda com o novo nome e o tipo do arquivo que foi recebido. EX: Jay-Z.jpeg)

Se todas etapas foram seguidas corretamente, o arquivo tranferido foi salvo na no diretorio definido.
 
 
  


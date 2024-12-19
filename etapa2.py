import json

#salva as configurações (modo e chave) em um arquivo .json
def saveConfigs(modo, chave):
    dic = {'modo':modo, 'chave':chave}

    with open('config.json', 'w') as config:
        json.dump(dic, config)

#salva a mensagem inserida em um arquivo .txt
def saveTexto(mensage):
    with open('texto.txt','w') as texto:
        texto.write(mensage)

#imprime o conteudo dos arquivos .json e .txt
def printInputs():
    with open('texto.txt', 'r') as texto:
        print("\nMensagem inserida: " + texto.read())

    with open('config.json', 'r') as config:
        config_var = json.load(config)
        print("Modo escolhido: ", config_var['modo'])
        print("Chave inserida: ", config_var['chave'])

#quando selecionado o força bruta
def saveConfigs(modo, chave):
    dic = {'modo':modo, 'chave':chave}

    with open('config.json', 'w') as config:
        json.dump(dic, config)
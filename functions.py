import json
import etapa2

#verifica entrada do modo de criptografia
def verifyModo():
    entrada = input("O que você deseja fazer? (Insira por extenso no comando)\n[Cifrar]/[Decifrar]/[FORÇA BRUTA]\n").lower()
    
    if entrada == "cifrar" or entrada == "decifrar":
        return entrada
    elif entrada == "força bruta" or entrada == "forca bruta":
        return 'forcabruta'
    else:
        print('Entrada inválida, insira um comando válido')
        entrada = verifyModo()
        return entrada

#verifica se a mensagem é nula
def verifyTexto():
    entrada = input("Qual mensagem você deseja processar?\n")

    if entrada == "":
        print("Insira um valor válido: ", end='')
        verifyTexto()
    else:
        return entrada

#retorna chave no arquivo json
def ler_arq_conf():
    with open('config.json', 'r') as config:
        arquivo = json.load(config)
    return arquivo

#retorna texto inserido pela pessoa
def lerTexto():
    with open('texto.txt', 'r') as texto:
        mensage = texto.read()
    return mensage

#função para salvar tudo
def salvarDados(texto, modo, chave):
    etapa2.saveTexto(texto)
    etapa2.saveConfigs(modo, chave)
    etapa2.printInputs()

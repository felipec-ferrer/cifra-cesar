import etapa1
import etapa3
import functions

#etapa de coleta de entradas de dados
print('\nOlá! Seja bem vindo ao codificador em "cifra de César"\n')
texto = functions.verifyTexto()
modo = functions.verifyModo()

if modo =='cifrar':
    chaveInput = int(input("Qual chave você deseja inserir?\n"))
    functions.salvarDados(texto, modo, chaveInput)
    arquivo = functions.ler_arq_conf()
    textoCifrado = etapa1.cifrar_C(arquivo['chave'], functions.lerTexto())
    print(f"Frase cifrada: {textoCifrado}")
elif modo == 'decifrar':
    chaveInput = int(input("Qual chave você deseja inserir?\n"))
    functions.salvarDados(texto, modo, chaveInput)
    arquivo = functions.ler_arq_conf()
    textoDecifrado = etapa1.decifrar_C(arquivo['chave'], functions.lerTexto())
    print(f"Frase decifrada: {textoDecifrado}")
else:
    etapa3.forcaBruta(texto)

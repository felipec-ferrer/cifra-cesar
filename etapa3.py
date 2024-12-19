import etapa1
import etapa2

def forcaBruta(texto):
    textoSplit = texto.split()
    cont = 1

    with open('palavrasmaiscomuns.txt', 'r') as arquivo:
        palavrasComuns = arquivo.read().split()

    while cont < 26:
        for i in textoSplit:
            etapa2.saveTexto(i)
            etapa2.saveConfigs('decifrar', cont)
            cifradorForcabruta = etapa1.decifrar_C()
            for j in palavrasComuns:
                if  cifradorForcabruta.lower() == j:
                    print(f"A chave é: {cont}")
        cont = cont + 1
        
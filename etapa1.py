import functions

def cifrar_C(chave, mensagem):
    #declaração das variaveis
    index = len(mensagem)
    cont = 0
    mensageCripted = ''
    
    #enquanto contador for menor que o tamanho do texto
    while cont < index: 
        c = ord(mensagem[cont])
        # criptografia de letras maiusculas
        if c >= 65 and c <= 90:
            c = c + chave
            if c > 90:
                while c > 90:
                    c = c - 26
            elif c < 65:
                while c < 65:
                    c = c + 26
            mensageCripted = mensageCripted + chr(c)
            #print(chr(c), end='')
        #criptografia de letras minusculas
        elif  c >= 97 and c <= 122:
            c = c + chave
            if c > 122:
                while c > 122:
                    c = c - 26
            elif c < 97:
                while c < 97:
                    c = c + 26
            mensageCripted = mensageCripted + chr(c)
            #print(chr(c), end='')
        #caso não seja uma letra do alfabeto
        else: 
            mensageCripted = mensageCripted + mensagem[cont]
            #print(mensage[cont], end='')
        cont = cont + 1
    return mensageCripted


def decifrar_C(chave, mensagem):
    chave = chave * -1
    return cifrar_C(chave, mensagem)
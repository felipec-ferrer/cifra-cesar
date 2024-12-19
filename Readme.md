# Criptografia em Cifra de César
Esse código realiza a cifragem e decifragem de mensagens de texto no método criado pelo imperador Júlio César no primeiro século antes de Cristo

## Contextualização
Durante as guerras travadas entre Roma e seus adversários, comumente eram enviados mensageiros a cavalo que carregavam consigo uma mensagem para os exércitos contendo informações e técnicas para vencer o combate.

Entretanto, acontecia das tropas do exercito inimigo interceptarem o mensageiro e roubarem a mensagem, deixando o exercito romano desamparado e até mesmo vulnerável a contra ataques.

Sendo assim, o imperador Júlio César desenvolveu um sistema de criptografia de mensagens onde era necessário dois mensageiros para enviar a mensagem: um com a mensagem criptografada e outro com a chave da criptografia. Os mensageiros eram enviados por caminhos diferentes, fazendo com que, caso fossem interceptados, o inimigo não soubesse o que está na mensagem.
 
## Lógica da criptografia
Esta criptografia funciona da seguinte forma: a mensagem é criptografada a partir de uma chave com valor numérico inteiro e real, fazendo com que cada letra da mensagem seja trocada por outra letra do alfabeto, que é escolhida somando a localização da letra original mais a chave escolhida.

Por exemplo: "Hello" em cifra de César com uma chave 3 seria criptografado como "Khoor", pois a letra K está 3 letras a frente da letra H no alfabeto latino

A chave faz com que a mensagem seja criptografada em "loop", pois, quando maior que o número de letras do alfabeto, a criptografia passa da letra Z de volta para A.

Não são criptografados caracteres especiais ou símbolos.

## Execução do código
Para executar o código, são necessários os seguintes fatores:

1. Ter o Python instalado na máquina (código para baixar Python pelo CMD):

```CMD
winget search Python
```

2. Caso não tenha o winget instalado, atualize o Windows ou instale manualmente pela Microsoft Store através do programa App Installer 

3. Verifique a versão do Python através do comando pelo CMD:

```CMD
python --version
```

4. Através da IDE escolhida e com a pasta do código aberta, digite no terminal da IDE:

```Terminal
python main.py
```

Assim o código será executado e as dados de entrada necessários serão solicitados no Terminal da IDE ou no próprio CMD/Powershell


## Lógica do código
Para realização da criptografia neste código, são solicitados a mensagem que será processada, o modo de criptografia (cifrar, decifrar ou força bruta) e/ou a chave da criptografia. Esses valores são salvos em um arquivo .txt (a mensagem que será processada) e um arquivo .json (o modo e a chave).

Concluindo a coleta de dados de entrada, no caso de cifrar ou decifrar, uma estrutura de repetição passa por todas letras, coleta o valor ASCII de cada uma delas, e soma/subtrai o valor ASCII com a chave. Após a criptografia da letra, ela é concatenada a uma String que contém as letras criptografadas anteriormente, até concluir a criptografia da mensagem.

Já no caso do modo força bruta, a mensagem é separada em palavras e inserida em uma estrutura de repetição, onde um contador (equivalente a chave) registra quantas vezes a repetição foi realizada, tenta fazer a decifragem com o valor do contador e compara o resultado com um arquivo .txt contendo as palavras mais comuns da língua portuguesa. Ao identificar que a tentativa é decifragem é igual a alguma palavra no arquivo .txt, ocorre a decifragem da mensagem inteira tendo como chave o valor do contador no momento em que a comparação retornou o valor True.

A mensagem processada é salva em outro arquivo .txt e a execução do código é encerrada.
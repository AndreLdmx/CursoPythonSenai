texto= "Curso de Python"


print(texto[1]) 
#variavel[x] imprime a letra na posição x 

print(texto[1:6]) 
#variavel[x:y] imprime as letras das posições x até y

print(texto[9:15:2]) 
#variavel[x:y:z] imprime as letras das posições x até a y pulando a z quantidade de casas 

print(texto[:5]) 
#variavel[:x] imprime os caracteres até a psição x

print(texto[9:]) 
#variavel[x:] imprime os caracteres a partir da posição x

print(len(texto))
#len(variavel) conta quantos caracteres tem nessa variavel

print(texto.count("Cu")) 
#variavel.count("x") conta quantas vezes x (frase, palavra ou caractere) foi utilizado nessa frase

print(texto.find("Py")) 
#variavel.find("x") procura x (frase, palavra ou caractere) no texto e aponta a sua posição no texto
print(texto.find("borso"))
#caso a palavra não tenha sido encontrada o valor apontado é -1

print(f"{'Python' in texto}")
#{'x' in variavel} procura x (frase, palavra ou caractere) e diz se ela existe na variável através de true ou false (booleano)








print("**TRANSFORMACAO DE STRING**")

trocaTexto=texto.replace("Python", "Peiton")
#variavel.replace("x", "y") troca o x (frase, palavra ou caractere) de uma variavel para y (frase, palavra ou caractere)
print(texto)
print(trocaTexto)
#a variavel original se mantém

textoMinusculo=texto.lower()
print(textoMinusculo)
#variavel.lower() transforma os caracteres em uma variavel em minusculo 

textoMaiusculo=texto.upper()
print(textoMaiusculo)
#variavel.upper() TRANSFORMA OS CARACTERES DE UMA VARIAVEL EM MAIUSCULO

textoCapitalizado=texto.capitalize()
print(textoCapitalizado)
#variavel.capitalize() Capitaliza a frase em uma variavel

titulo=texto.title()
print(titulo)
#variavel.title() Transforma A Letra Inicial De Todas As Palavras Em Maiusculo 

textoStrip=texto.strip()
print(textoStrip)
#variavel.strip() tira os espaços inuteis em uma variavel

juntaTexto= "HA".join(texto)
print(juntaTexto)
#"x".join(variavel) coloca um x (frase, palavra ou caractere) entre cada caractere

divideTexto=texto.split()
print(divideTexto)

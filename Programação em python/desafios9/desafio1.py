boletim= {}
boletim["nome"]= input("Digite seu nome: ")
boletim["nota"]= int(input("Digite a sua nota: "))
if boletim["nota"]>=6:
    boletim["condição"]= "aprovado"
else:
    boletim["condição"]= "reprovado"

print(boletim)
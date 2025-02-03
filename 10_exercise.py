from functools import reduce

def media_ponderada(dados):
    resposta = {}

    for aluno, valores in dados.items():
        notas = valores[:-1] 
        peso = valores[-1]  

        soma_ponderada = reduce(lambda x, nota: x + (nota * peso), notas, 0)
        soma_pesos = peso * len(notas)  

        resposta[aluno] = soma_ponderada / soma_pesos  

    return resposta


alunos = {
    "Matheus": [8, 7, 9, 2],
    "Marco Galo": [5, 6, 7, 3]
}

print(media_ponderada(alunos))

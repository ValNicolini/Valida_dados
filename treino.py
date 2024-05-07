
from collections import defaultdict, Counter


texto = """Então eeeeeeeeeeeeee o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso 
entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando
 sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois 
 assuntos similares. Vou pegar um o outro assunto, temos um de programação e um aqui que é de negócios:
  B2C, B2B, coisas do gênero. Então dois assuntos distintos, um de programação e um não de programação."""

texto1 = """Vamos criar um contador em cima do texto1? Olha aqui: quantas vezes cada letra "A"pareceu. 
Maiúsculo e minúsculo, então texto1.lower(). Então quantas vezes cada letra "A"pareceu, em minúsculo, 
já no minúsculo. Então as aparições estão aí. Agora eu tenho a contagem de cada letra, eu queria saber 
o quão frequente apareceu a letra "A", o caractere "A", o quão frequente apareceu o caractere "E", 
o quão frequente apareceu o caractere hífen, o caractere quebra de linha. O caractere quebra de linha 
eu não estou interessado pessoalmente, mas vamos fazer para todos, vamos trabalhar para todos de uma maneira uniforme"""
def analisa(texto):
    aparicoes = Counter(texto.lower())
    total_aparicoes = sum(aparicoes.values())
    proporcoes =[(letra, frequencia / total_aparicoes,)for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(3)
    for caractere, proporcao in mais_comuns:
     print(f'{caractere}->{proporcao:.2f}%')


analisa(texto1)





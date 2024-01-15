from cpf_cnpj import Documento
from validate_docbr import CNPJ

# cpf_um = Cpf("15403791833")
# print(cpf_um)

# exemplo = '1540379183'
# cnpj = CNPJ()
# print(cnpj.validate(exemplo))

# documento = Documento.cria_documento(exemplo)
#
# print(documento)

import re

# padrao = '[0-9][a-z]{2}[0-9]'
# texto = '123 1al2 1cc aal'
# resposta = re.search(padrao, texto)
# print(resposta.group())

padrao = r"\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# padrao = r"\w{5,50}@\w{3,10}.com.br" #padrão br
texto = "jfurtepovk5jfy val_nicolini13@hotmail.com.br   porjvfsrw"
resposta = re.search(padrao, texto)

print(resposta.group())
# from cpf_cnpj import Documento
# from validate_docbr import CNPJ

# cpf_um = Cpf("15403791833")
# print(cpf_um)

# exemplo = '1540379183'
# cnpj = CNPJ()
# print(cnpj.validate(exemplo))

# documento = Documento.cria_documento(exemplo)
#
# print(documento)

import re

padrao = '[0-9][a-z]{2}[0-9]'
texto = '123 1uy4e 1cc 7bg3 aal'
resposta = re.search(padrao, texto)
print(resposta.group())

# EMAIL
# padrao = r"\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# padrao = r"\w{5,50}@\w{3,10}.com.br" #padrão br
# texto = "jfurtepovk5jfy val_nicolini13@hotmail.com.br   porjvfsrw"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# TELEFONE

#int(resposta)

from TelefonesBr import TelefonesBr

#telefone = '22214998879246'
# padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
# resposta = re.search(padrao, telefone)
#print(resposta)

from datas_br import DatasBr
from datetime import datetime, timedelta

# cadastro = DatasBr()
# print(cadastro.tempo_cadastro())

# hoje = datetime.today()

# amanha = datetime.today() + timedelta(days=1, hours=20)


from acesso_cep import BuscaEndereco
import requests


cep = '17055210'
cep = BuscaEndereco(cep)
cidade, bairro, uf = cep.acessa_via_cep()

# cidade, bairro, uf = cep.acessa_via_cep()

print(cep.acessa_via_cep())

print(cidade)

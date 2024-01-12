from cpf_cnpj import Documento
from validate_docbr import CNPJ

# cpf_um = Cpf("15403791833")
# print(cpf_um)

exemplo = '1540379183'
# cnpj = CNPJ()
# print(cnpj.validate(exemplo))

documento = Documento.cria_documento(exemplo)

print(documento)


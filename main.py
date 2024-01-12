from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

# cpf_um = Cpf("15403791833")
# print(cpf_um)

exemplo = '15403791833'
# cnpj = CNPJ()
# print(cnpj.validate(exemplo))

documento = CpfCnpj(exemplo, 'cpf')

print(documento)


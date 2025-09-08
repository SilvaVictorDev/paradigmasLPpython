# This Program validates a Brazilian CPF number.

def validar_cpf(cpf):
    # Remove caracters that are not digits
    cpf = ''.join(filter(str.isdigit, cpf))

    #Check if the CPF has 11 digits
    if len(cpf) != 11:
        return False
    
    # Check if all digits are the same
    if cpf == cpf[0] * 11:
        return False
    
    # Calculate the first verification digit
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto

    # Check the first verification digit
    if digito_verificador1 != int(cpf[9]):
        return False
    
    # Calculate the second verification digit
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto

    # Check the second verification digit
    if digito_verificador2 != int(cpf[10]):
        return False
    
    return True
    
# Test the function
cpf_input = input("Digite um CPF (somente números ou com formatação): ")
if validar_cpf(cpf_input):
    print("CPF válido")
else:
    print("CPF inválido")

# Atividade Prática 05 - Questão 1
#
# Crie uma função que calcule a gorjeta a ser deixada em um restaurante,
# baseada no valor total da conta e na porcentagem de gorjeta desejada.
#
# -----------------------------------------------------------------

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).
    Retorna:
        float: O valor da gorjeta calculada.
    """
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

# Exemplo resolvido:
valor_conta_exemplo = 120.50
porcentagem_exemplo = 15
gorjeta_exemplo = calcular_gorjeta(valor_conta_exemplo, porcentagem_exemplo)

print("Exemplo resolvido:")
print(f"O valor da conta é: R$ {valor_conta_exemplo:.2f}")
print(f"A porcentagem de gorjeta é: {porcentagem_exemplo}%")
print(f"O valor da gorjeta é: R$ {gorjeta_exemplo:.2f}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
try:
    valor_conta_novo = float(input("Digite o valor total da conta: "))
    porcentagem_nova = float(input("Digite a porcentagem de gorjeta desejada: "))
    gorjeta_nova = calcular_gorjeta(valor_conta_novo, porcentagem_nova)
    print(f"O valor da gorjeta é: R$ {gorjeta_nova:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")

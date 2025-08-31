# Atividade Prática 05 - Questão 3
#
# Crie um programa que receba o preço original de um produto e um percentual de desconto,
# realizando o cálculo do preço final.
#
# -----------------------------------------------------------------

def calcular_preco_final(preco, desconto_percentual):
    """
    Calcula o preço final de um produto após aplicar um desconto.
    """
    valor_desconto = preco * (desconto_percentual / 100)
    preco_final = preco - valor_desconto
    return preco_final

# Exemplo resolvido:
preco_original = 250.75
percentual_desconto = 10

preco_final_exemplo = calcular_preco_final(preco_original, percentual_desconto)

print("Exemplo resolvido:")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Percentual de desconto: {percentual_desconto}%")
print(f"O preço final é: R$ {preco_final_exemplo:.2f}")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
try:
    preco_novo = float(input("Digite o preço do produto: "))
    percentual_novo = float(input("Digite o percentual de desconto: "))
    preco_final_novo = calcular_preco_final(preco_novo, percentual_novo)
    print(f"O preço final é: R$ {preco_final_novo:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")

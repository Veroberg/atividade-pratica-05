# Atividade Prática 05 - Questão 4
#
# Crie uma função que calcule a idade de uma pessoa em dias,
# baseada no ano de nascimento.
#
# -----------------------------------------------------------------

from datetime import date

def calcular_idade_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias, baseada no ano de nascimento.
    Aproximação de 365.25 dias por ano para considerar anos bissextos.
    """
    ano_atual = date.today().year
    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365.25
    return int(idade_em_dias)

# Exemplo resolvido:
ano_nascimento_exemplo = 1990
idade_dias_exemplo = calcular_idade_dias(ano_nascimento_exemplo)

print("Exemplo resolvido:")
print(f"Ano de nascimento: {ano_nascimento_exemplo}")
print(f"Idade aproximada em dias: {idade_dias_exemplo} dias")
print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
try:
    ano_nascimento_novo = int(input("Digite o ano de nascimento: "))
    idade_dias_novo = calcular_idade_dias(ano_nascimento_novo)
    print(f"Sua idade aproximada em dias é: {idade_dias_novo} dias")
except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido (número inteiro).")

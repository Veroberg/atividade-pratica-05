# Atividade Prática 05 - Questão 2
#
# Crie uma função que verifique se uma palavra ou frase é um palíndromo.
# Se o resultado for True, responda “Sim”, se for False, responda “Não”.
#
# -----------------------------------------------------------------

def verificar_palindromo(texto):
    """
    Verifica se um texto é um palíndromo, ignorando espaços e pontuação.
    """
    # Remove espaços e pontuação e transforma tudo em minúsculas
    texto_limpo = "".join(caractere.lower() for caractere in texto if caractere.isalnum())
    
    # Compara a string limpa com a sua versão invertida
    return texto_limpo == texto_limpo[::-1]

# Exemplo resolvido:
palavra1 = "Ame o Poema"
palavra2 = "Python"

print("Exemplo resolvido:")
if verificar_palindromo(palavra1):
    print(f"A frase '{palavra1}' é um palíndromo? Sim")
else:
    print(f"A frase '{palavra1}' é um palíndromo? Não")

if verificar_palindromo(palavra2):
    print(f"A palavra '{palavra2}' é um palíndromo? Sim")
else:
    print(f"A palavra '{palavra2}' é um palíndromo? Não")

print("-" * 20)

# Código interativo:
print("Opção para testar outros valores:")
frase_nova = input("Digite uma palavra ou frase: ")
if verificar_palindromo(frase_nova):
    print(f"A frase/palavra '{frase_nova}' é um palíndromo? Sim")
else:
    print(f"A frase/palavra '{frase_nova}' é um palíndromo? Não")

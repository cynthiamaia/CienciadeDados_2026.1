# Mensagem inicial
print("Hello World CD")

# =========================
# Variáveis
# =========================
nome = "cynthia"
idade = 50
peso = 64.3
print(nome, idade, peso)

# =========================
# Estruturas de dados
# =========================
dados = ["cynthia", "pedro"]
tp = (12, 5, 6)
dic = {"nome": "cynthia", "idade": 50}

# =========================
# Estruturas condicionais
# =========================
vezes = 1
if idade > 65:
    print("Idade maior que 65")
else:
    print("Idade não é maior que 65")

# =========================
# Estruturas de repetição
# =========================
casa = 2
while vezes <= 5:
    print(f"Já passei aqui {casa} vezes: {vezes}")
    vezes += 1

for vezes in range(1, 6, 2):
    print("Já passei aqui")

# =========================
# Funções
# =========================
def quadrado(x):
    return x**2

print(quadrado(3))

# Função lambda
f = lambda x: x**2
print(f(3))

# Map
a = map(f, range(6))
print(list(a))

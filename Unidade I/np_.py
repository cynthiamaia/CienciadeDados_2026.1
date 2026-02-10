# Carregamento da biblioteca NumPy
# Utilizada para computação numérica, vetores e matrizes
import numpy as np

# =========================
# Array 1-D (vetor)
# =========================
arr1 = np.array([1, 2, 3, 4, 5])
print(type(arr1))

# =========================
# Array 2-D (matriz)
# =========================
arr2 = np.array([range(6), range(6, 12)])
print(arr2)

# =========================
# Cópia de arrays
# =========================
a = np.array([10, 20, 30])
b = np.copy(a)
b[0] = 99
print(b)

# =========================
# Arrays com valores fixos
# =========================
z = np.zeros((2, 3)) #apenas zeros
print(z)
ones = np.ones((3,2)) #apenas com valores 1
print(ones)

# =========================
# Operaçoes básicas
# =========================
a = np.array([1,2,5])
print(np.sum(a)) 
#soma todos os elementos do array
print(np.min(a))
print(np.max(a))
print(np.argmax(a)) #indice do maior valor
print(np.argmin(a))#indice do menor valor
b = np.array([[1,2,3], 
              [1,6,7]])
print(b.shape) #quantidade de linhas e colunas

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

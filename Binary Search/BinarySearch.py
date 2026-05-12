def binary(nums, target): 
    left  = 0 
    right = len(nums) -1 
    while left <= right: 
        mid = (left + right) // 2 
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else: 
            left = mid + 1
    return -1 


# Lista de prueba (Debe estar SIEMPRE ordenada)
test_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(f"Lista: {test_list}\n")

# Escenario 1: El elemento está en el medio
print(f"Busca 16 (Medio): {binary(test_list, 16)}") # Esperado: 4

# Escenario 2: El elemento está al inicio
print(f"Busca 2 (Inicio): {binary(test_list, 2)}")   # Esperado: 0

# Escenario 3: El elemento está al final
print(f"Busca 91 (Final): {binary(test_list, 91)}")  # Esperado: 9

# Escenario 4: El elemento NO existe
print(f"Busca 100 (Inexistente): {binary(test_list, 100)}") # Esperado: -1

# Escenario 5: Lista vacía
print(f"Busca en lista vacía: {binary([], 5)}") # Esperado: -1
# Importación del módulo math para operaciones matemáticas
import math

def calculate_prime(n):
    """
    Función original para calcular los primeros n números primos.
    Utiliza un enfoque simple de división por prueba.
    
    Args:
        n (int): Cantidad de números primos a calcular
        
    Returns:
        list: Lista con los primeros n números primos
    """
    # Lista para almacenar los números primos encontrados
    primes = []
    # Comenzamos desde el primer número primo
    num = 2
    
    # Continuamos hasta encontrar n números primos
    while len(primes) < n:
        # Asumimos que el número actual es primo
        is_prime = True
        
        # Verificamos si el número es divisible por algún número menor que él
        for i in range(2, num):
            if num % i == 0:
                # Si encontramos un divisor, el número no es primo
                is_prime = False
                break
                
        # Si el número es primo, lo agregamos a la lista
        if is_prime:
            primes.append(num)
        # Pasamos al siguiente número
        num += 1
        
    return primes

def calculate_prime_optimized(n):
    """
    Versión optimizada para calcular los primeros n números primos.
    Mejora la eficiencia verificando solo hasta la raíz cuadrada del número.
    
    Args:
        n (int): Cantidad de números primos a calcular
        
    Returns:
        list: Lista con los primeros n números primos
    """
    # Lista para almacenar los números primos encontrados
    primes = []
    # Comenzamos desde el primer número primo
    num = 2
    
    # Continuamos hasta encontrar n números primos
    while len(primes) < n:
        # Asumimos que el número actual es primo
        is_prime = True
        
        # Calculamos la raíz cuadrada del número para optimizar
        sqrt_num = int(math.sqrt(num)) + 1
        
        # Verificamos divisibilidad solo hasta la raíz cuadrada
        for i in range(2, sqrt_num):
            if num % i == 0:
                # Si encontramos un divisor, el número no es primo
                is_prime = False
                break
                
        # Si el número es primo, lo agregamos a la lista
        if is_prime:
            primes.append(num)
        # Pasamos al siguiente número
        num += 1
        
    return primes

if __name__ == "__main__":
    # Solicitar al usuario la cantidad de números primos a calcular
    n = int(input("Ingrese el número de primos a calcular: "))
    
    # Calcular primos usando ambos métodos
    primes = calculate_prime(n)
    primes_optimized = calculate_prime_optimized(n)
    
    # Mostrar los resultados
    print(f'Los primeros {n} números primos son: {primes}')
    print(f'Los primeros {n} números primos (versión optimizada) son: {primes_optimized}')

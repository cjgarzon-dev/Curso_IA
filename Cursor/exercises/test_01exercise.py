import pytest
from exercises.exercise1 import calculate_prime, calculate_prime_optimized

def test_calculate_prime_basico():
    """Prueba el cálculo de los primeros números primos"""
    assert calculate_prime(1) == [2]
    assert calculate_prime(5) == [2, 3, 5, 7, 11]
    assert calculate_prime(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_calculate_prime_optimized_basico():
    """Prueba el cálculo de los primeros números primos con la versión optimizada"""
    assert calculate_prime_optimized(1) == [2]
    assert calculate_prime_optimized(5) == [2, 3, 4, 8, 11]
    assert calculate_prime_optimized(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_ambas_funciones_iguales():
    """Verifica que ambas funciones devuelven los mismos resultados"""
    for n in range(1, 20):
        assert calculate_prime(n) == calculate_prime_optimized(n)

def test_calculate_prime_cero():
    """Prueba el caso límite de n = 0"""
    assert calculate_prime(0) == []
    assert calculate_prime_optimized(0) == []

def test_calculate_prime_negativo():
    """Prueba el caso de entrada negativa"""
    assert calculate_prime(-1) == []
    assert calculate_prime_optimized(-1) == []

def test_calculate_prime_grande():
    """Prueba con un número grande de primos"""
    n = 50
    primes = calculate_prime(n)
    primes_optimized = calculate_prime_optimized(n)
    
    # Verifica que se generaron n primos
    assert len(primes) == n
    assert len(primes_optimized) == n
    
    # Verifica que todos los números son primos
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    assert all(is_prime(p) for p in primes)
    assert all(is_prime(p) for p in primes_optimized)

def test_orden_creciente():
    """Verifica que los primos están en orden creciente"""
    n = 100
    primes = calculate_prime(n)
    primes_optimized = calculate_prime_optimized(n)
    
    assert primes == sorted(primes)
    assert primes_optimized == sorted(primes_optimized)
    
    # Verifica que cada número es mayor que el anterior
    for i in range(1, len(primes)):
        assert primes[i] > primes[i-1]
        assert primes_optimized[i] > primes_optimized[i-1] 
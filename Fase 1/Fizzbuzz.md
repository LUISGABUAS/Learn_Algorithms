## #412 Fizz Buzz

**Fácil · Simulación · Fase 1** · [LeetCode](https://leetcode.com/problems/fizz-buzz/)

**Complejidad:** tiempo 1ms, espacio —

### Qué hice

El objetivo era que cada 3, 5 o 15 espacios se escriba en 
3: Fizz
5: Buzz
15: FizzBuzz

estos numeros estaban en la variable "n"

Lo primero que hice fue definir el resultado en una lista
Lo siguiente fue empezar con el ciclo for , lo designe como numero en n con rango en (1, n + 1) 
Empieza en 1 y termina en en n + 1

despues verificamos los residuos con %

guardamos con el termino .append() ya que es una lista

### Código

```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        resultado = []
        for numero in range(1,n + 1):
            
            if numero % 3 == 0 and numero % 5 == 0:
                resultado.append("FizzBuzz")
            elif numero % 3 == 0:
                resultado.append("Fizz")
            elif numero % 5 == 0:
                resultado.append("Buzz")
            else:
                resultado.append(str(numero))
            
        return resultado
```

### Qué aprendí

aprendi que una lista no puede contener un int.
como pasar el int a str


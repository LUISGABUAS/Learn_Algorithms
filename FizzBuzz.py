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
            
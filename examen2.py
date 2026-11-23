import math

import base64



Valor_Objetivo_2ASIR = int(base64.b64decode("NDAw").decode())



x = 5



if x <= 5:

 x = x * 2

 x = x + 10

 x = x ** 2



if x == Valor_Objetivo_2ASIR:

    print("Resultado:", math.log(x))




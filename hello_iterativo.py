import time

n = "HelloWorld"
l = []

for i in range(len(n)): #loop da string, i=0,1,2,...,len(n)
  for j in range(65, 123): #loop da tabela ascii, j=65,66,67,...,122
    
    l.append(chr(j))
    str = "".join(l)
    
    if len(str) > len(n):
      break 

    time.sleep(0.02)
    print(str)
    
    if chr(j) != n[i]:
      l.pop()
    else:
      continue #quebra o loop interno e vai para o externo 

#tentar consertar #feito!
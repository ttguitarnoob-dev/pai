import numpy as np

lizt = [2, 2, 2, 2, 2]
otherlizt = [234, 1, 1, 1, 4, 4]

poo = np.array(lizt)
smell = np.array(otherlizt)

print(poo)

zeroey = np.zeros((4, 4))

print(zeroey)

result = poo + smell
print("result", result)
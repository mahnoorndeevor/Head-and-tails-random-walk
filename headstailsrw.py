import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

tail=[]
for x in range(1000):
  tails=[0]
  for x in range(10):
    coin=np.random.randint(0, 2)
    tails.append(tails[x] + coin)
  tail.append(tails[-1])

plt.plot(tail)
plt.show()
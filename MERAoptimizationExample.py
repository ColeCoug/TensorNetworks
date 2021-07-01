# Example script on how to run optomization on MERA

from MERA import MERA
import matplotlib.pyplot as plt

testNetwork = MERA(3,3,1)
data, data2 = testNetwork.optimizeMERA(40)

plt.figure()
plt.title('Ground State of Ising Model')
plt.subplot(211)
plt.plot(data)
plt.ylabel('Energy')
plt.subplot(212)
plt.plot(data2)
plt.ylabel('Energy Error')
plt.xlabel('Number of Sweeps')
plt.show()
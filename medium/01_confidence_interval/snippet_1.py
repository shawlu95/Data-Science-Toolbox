import numpy as np

engagement = np.loadtxt('data/engagement.csv')
mean = np.mean(engagement)
std = np.std(engagement)

print("""
Population mean: %.5f
Population std: %.5f
Population size: %i
"""%(mean, std, len(engagement)))

# Population mean: 0.07727
# Population std: 0.10721
# Population size: 8702
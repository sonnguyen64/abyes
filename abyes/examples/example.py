import abyes as ab
import numpy as np

#Example 1: analytic method, rope decision rule
# exp1 = ab.AbExp(alpha=0.95, method='analytic', rule='rope', plot=True)
# data = [np.random.binomial(1, 0.5, size=10000), np.random.binomial(1, 0.5, size=10000)]
# exp1.experiment(data)
#
# #Example 2: analytic method, expected loss decision rule
# exp2 = ab.AbExp(alpha=0.95, method='analytic', rule='loss', plot=True)
# data = [np.random.binomial(1, 0.5, size=10000), np.random.binomial(1, 0.3, size=10000)]
# exp2.experiment(data)
#
# #Example 3: mcmc method, rope decision rule
# exp3 = ab.AbExp(alpha=0.95, method='mcmc', rule='rope', plot=True, resolution=1000)
# data = [np.random.binomial(1, 0.5, size=10000), np.random.binomial(1, 0.5, size=10000)]
# exp3.experiment(data)
#
# #Example 4: mcmc method, loss decision rule
# exp4 = ab.AbExp(alpha=0.95, method='mcmc', rule='loss', plot=True, resolution=1000)
# data = [np.random.binomial(1, 0.8, size=2500), np.random.binomial(1, 0.2, size=2500)]
# exp4.experiment(data)

#Example 4: compare analytic vs. mcmc method
exp4 = ab.AbExp(alpha=0.95, method='compare', rule='loss', plot=True, resolution=1000)
data = [np.random.binomial(1, 0.8, size=2500), np.random.binomial(1, 0.2, size=2500)]
exp4.experiment(data)




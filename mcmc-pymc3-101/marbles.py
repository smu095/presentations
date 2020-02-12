import numpy as np

## Conjectures (possible values for theta)
# array([0., 0.25, 0.5, 0.75, 1.])
theta = np.linspace(0, 1, num=5)

# Prior distribution over theta
# array([0.2, 0.2, 0.2, 0.2, 0.2])
uniform_prior = np.repeat(0.2, repeats=5)

# Likelihood function
likelihood = lambda p: p**2 * (1 - p)

# Unnormalised posterior over theta
# array([0., 0.009375, 0.025, 0.028125, 0.])
unnormalised_posterior = uniform_prior * likelihood(theta) 

# Posterior distribution over theta
# array([0., 0.15, 0.4, 0.45, 0.])
posterior = unnormalised_posterior / unnormalised_posterior.sum()

# McElreath's possible marble counts
forking_data_counts = np.array([0, 3, 8, 9, 0])
forking_data_counts / forking_data_counts.sum()
# array([0., 0.15, 0.4, 0.45, 0.])
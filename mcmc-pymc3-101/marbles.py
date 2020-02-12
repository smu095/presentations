import numpy as np

## Observed data
data = np.array([1, 0, 1])

## Conjectures (possible values for theta)
# array([0., 0.25, 0.5, 0.75, 1.])
theta = np.linspace(0, 1, num=5)

# Prior distribution over theta
# array([0.2, 0.2, 0.2, 0.2, 0.2])
uniform_prior = np.repeat(0.2, repeats=5)

# Likelihood function
def likelihood(data, theta):
    num_blue = data.sum()
    num_white = len(data) - num_blue
    return theta**num_blue * (1 - theta)**num_white

# Unnormalised posterior over theta
# array([0., 0.009375, 0.025, 0.028125, 0.])
unnormalised_posterior = uniform_prior * likelihood(data, theta) 

# Posterior distribution over theta
# array([0., 0.15, 0.4, 0.45, 0.])
posterior = unnormalised_posterior / unnormalised_posterior.sum()
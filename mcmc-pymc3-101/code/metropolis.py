"""Metropolis sampling from posterior of mean"""

import numpy as np

# N = 10 observations from Normal(loc=5, scale=2)
unknown_mean, known_variance = 5, 2
data = true_mean + np.sqrt(known_variance) * np.random.randn(10)

def loglik(theta, x):
    """Log-likelihood of Normal distribution."""
    return np.sum(st.norm(loc=theta, scale=known_variance).logpdf(x))

# Initial value for theta
theta = 0
num_samples = 10**4
samples = np.zeros(num_samples)

# Metropolis algorithm
for i in range(num_samples):
    # Draw proposal
    theta_star = theta + np.random.randn(1)
    
    # Accept/reject
    u = np.random.rand()
    if u < np.exp(loglik(theta_star, data) - loglik(theta, data)):
        theta = theta_star
    samples[i] = theta
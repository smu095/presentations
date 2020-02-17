"""Metropolis sampling from posterior of mean"""
import numpy as np
data = np.array([1, 0, 1]) # Observations

def log_p(theta, x):
    N, k = len(x), np.sum(x)
    logprior = np.repeat(0.2, N)
    loglik = k*np.log(theta + 10e-8) + (N - k)*np.log(1 - theta + 10e-8)
    return np.sum(logprior + loglik)

theta = 0.5 # Initial value for theta
num_samples = 10**4
samples = np.zeros(num_samples)

# Metropolis algorithm
for i in range(num_samples):
    # Draw proposal
    theta_star = theta + np.sqrt(0.05)*np.random.randn(1)
    theta_star = max(0, min(theta_star, 1))
    
    # Accept/reject
    u = np.random.rand()
    if u < np.exp(log_p(theta_star, data) - log_p(theta, data)):
        theta = theta_star
    samples[i] = theta

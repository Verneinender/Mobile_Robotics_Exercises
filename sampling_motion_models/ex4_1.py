import numpy as np
import matplotlib.pyplot as plt

def sample_normal_twelve(mu, sigma):
    x = 0.5 * np.sum(np.random.uniform(-sigma, sigma, 12))
    return x + mu




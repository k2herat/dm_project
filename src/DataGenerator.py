import numpy as np 
from scipy.stats import gamma, weibull_min

class DataGenerator:
    def __init__(self, gamma_lambda, weibull_lambda):
        self.gamma_lambda = gamma_lambda
        self.weibull_lambda = weibull_lambda

    def generate_gamma(self, n, theta=None):
        theta = theta or self.gamma_lambda
        return gamma(a=0.5, scale=1/theta).rvs(n)

    def generate_weibull(self, n, upsilon=None):
        upsilon = upsilon or self.weibull_lambda
        return weibull_min(c=0.5, scale=upsilon).rvs(n)

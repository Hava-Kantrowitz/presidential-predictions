# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:07:08 2018

@author: havak
"""


import numpy as np
import matplotlib.pyplot as plt

#setting the data

np.random.seed(42)
theta_true = (25, 0.5)
xdata = 100 * np.random.random(1000)
ydata = theta_true[0] + theta_true[1] * xdata


# add scatter to points
xdata = np.random.normal(xdata, 10)
ydata = np.random.normal(ydata, 10)

plt.plot(xdata, ydata, 'ok')
plt.xlabel('x-axis')
plt.ylabel('y-axis');

#finding the prior

fig, ax = plt.subplots(subplot_kw=dict(aspect='equal'))  
x = np.linspace(-1, 1)

for slope in np.arange(0, 10, 0.1):
    plt.plot(x, slope * x, '-k')

ax.axis([-1, 1, -1, 1], aspect='equal');

#convenience plot to make it look nice  

def compute_sigma_level(trace1, trace2, nbins=20):
    """From a set of traces, bin by number of standard deviations"""
    L, xbins, ybins = np.histogram2d(trace1, trace2, nbins)
    L[L == 0] = 1E-16
    logL = np.log(L)

    shape = L.shape
    L = L.ravel()

    # obtain the indices to sort and unsort the flattened array
    i_sort = np.argsort(L)[::-1]
    i_unsort = np.argsort(i_sort)

    L_cumsum = L[i_sort].cumsum()
    L_cumsum /= L_cumsum[-1]
    
    xbins = 0.5 * (xbins[1:] + xbins[:-1])
    ybins = 0.5 * (ybins[1:] + ybins[:-1])

    return xbins, ybins, L_cumsum[i_unsort].reshape(shape)


def plot_MCMC_trace(ax, xdata, ydata, trace, scatter=False, **kwargs):
    xbins, ybins, sigma = compute_sigma_level(trace[0], trace[1])
    ax.contour(xbins, ybins, sigma.T, levels=[0.683, 0.955], **kwargs)
    if scatter:
        ax.plot(trace[0], trace[1], ',k', alpha=0.1)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel(r'$\beta$')
    
    
def plot_MCMC_model(ax, xdata, ydata, trace):
    ax.plot(xdata, ydata, 'ok')

    alpha, beta = trace[:2]
    xfit = np.linspace(-20, 120, 10)
    yfit = alpha[:, None] + beta[:, None] * xfit
    mu = yfit.mean(0)
    sig = 2 * yfit.std(0)

    ax.plot(xfit, mu, '-k')
    ax.fill_between(xfit, mu - sig, mu + sig, color='lightgray')

    ax.set_xlabel('Number')
    ax.set_ylabel('Chance')


def plot_MCMC_results(xdata, ydata, trace, colors='k'):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    plot_MCMC_trace(ax[0], xdata, ydata, trace, True, colors=colors)
    plot_MCMC_model(ax[1], xdata, ydata, trace)
    
#basic Bayesian module
    
import emcee 
print(emcee.__version__)
def log_prior(theta):
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # returns log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def log_likelihood(theta, x, y):
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    return -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)

def log_posterior(theta, x, y):
    return log_prior(theta) + log_likelihood(theta, x, y)

nparam = 3  # number of parameters 
nwalkers = 100  # number of MCMC walkers
nburn = 7000  # "burn-in" period so algorithm stabilizes
nsteps = 8000  # number of MCMC steps 


# set theta near the maximum likelihood, with 
np.random.seed(10)
starting_guesses = np.random.random((nwalkers, nparam))
sampler = emcee.EnsembleSampler(nwalkers, nparam, log_posterior, args=[xdata, ydata])

#running again
emcee_trace = sampler.chain[:, nburn:, :].reshape(-1, nparam).T
plot_MCMC_results(xdata, ydata, emcee_trace)


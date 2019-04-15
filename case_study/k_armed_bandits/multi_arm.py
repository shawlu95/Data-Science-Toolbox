import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from time import time

def two_sample_z_test(est_p, wins, traffic, alpha=0.05):
    """
    Perform two-sample z test on champion arm and second arm.
    
    Parameters
    ----------
    est_p list[float]: estimated click through rates
    wins list[int]: conversion for each arm
    traffic list[int]: traffic diverted to each arm
    alpha float: false positive rate (tyoe I error)
    
    Returns true if statistically significant.
    """
    winner_idx = np.argmax(est_p)
    second_idx = sorted([(p, i) for i, p in enumerate(est_p)])[-2][1]
    
    p0, p1 = est_p[winner_idx], est_p[second_idx]
    x0, x1 = wins[winner_idx], wins[second_idx]
    n0, n1 = traffic[winner_idx], traffic[second_idx]

    p_pooled = (x0 + x1) / (n0 + n1)
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1 / n0 + 1 / n1))
    
    # note that z is guaranteed to be positive
    z = (p0 - p1) / se
    p_val = 2 * (1 - norm.cdf(abs(z)))
    
    return p_val < alpha

class Arm(object):
    """
    Each arm's true click through rate is 
    modeled by a beta distribution.
    """
    def __init__(self, idx, a=1, b=1):
        """
        Init with uniform prior.
        """
        self.idx = idx
        self.a = a
        self.b = b
        
    def record_success(self):
        self.a += 1
        
    def record_failure(self):
        self.b += 1
        
    def draw_ctr(self):
        return np.random.beta(self.a, self.b, 1)[0]
    
    def mean(self):
        return self.a / (self.a + self.b)
    
    def __str__(self):
        return "arm %i, a=%i, b=%i"%(self.idx, self.a, self.b)

def monte_carlo_simulation(arms, draw=100):
    """
    Monte Carlo simulation of thetas. Each arm's click through
    rate follows a beta distribution.
    
    Parameters
    ----------
    arms list[Arm]: list of Arm objects.
    draw int: number of draws in Monte Carlo simulation.
    
    Returns
    -------
    mc np.matrix: Monte Carlo matrix of dimension (draw, n_arms).
    p_winner list[float]: probability of each arm being the winner.
    """
    # Monte Carlo sampling
    alphas = [arm.a for arm in arms]
    betas = [arm.b for arm in arms]
    mc = np.matrix(np.random.beta(alphas, betas, size=[draw, len(arms)]))
    
    # count frequency of each arm being winner 
    counts = [0 for _ in arms]
    winner_idxs = np.asarray(mc.argmax(axis=1)).reshape(draw,)
    for idx in winner_idxs:
        counts[idx] += 1
    
    # divide by draw to approximate probability distribution
    p_winner = [count / draw for count in counts]
    return mc, p_winner

def k_arm_bandit_mc(ctrs, alpha=0.05, burn_in=1000, max_iter=100000, draw=100, silent=False):
    """
    Perform stochastic k-arm bandit test. Experiment is terminated when
    value remained in experiment drops below certain threshold.
    
    Parameters
    ----------
    ctrs list[float]: true click through rates for each arms.
    alpha float: terminate experiment when the (1 - alpha)th percentile
        of the remaining value is less than 1% of the winner's click through rate.
    burn_in int: minimum number of iterations.
    max_iter int: maxinum number of iterations.
    draw int: number of rows in Monte Carlo simulation.
    silent bool: print status at the end of experiment.
    
    Returns
    -------
    idx int: winner's index.
    est_ctrs list[float]: estimated click through rates.
    wins list[int]: number of conversion in each arm.
    traffic list[int]: number of traffic in each arm.
    history_p, history_ctr list[list[float]]: storing est_ctrs and p_winner.
    history_alphas, history_betas list[list[int]]: storing alpha and beta for each arm.
    values_remaining list[float]: remaining value for each row of Monte Carlo matrix.
    """
    n_arms = len(ctrs)
    arms = [Arm(idx=i) for i in range(n_arms)]
    history_ctr = [[] for _ in range(n_arms)]
    history_p = [[] for _ in range(n_arms)]
    history_alphas = [[] for _ in range(n_arms)]
    history_betas = [[] for _ in range(n_arms)]
    history_idx = []
    
    for i in range(max_iter):
        # stochastic sampling: take one draw for each arm
        # divert traffic to best draw
        sample_p = [arm.draw_ctr() for arm in arms]
        idx = np.argmax(sample_p)
        history_idx.append(idx)
        arm, ctr = arms[idx], ctrs[idx]

        # update arm's beta parameters
        if np.random.rand() < ctr:
            arm.record_success()
        else:
            arm.record_failure()

        # record current estimates of each arm's ctr
        est_ctrs = [arm.mean() for arm in arms]
        for j, p in enumerate(est_ctrs):
            history_ctr[j].append(p)

        # record current estimates of each arm being winner
        mc, p_winner = monte_carlo_simulation(arms, draw)
        for j, p in enumerate(p_winner):
            history_p[j].append(p)
        
        # record alpha and beta
        for j, arm in enumerate(arms):
            history_alphas[j].append(arm.a)
            history_betas[j].append(arm.b)
            
        # terminate when value remaining is negligible
        if i >= burn_in:
            winner_idx = np.argmax(p_winner)
            values_remaining = (mc.max(axis=1) - mc[:, winner_idx]) / mc[:, winner_idx]
            if np.percentile(values_remaining, q=100 * (1 - alpha)) < 0.01 * est_ctrs[winner_idx]:
                if not silent: print("Winning arm %i beats second arm at iteration %i"%(idx, i + 1))
                break

    wins = [arm.a - 1 for arm in arms]
    traffic = [arm.a + arm.b - 2 for arm in arms]
    return idx, est_ctrs, wins, traffic, history_ctr, history_p, history_idx, history_alphas, history_betas, values_remaining

def k_arm_bandit(ctrs, alpha=0.05, burn_in=100, max_iter=100000, silent=False):
    """
    Perform stochastic k-arm bandit test. Experiment is terminated when
    champion arm defeats the second place with statistical significance.
    
    Parameters
    ----------
    ctrs list[float]: true click through rates for each arms.
    alpha float: false positive rate (tyoe I error)
    burn_in int: minimum number of iterations.
    max_iter int: maxinum number of iterations.
    silent bool: print status at the end of experiment.
    
    Returns
    -------
    idx int: winner's index.
    est_ctrs list[float]: estimated click through rates.
    wins list[int]: number of conversion in each arm.
    traffic list[int]: number of traffic in each arm.
    history list[list[float]]: storing est_ctrs.
    """

    n_arms = len(ctrs)
    arms = [Arm(idx=i) for i in range(n_arms)]
    history = [[] for _ in range(n_arms)]
    
    for i in range(max_iter):
        # stochastic sampling: take one draw for each arm
        # divert traffic to best draw
        sample_p = [arm.draw_ctr() for arm in arms]
        idx = np.argmax(sample_p)
        arm, ctr = arms[idx], ctrs[idx]
        
        # update arm's beta parameters
        if np.random.rand() < ctr:
            arm.record_success()
        else:
            arm.record_failure()
        
        # record current estimates of each arm being winner
        est_ctrs = [arm.mean() for arm in arms]
        for j, p in enumerate(est_ctrs):
            history[j].append(p)
        
        # terminate experiment when champion arm defeats 
        # the second place with statistical significance.
        if i > burn_in:
            wins = [arm.a - 1 for arm in arms]
            traffic = [arm.a + arm.b - 2 for arm in arms]
            if two_sample_z_test(est_ctrs, wins, traffic, alpha):
                if not silent: print("Winning arm %i beats second arm at iteration %i"%(idx, i + 1))
                break
    return idx, est_ctrs, wins, traffic, history

def epsilon_greedy(ctrs, alpha=0.05, epsilon=0.3, burn_in=100, max_iter=100000, silent=False):
    """
    With probability epsilon, randomly explore a non-optimal arm.
    Otherwise, greedily exploit current winning arm. 

    Experiment is terminated when champion arm defeats the second 
    place with statistical significance.

    Parameters
    ----------
    ctrs list[float]: true click through rates for each arms.
    alpha float: false positive rate (tyoe I error)
    burn_in int: minimum number of iterations.
    max_iter int: maxinum number of iterations.
    silent bool: print status at the end of experiment.

    Returns
    -------
    winner_idx int: winner's index.
    est_ctrs list[float]: estimated click through rates.
    wins list[int]: number of conversion in each arm.
    traffic list[int]: number of traffic in each arm.
    history_ctr list[list[float]]: storing est_ctrs.
    """
    idx = winner_idx = 0
    n_arms = len(ctrs)
    history_ctr = [[] for _ in range(n_arms)]

    traffic = np.array([1] * n_arms)
    wins = np.array([int(np.random.rand() < ctr) for ctr in ctrs])

    for i in range(max_iter):    
        if np.random.rand() < epsilon:
            # randomly choose a arm
            idx = np.random.randint(0, len(ctrs))
        else:
            # greedily use the best arm
            idx = winner_idx
        ctr = ctrs[idx]

        # new user arrives
        wins[idx] += int(np.random.rand() < ctr)
        traffic[idx] += 1

        # record estimated click through rates
        est_ctrs = wins / traffic
        for j, p in enumerate(est_ctrs):
            history_ctr[j].append(p)

        # update champion's index
        winner_idx = np.argmax(est_ctrs)

        # terminate if statistical significant
        if i >= burn_in:
            if two_sample_z_test(est_ctrs, wins, traffic, alpha):
                if not silent: print("Winning arm %i beats second arm at iteration %i"%(winner_idx, i + 1))
                break
    return winner_idx, est_ctrs, wins, traffic, history_ctr

def plot_history(ctrs, est_ctrs, df_history, title, rolling=10, fname=None, transparent=False):
    """
    Plot evolution of conversion rates estimates or winner probability for each arm.
    
    Parameters
    ----------
    ctr, est_ctrs list[float]: true ctrs and estiamted ctrs.
    df_history list[list[float]]: a nested list of each arm's history.
    rolling int: rolling window length.
    fname str: enter file name if need to store, including '.png'.
    transparent bool: make background transparent.
    """
    true_winner_idx = np.argmax(ctrs)
    winner_idx = np.argmax(est_ctrs)
    
    cols = ["arm_%i_ctr=%.2f"%(i + 1, ctr) for i, ctr in enumerate(ctrs)]
    data = {col : hist for col, hist in zip(cols, df_history)}
    df_history_ma = pd.DataFrame(data).rolling(rolling).mean()
    
    plt.figure(figsize=(12, 4))
    for i, col in enumerate(cols):
        if i == true_winner_idx :
            plt.plot(df_history_ma[col], lw=2, color='b')
        elif i == winner_idx:
            plt.plot(df_history_ma[col], lw=2, color='r')
        else:
            plt.plot(df_history_ma[col], alpha=0.5)

    legend = ["true ctr = %.3f, est ctr = %.3f"%(true, est) for true, est in zip(ctrs, est_ctrs)]
    plt.legend(legend, frameon=False, loc='upper center', ncol=3)
    plt.title(title)
    plt.ylim(0, 1)
    
    if fname:
        plt.savefig('outputs/%s'%fname, transparent=transparent)
    plt.show()
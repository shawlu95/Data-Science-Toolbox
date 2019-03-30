import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from time import time

def bernoulli(p):
    return np.random.rand() < p

def two_sample_z_test(est_p, wins, traffic, alpha=0.05):
    winner_idx = np.argmax(est_p)
    second_idx = sorted([(p, i) for i, p in enumerate(est_p)])[-2][1]
    p1, p2 = est_p[winner_idx], est_p[second_idx]
    x1, x2 = wins[winner_idx], wins[second_idx]
    n1, n2 = traffic[winner_idx], traffic[second_idx]

    p_pooled = (x1 + x2) / (n1 + n2)
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    p_val = 2*(1 - norm.cdf(abs(z)))
    
    return p_val < alpha

def epsilon_greedy(ctrs, alpha=0.05, epsilon=0.3, burn_in=100, max_iter=100000, silent=False):
    idx = winner_idx = 0
    n_arm = len(ctrs)
    wins = np.array([0] * n_arm)
    traffic = np.array([1] * n_arm)
    history = [[] for _ in range(n_arm)]

    for i in range(max_iter):    
        if np.random.rand() < epsilon:
            # randomly choose a arm
            while idx == winner_idx:
                idx = np.random.randint(0, len(ctrs))
        else:
            # greedily use the best arm
            idx = winner_idx
        ctr = ctrs[idx]

        # new user arrives
        conversion = bernoulli(ctr)

        wins[idx] += int(conversion)
        traffic[idx] += 1

        if sum(wins) != 0:
            est_p = wins / traffic
            winner_idx = np.argmax(est_p)

            for j, p in enumerate(est_p):
                history[j].append(p)

        if i >= burn_in:
            if two_sample_z_test(est_p, wins, traffic, alpha):
                if not silent: print("Winning arm %i beats second arm at iteration %i"%(winner_idx, i + 1))
                break
    return winner_idx, est_p, wins, traffic, history

class Arm(object):
    def __init__(self, idx, a=1, b=1):
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

def k_arm_bandit(ctrs, alpha=0.05, burn_in=100, max_iter=100000, silent=False):
    cols = ["arm_%i_ctr=%.2f"%(i + 1, ctr) for i, ctr in enumerate(ctrs)]
    
    # slow
    # df_history = pd.DataFrame(columns=cols)

    n_arms = len(ctrs)
    arms = [Arm(idx=i) for i in range(n_arms)]
    history = [[] for _ in range(n_arms)]
    
    for i in range(max_iter):
        sample_p = [arm.draw_ctr() for arm in arms]

        idx = np.argmax(sample_p)
        ctr = ctrs[idx]
        arm = arms[idx]
        
        if bernoulli(ctr):
            arm.record_success()
        else:
            arm.record_failure()

        mean_ps = [arm.mean() for arm in arms]
        wins = [arm.a - 1 for arm in arms]
        traffic = [arm.a + arm.b - 2 for arm in arms]
        
        for j, p in enumerate(mean_ps):
            history[j].append(p)
                
        # slow
        # df_history = df_history.append({col : mean_p for col, mean_p in zip(cols, mean_ps)}, ignore_index=True)
        
        if i > burn_in:
            if two_sample_z_test(mean_ps, wins, traffic, alpha):
                if not silent: print("Winning arm %i beats second arm at iteration %i"%(idx, i + 1))
                break
    return idx, mean_ps, wins, traffic, history
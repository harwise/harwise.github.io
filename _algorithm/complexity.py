import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

N = 1024

# a(n) = a(0) + a(1) + ... + a(n-1)
# a(n) = 2 * a(n-1)
x = list()
a = list()
x.append(0)
a.append(1)
for i in range(N):
    x.append(i+1)
    a.append(sum(a))

# fibonacci
# fib(n) = fib(0) + ... + fib(n-2)
# fib(n) = fib(n-1) + fib(n-2)
fib = list()
fib.append(1)
fib.append(1)
for i in range(N-1):
    fib.append(fib[-1]+fib[-2])

# b(n) = b(n-1) + b(n/2)
b = list()
b.append(1)
for i in range(N):
    b.append(b[i-1]+b[int(i/2)])

#print(a)
x = range(N+1)
df = pd.DataFrame({
    'N': x, 
    'A_n': a,
    'fib_n' : fib,
    'b_n' : b,
})

plt.xlim([0, 100])
plt.ylim([1e6, 1e9])
#plt.yscale('log')
plt.plot( 'N', 'A_n', data=df, color='red')
plt.plot( 'N', 'fib_n', data=df, color='blue')
#plt.plot( 'N', 'b_n', data=df, color='black')
plt.show()


nn = list()
for i in range(20):
    nn.append(pow(i,i))

print(nn)

sys.exit()


n = 50
X = uniform.rvs(0, 1, size=n)
theta_hat = X.max()

# Run bootstrap

B = 100000
t_boot = np.empty(B)
for i in range(B):
    xx = np.random.choice(X, n, replace=True)
    t_boot[i] = xx.max()

se_boot = t_boot.std()

alpha = 0.05
z = norm.ppf(1-alpha/2)
normal_conf = (theta_hat - z * se_boot, theta_hat + z * se_boot)
print("95%% confidence interval (Normal): %.3f, %.3f" % normal_conf)

bins = np.linspace(0.75, 1.05, 200)

def theta_cdf(x):
    if x <= 0: return 0
    if x >= 1: return 1
    return x**50

theta_cdf_bins = list(map(theta_cdf, bins))
theta_cdf_bins_delta = np.empty(len(bins))
theta_cdf_bins_delta[0] = 0
theta_cdf_bins_delta[1:] = np.diff(theta_cdf_bins)    

plt.figure()
plt.hist(t_boot, bins, label='bootstrap', color='blue', histtype='step', density=True)

plt.figure()
plt.step(bins, theta_cdf_bins_delta, color='green', label='True sampling distribution')


plt.show()

sys.exit()

n = 100
alpha = 0.05
r = norm.rvs(size=n)
#r = cauchy.rvs(size=n)

epsilon = math.sqrt((1 / (2 * n)) * math.log(2 / alpha))

F_n = lambda x : sum(r < x) / n
L_n = lambda x : max(F_n(x) - epsilon, 0)
U_n = lambda x : min(F_n(x) + epsilon, 1)

xx = sorted(r)

df = pd.DataFrame({
    'x': xx, 
    'F_n': np.array(list(map(F_n, xx))), 
    'U_n': np.array(list(map(U_n, xx))), 
    'L_n': np.array(list(map(L_n, xx))), 
    'CDF': np.array(list(map(norm.cdf, xx)))
})

plt.plot( 'x', 'L_n', data=df, color='red')
plt.plot( 'x', 'U_n', data=df, color='green')
plt.plot( 'x', 'CDF', data=df, color='purple')
plt.plot( 'x', 'F_n', data=df, color='black')
plt.show()

bounds = []
for k in tqdm(range(100)):
    n = 100
    alpha = 0.05
    r = norm.rvs(size=n)
    epsilon = math.sqrt((1 / (2 * n)) * math.log(2 / alpha))

    F_n = lambda x : sum(r < x) / n
    L_n = lambda x : max(F_n(x) - epsilon, 0)
    U_n = lambda x : min(F_n(x) + epsilon, 1)

    # xx = sorted(r)
    xx = r # No need to sort without plotting
    
    df = pd.DataFrame({
        'x': xx, 
        'F_n': np.array(list(map(F_n, xx))), 
        'U_n': np.array(list(map(U_n, xx))), 
        'L_n': np.array(list(map(L_n, xx))), 
        'CDF': np.array(list(map(norm.cdf, xx)))
        #'CDF': np.array(list(map(cauchy.cdf, xx)))
    })
    all_in_bounds = ((df['U_n'] >= df['CDF']) & (df['CDF'] >= df['L_n'])).all()
    #all_in_bounds = ((df['U_n'] >= df['CDF']) & (df['CDF'] >= df['L_n']))
    bounds.append(all_in_bounds)    
    
print('Average fraction in bounds: %.3f' % np.array(bounds).mean())

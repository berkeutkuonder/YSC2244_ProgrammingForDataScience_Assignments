#Assignment 1
import matplotlib.pyplot as plt
from math import pi,sqrt,exp,log,sin,cos

def lcg(m,a,c,x): #Linear Congruential Generator (LCG)
    new = (x*a + c) % m
    return new

m = 2147483647; a = 48271; c = 0 #MINSTD Constants

rand_seed = 42 #Random seed for LCG

def lcg_rand(): #Produces one random lcg number by using MINSTD constants
    global rand_seed
    rand_seed = lcg(m,a,c,rand_seed)
    return rand_seed

def lcg_randint(lb, ub, size): #Creates a list of 'size' amount of numbers between lb(lower boundary) and ub(upper boundary)
    nums = []
    while len(nums) != size:
        num = lcg_rand()
        nums.append(num)
    nums = [(i % ub) + lb for i in nums]
    return nums

def test_lcg_randint(): #Test function for lcg_randint()
    lb = 1; ub = 100; size = 25
    lst = lcg_randint(lb, ub, size) 
    for num in lst:
        if num < lb:
            raise Exception('There is a number below the lower boundary: {}'.format(num))
        if num > ub:
            raise Exception('There is a number above the upper boundary: {}'.format(num))
    print('The function lcg_randint workds fine')

test_lcg_randint() #Testing lcg_randint()     

def uniform_float(): #Returns a float number in [0,1[ interval following uniform distribution
    global rand_seed
    rand_seed = lcg(m,a,c,rand_seed)
    return float(rand_seed/m)

def test_uniform_float(): #Tests whether the uniform_float() function create a uniform data
    data = [uniform_float() for x in range(10000000)]
    plt.hist(data, bins=1000)
    plt.show()

test_uniform_float()
#A plot created by using uniform_float() function and in each case, the distribution looks like a uniform distribution
#between 0 and 1. Therefore, we can conclude that uniform_float() works fine

#%%EXTRAS - Normal Distribution
def BoxMuller(u1,u2): #Creates a normal distribution by using Box-Muller method
    #More info can be found: https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform
    z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
    z2 = sqrt(-2*log(u1))*sin(2*pi*u2)
    return z1,z2

#Box-Muller method creates 2 numbers at the same time, but our normal_float() function should return one number at a time
#Therefore, the variables below are used to store the second number and return it when the function is called again
print_z2 = False; z2 = 0

 
def normal_float(): #Creates a random number following normal distribution 
    global print_z2, z2
    if print_z2:
        print_z2 = False
        return z2
    u1, u2 = uniform_float(),uniform_float()
    z1, z2 = BoxMuller(u1,u2)
    return z1
  
def test_normal_float(): #Tests whether the normal_float() function create a data following normal distribution
    data = [normal_float() for x in range(10000000)]
    plt.hist(data, bins=1000)
    plt.show()

test_normal_float()
#A plot created by using normal_float() function and in each case, the distribution looks like a normal distribution.
#Also, the plot looks like the plot that Prof Bodin has in his lecture notes 02_Lab_RandomGenerator.html
#Therefore, we can conclude that normal_float() works fine

#%%EXTRAS - Poisson Distribution
def poisson_int(L): #Given the parameter lambda(L), creates a Poisson random variable by using a uniform distribution
    #More info can be found (at page 27):https://www.win.tue.nl/~marko/2WB05/lecture8.pdf
    if L < 1: #Checking for an appropriate input
        raise Exception('Lambda(L) should be greater than zero! Input argument was: {}'.format(L))
    i = 0
    res = 1
    while res > exp(-L):
        i +=1
        res *= uniform_float()
    return (i-1)
#%%
def test_poisson_int(): #Tests whether the normal_float() function create a data following normal distribution
    values = [poisson_int(10) for x in range(100000)]
    plt.hist(values, 100)
    plt.show()

test_poisson_int()
#A plot created by using poisson_int() function and in each case, the distribution looks like a poisson distribution.
#Also, the plot looks like the plot that Prof Bodin has in his lecture notes 02_Lab_RandomGenerator.html
#Therefore, we can conclude that poisson_int() works fine

#%%EXTRAS - Geometric Distribution
def geometric_float(p): #Given the parameter success probability(p), creates a Geometric random variable by using a uniform distribution
    #More info can be found (at page 22):https://www.win.tue.nl/~marko/2WB05/lecture8.pdf
    if p <= 0: #Checking for an appropriate input
        raise Exception('Probability(p) should be greater than 0! Input argument was: {}'.format(p))
    if p >= 1: #Checking for an appropriate input
        raise Exception('Probability(p) should be less than 1! Input argument was: {}'.format(p))
    u = uniform_float()
    x = log(u)/log(1-p)
    return x
#%%
def test_geometric_float(): #Tests whether the normal_float() function create a data following normal distribution
    data = [geometric_float(0.1667) for x in range(100000)]
    plt.hist(data, bins=100)
    plt.show()
#%%
test_geometric_float()
#A plot created by using geometric_float() function and in each case, the distribution looks like a geometric distribution.
#Also, the plot looks like the geometric distribution in https://i2.wp.com/statisticsbyjim.com/wp-content/uploads/2018/01/geometric.png?resize=576%2C384
#Therefore, we can conclude that geometric_float() works fine
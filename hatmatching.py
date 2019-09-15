import math
import random

#probability that out of n party-goers, k of them get back their original hat
def getProb(n,k,num_trials = 10000):
    hats = list(range(n))
    succ = 0;
    for i in range(num_trials):
        hats2 = shuffle(hats)
        if(len([j for j in range(n) if hats2[j] == j])==k):
            succ = succ + 1;
    return succ/num_trials

def shuffle(hats:list):
    for i in range(len(hats)-1):
        j = int(random.random()*(len(hats)-i)+i)
        swapvar = hats[i]
        hats[i] = hats[j]
        hats[j] = swapvar
    return hats

#for testing the shuffle function
def testshuffle():
    hats = [1,2,3]
    count = 0
    for i in range(10000):
        if(shuffle(hats)==[1,2,3]):
            count = count + 1
    #should print about 1/6
    print(count/10000)

#Instead of simulating, compute using derived formula
#round_off is 0 for no rounding, otherwise number of digits to round to
def computeProb(n,k,round_off = 0):
    count = 0;
    for i in range(n-k+1):
        count = count + (-1)**i / math.factorial(i)
    count = count/math.factorial(k)
    if round_off > 0:
        count = round(count,round_off)
    return count

def prompt():
    done = False
    while(not done):
        try:
            n = int(input("Please enter a value for n: "))
            k = int(input("Please enter a value for k: "))
            if(k>n):
                raise Exception
            else:
                print("\nThe probability that "+ str(k) + " of the "
                  + str(n) + " party-goers receive the correct hat is: ")
                print("Simulated probability: " + str(getProb(n,k)))
                print("Computed probability: " + str(computeProb(n,k,4)))
        except:
            print("Something didn't work! Please try again.")
        try:
            cont = input("Continue? (y/n): ")
            if('n' in cont):
                done = True
        except:
            pass

if __name__ == '__main__':
    prompt()

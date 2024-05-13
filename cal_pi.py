import sys
from decimal import Decimal, getcontext

def calculate_pi(precision):
    getcontext().prec = precision + 1
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    for i in range(1, precision):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    return pi

if __name__ == "__main__":
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])  #Get number of digits from command line
    else:
        digits = 10  #Default value when there are no command line arguments

    pi = calculate_pi(digits)
    print(str(pi))

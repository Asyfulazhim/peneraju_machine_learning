def simpleInterest(principle, period, rate):
    return (principle * period * rate) / 100

def compoundInterest(principle, period, rate, n=1):
    return principle * (1 + rate / (100 * n)) ** (n * period)


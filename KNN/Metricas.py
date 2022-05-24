def Manhattan(X, Y):
    d = 0
    for i in range(len(X)):
        d = d + abs(X[i] - (Y[i]))
    return d


def EuclidianaProm(X, Y):
    d = 0
    for i in range(len(X)):
        d = d + (X[i] - Y[i])**2
    d = (d/len(X))**(1/2)
    return d


def DifCaracterProm(X, Y):
    d = 0
    for i in range(len(X)):
        d = d + abs(X[i] - Y[i])
    d = d/len(X)
    return d


def Canberra(X, Y):
    d = 0
    for i in range(len(X)):
        d = abs(X[i] - Y[i])/(abs(X[i]) + abs(Y[i])) + d
    return d
import numpy

# ----------------------------------------------------
# Getting a random dataset
#
#  N:     number of input dimensions
#  d:     number of dimensions
# ----------------------------------------------------

def getdata(N,d):
    r = numpy.random.mtrand.RandomState(1234)
    X = r.normal(0,1,[d,N])
    v = r.normal(0,1,[d])
    T = numpy.dot(X.T,v) + 0.1*r.normal(0,1,[N])
    return X,T



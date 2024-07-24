import numpy as np

def assembleKr(s):
    Ne = np.size(s.elements, axis = 1)
    N = np.size(s.nodes, axis = 1)
    K = np.zeros([N,N])
    r = np.zeros(N) 
    for i in range(0, Ne):
        Ie = s.elements[:, i]
        xe = s.nodes[:,s.elements[:,i]]
        Ke = s.keFunc(xe)
        re = s.reFunc(xe)
        K[np.ix_(Ie, Ie)] += Ke
        r[Ie] += re
    

    return K, r


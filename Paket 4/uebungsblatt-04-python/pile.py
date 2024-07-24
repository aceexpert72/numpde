import numpy as np

def pileKe(s):
        def computeKe(xe):
                h = abs(xe[0,1]-xe[0,0])
                Ke = (s.EA/h) * np.array([[1,-1],[-1,1]]) + (s.C*h/6) * np.array([[2,1],[1,2]])
                return Ke
        return computeKe

def pileRe(s):
        def computeRe(xe):
                h = abs(xe[0,1]-xe[0,0])
                Re = s.n * (h/2) * np.array([1,1])
                return Re
        return computeRe



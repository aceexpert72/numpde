

import numpy as np

def compute_error(u,xh,uHat):
    N = len(xh)
    M = 100*(N-1)+1
    xf = np.linspace(xh[0],xh[-1],M)
    yf = u(xf)
    yh_interp = np.interp(xf, xh, uHat)
    abs_diff = np.abs(yf - yh_interp)
    max_error = np.max(abs_diff)

    return max_error

def pileFEM(s,k):
    
    N = k + 1
    h = s.l/k
    
    def tridiag(a,b,c):
        return \
            np.diag([a]+(N-2)*[b]+[a])+ \
            np.diag((N-1)*[c],k=1)+ \
            np.diag((N-1)*[c],k=-1)

    K_EA = s.EA / h * tridiag(1,2,-1)
    K_C = h * s.C / tridiag(2,4,1)

    K_S = np.zeros([N,N])
    K_S[-1,-1] = s.S

    K = K_EA + K_C + K_S

    r = s.n * h / 2 * np.array ([1] + (N-2) * [2] + [1])
    r[0]= s.F

    uHatK = np.linalg.solve(K,r)
    xK = np.linspace (0, s.l, k+1)
    return [xK, uHatK]

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

def assembleKr_gmsh(m): #Übung 7 Aufgabe 1.3
    N = m.nodes.shape[1]
    K = np.zeros([N, N])
    r = np.zeros([N])
    Ne = m.elements.shape[1]
    
    for e in range(0, Ne):
        Ie = m.elements[:, e]
        xe = m.nodes[:, m.elements[:, e]]
        Ke = m.p.keFunc(xe)
        re = m.p.reFunc(xe)
        
        K[np.ix_(Ie, Ie)] += Ke
        r[Ie] += re
        
    return K, r

def assembleKr_gmsh_complex(m): #Übung 7 Aufgabe 1.3
    N = m.nodes.shape[1]
    K = np.zeros([N, N])
    r = np.zeros([N])
    Ne = m.elements.shape[1]
    
    for n in m.groupNames:
        g = m.groups[n]
        
        for e in range(0, g.Ne):
            Ie = g.elements[:, e]
            xe = m.nodes[:, g.elements[:, e]]
            
            if 'keFunc' in g.p:
                Ke = g.p.keFunc(xe)
                K[np.ix_(Ie, Ie)] += Ke
                
            if "reFunc" in g.p:    
                re = g.p.reFunc(xe)
                r[Ie] += re
            
        
    return K, r

def heatKe(lambder):
    def computeKe(x):
        Ke = np.zeros([3,3])
        u = x[:,1] - x[:,0]
        v = x[:,2] - x[:,1]
        w = x[:,0] - x[:,2]
        Ae = 1/2 * np.abs(np.cross(u,v))
        Be = 1/(2*Ae) * np.array([[v[1],w[1],u[1]],[-v[0],-w[0],-u[0]]])
        #print('Be =',Be)
        #print('BeT =',Be.T)
        #print(np.dot(Be,Be.T))
        Ke = lambder * Ae * np.dot(Be.T,Be) 
        #print('Ke =',Ke)
        return Ke
    return computeKe

def heatRe(w):
    def computeRe(x):
        u = x[:,1] - x[:,0]
        v = x[:,2] - x[:,1]
        Ae = abs(1/2 * (u[0]*v[1] - u[1]*v[0]))
        Re = 1/3 * w * Ae * np.array([1, 1, 1])
        return Re
    return computeRe

def robinKe(h):
    def computeKe(x):
        u = x[:,1] - x[:,0]
        le = np.linalg.norm(u)
        Ke = (h * le)/6 * np.array([[2, 1],[1, 2]])
        return Ke
    return computeKe

def robinRe(h, ts):
    def computeRe(x):
        u = x[:,1] - x[:,0]
        le = np.linalg.norm(u)
        Re = (h * le * ts)/2 * np.array([ 1 , 1 ])
        return Re
    return computeRe


#Übungsblatt 9 Aufgabe 2.1
def heatMe(rho, c):
    def computeMe(x):
        u = x[:, 1] - x[:, 0]
        v = x[:, 2] - x[:, 1]
        Ae = abs(1/2 * (u[0]*v[1] - u[1]*v[0]))
        I = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
        Me = 1/12 * rho * c * Ae * I
        return Me
    return computeMe

#Übungsblatt 9 Aufgabe 2.2
def assembleKMr(m):
    k = m.elements.shape[1]
    N = m.nodes.shape[1]
    K = np.zeros([N, N])
    M = np.zeros([N, N])
    r = np.zeros([N])

    for n in m.groupNames:
        g = m.groups[n]
        
        for e in range(0, g.Ne):
            Ie = g.elements[:, e]
            xe = m.nodes[:, g.elements[:, e]]
            
            if 'keFunc' in g.p:
                Ke = g.p.keFunc(xe)
                K[np.ix_(Ie, Ie)] += Ke
            if "reFunc" in g.p:    
                re = g.p.reFunc(xe)
                r[Ie] += re
            if "meFunc" in g.p:    
                Me = g.p.meFunc(xe)
                M[np.ix_(Ie, Ie)] += Me

    return K, M, r

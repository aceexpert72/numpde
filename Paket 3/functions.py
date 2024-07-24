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

def pileKe(Ke):
    Ke = 1
    return Ke

def pileRe(Re):
    Re = 1
    return Re

def assembleKr(Kr):
    Kr = 1
    return Kr



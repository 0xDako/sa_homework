import numpy as np
import json



def K_t(x, k, s):
    l = np.matmul(np.ones((len(s))), np.matmul(x,k))
    return 1/l*np.matmul(x, k)

def task(s): 
    s = json.loads(s)
    l_1 = len(s)
    l_2 = len(s[0])
    r = np.zeros((l_1, l_2, l_2))

    for i in range(l_1):
        for j in range(l_2):
            for k in range(l_2):
                if s[i][j] > s[i][k]:
                    r[i][j][k] = 1
                elif s[i][j] == s[i][k]:
                    r[i][j][k] = 0.5
                else: 
                    r[i][j][k] = 0

    x = np.zeros((l_2, l_2))

    for i in range(l_2):
        for j in range(l_2):
            for k in range(l_1):
                x[i][j] += r[k][i][j]

    x = np.transpose(x/l_1)
    k0 = np.ones((l_1))/l_2

    e = 0.001
    while np.linalg.norm(K_t(x, k0, s) - k0) >= e:
        k0 = K_t(x, k0, s)
    res = list(np.around(K_t(x, k0, s), 3))

    output = json.dumps(res)
    return output


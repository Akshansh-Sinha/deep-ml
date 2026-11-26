import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    avec = np.array(a)
    bvec = np.array(b)

    if avec.shape[1] == bvec.shape[0]:
        return np.dot(avec,bvec).tolist()

    return -1;
import numpy as np 
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    avec = np.array(a)
    bvec = np.array(b)
    if avec.shape[1] == bvec.shape[0]:
        return np.dot(avec,bvec).tolist()
    return -1
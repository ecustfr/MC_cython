# overlap.pyx

# 导入 Cython 编译选项
# 打开 C 级除法、关闭边界检查和数组环绕访问，提高性能
# cython: cdivision=True
# cython: boundscheck=False
# cython: wraparound=False

import numpy as np
cimport numpy as np
import cython.cimports.libc.math as cymath  # 你需要确保 cymath 中定义了 rint 或替换为 libc.math.rint
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def Overlap1(np.ndarray[np.double_t, ndim=1] r_one,
             np.ndarray[np.double_t, ndim=2] r,
             double box_length,
             double sigma) -> bint:
    cdef bint over = False
    cdef Py_ssize_t i, d
    cdef double sigma2 = sigma * sigma
    cdef Py_ssize_t num_par = r.shape[0]

    cdef double ri2
    cdef np.ndarray[np.double_t, ndim=1] ri = np.zeros(3, dtype=np.float64)

    for i in range(num_par):
        ri2 = 0.0
        for d in range(3):
            ri[d] = r_one[d] - r[i, d]
            ri[d] = ri[d] - cymath.rint(ri[d] / box_length) * box_length
            ri2 += ri[d] * ri[d]
        if ri2 < sigma2:
            return True

    return False

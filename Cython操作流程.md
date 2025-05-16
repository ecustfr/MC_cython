要引用c 源代码

1. 拥有一个 c语言的 f.h 文件 其中有函数 int g(int a)
2. 在HH.pyx 文件中写出
`cdef extern from "f.h" :  int g(int a)`  
然后可以调用
` g(n) `

在编译文件中
```
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name = "wrapper_cfib" , sources = ["HH.pyx","f.c"] )

setup(
    ext_modules = cythonize(ext)
)
```
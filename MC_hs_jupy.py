# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:32:21 2025

@author: Administrator
"""

import numpy as np
import cython
from itertools import product 
import cython.cimports.libc.math as cymath



def hs_initial_conf(num_par , box_length , sigma):
    
    n_lattice = np.rint( (num_par/4)**(1/3)) .astype(np.int_)
    
    r_fcc = np.array ( [ [0.25,0.25,0.25],[0.25,0.75,0.75],[0.75,0.75,0.25],[0.75,0.25,0.75] ], dtype=np.float_ )                    
    
    cell = box_length / n_lattice
    
    half_box = box_length/2
    
    delta_n = num_par-n_lattice
    
    
    i = 0
    
    r = np.empty( num_par , dtype = np.float_ )
    
    for ix,iy,iz in product( range(n_lattice) , repeat = 3):
        for a in range(4):
            r[i,:] = r_fcc[a,:] + np.array([ix,iy,iz].astype(np.float_)) 
            r[i,:] = r[i,:]*cell
            r[i,:] = r[i,:] - half_box
            
            i = i+1 
    
                
    
    if delta_n > 0:
        insert_particle( ) 
    elif delta_n < 0 :    
        delete_particle()
    else:
        pass
    
    return r
    
    


def cell_list(): #对 粒子的位置进行分类
    
    pass

def MC_hs( cell_list ):
    pass

def sample_MC():
    

    pass

def ananlyse_MC():
    
    pass

def OverlapAll():
    pass

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
def Overlap1(r_one:cython.double[::1] , r:cython.double[:,::1] , box_length : cython.double , sigma : cython.double )-> bool:
    
    over = False
    
    i : cython.Py_ssize_t
    d : cython.Py_ssize_t
    
    
    sigma2 : cython.float = sigma*sigma
    num_par = r.shape[0] 
    
    
    ri2 : cython.float
    ri  : cython.double[::1] = np.zeros(3)
    
    for i in range(num_par):
        ri2 = 0.0
        for d in range( 3 ):
            ri[d] = r_one[ d,i ] - r[d,i] 
            ri[d] = ri[d] - cymath.rint(ri[d]/box_length) * box_length
            ri2 += ri[d]*ri[d]
        if ri2 < sigma2:
            over = True
            return
    
    return over

def insert_particle() :
    
    pass

def delete_particle():
    pass

if __name__ == '__main__':
    
    num_par     = 64*4
    dimension   = 3
    temperature = 1.50
    beta = 1/ temperature
    
    nsteps = 50000
    
    equilibration_samples = 1000
    
    
    sample_interval = 100
    
    density = 0.2
    
    sigma = 1
    
    eta = density * 3.1415926 * sigma**3 /6 
    
    print(f"\r堆积密度：{eta}")
    
    box_length =  (num_par / density)**(1/dimension)
    
    if box_length < 2 * sigma:
        raise ValueError("sigma too large for this box (2 * rcut = {2*rcut} > {box_length} = box_length)")
    
    
    r = hs_initial_conf(num_par, box_length, sigma) 
    
    for i in range(equilibration_samples):
        samples = sample_MC(  )
        
    for i in range(nsteps):
        
        samples = sample_MC()
    
    
    
    
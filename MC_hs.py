# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:32:21 2025

@author: Administrator
"""

import numpy as np
import overlap1 #用cython 重新写了 判断重叠的函数 overlap1(rone,r,box_length,sigma)
from itertools import product 




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

def MC_hs_origin( r , box_length , sigma , nsteps , sim_par:dict ,sample_or_not:bool , samples:[dict])->[dict]: #不使用 cell list 进行优化
    # sim_par = {Eps_Move:eps_move} eps_move*box_length 粒子移动的最大距离 
    
    eps_move = sim_par['Eps_Move']

    num_par = r.shape[0]
    for i in range(nsteps):
        for par in range(num_par):
            r_try = r[0,:]+ (2*np.random.rand(3)-1)*eps_move
            if overlap1(r_try,r[1:,:],box_length,sigma):
                acc = 0
                
            else:
                acc = 1
                r[0,:] = r_try
                
            r = np.roll(r,1,axis=1)
            acc_total += acc 
        if sample_or_not:
            #进行采样

    acc_ratio = acc_total/(nsteps*num_par)
    return (acc_ratio,r)
    

def MC_hs( cell_list ): # 使用 cell_list 进行优化
    
    pass

def sample_MC():
    

    pass

def ananlyse_MC():
    
    pass

def OverlapAll( r , box_length , sigma):
    num_par = r.shape[0]
    overlap = False
    for i in range(num_par-1):
        overlap = overlap1(r[i,:], r[i+1:,:] , box_length ,sigma )
        if overlap:
            return overlap


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
    
    equilibration_samples = 1000 #
    
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
    
    
    
    
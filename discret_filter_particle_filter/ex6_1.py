# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:49:11 2021

@author: wangy
"""
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

def discrete_filter(bel, u):
    """
    caculate new belief Bel(x)
    
    arguments:
        bel -- current belief of robot podition x
        u -- move command -1 = backward, 1 = forward
    """
    bel_prime = np.zeros(bel.shape[0])
    #这里一定要注意，bel.shape = (20,) bel既不是一个行向量
    #也不是一个列向量，它仅仅是一个20维的数组/向量而已！
    #等效于 a = np.array([1,2,3]) a仅仅是一个三维向量！a.shape = (3,)
    # b = np.array([[1,2,3]]) b.shape = (1,3)
    
    if u == 1:
        for x in range(bel.shape[0]):
            if x >= 2:
                bel2 = bel[x-2]
            else:
                bel2 = 0
            if x >= 1:
                bel1 = bel[x-1]
            else:
                bel1 = 0
            bel0 = bel[x]
            
            if x < bel.shape[0]-1:
                bel_prime[x] = 0.25*bel0 + 0.5*bel1 + 0.25*bel2
            elif x == bel.shape[0]-1:
                bel_prime[x] = 1*bel0 + 0.75*bel1 + 0.25*bel2 
                
    if u == -1:
        for x in range(bel.shape[0]):
            if x < bel.shape[0]-2:
                bel2 = bel[x+2]
            else:
                bel2 = 0
            if x < bel.shape[0]-1:
                bel1 = bel[x+1]
            else:
                bel1 = 0;
            bel0 = bel[x]
            
            if x > 0:
                bel_prime[x] = 0.25*bel2 + 0.5*bel1 + 0.25*bel0
            elif x == 0:
                bel_prime[x] = 0.25*bel2 + 0.75*bel1 + 0.25*bel0
                
    return bel_prime

def plot_histogram(bel):
    plt.cla()
    plt.bar(range(0, bel.shape[0]), bel, width=1.0)
    plt.axis([0, bel.shape[0], 0, 1])
    plt.draw()
    plt.pause(1)
    
def main():
    bel = np.hstack((np.zeros(9), 1, np.zeros(10)))
    
    plt.figure()
    plt.ion()
    plt.show()
    
    for i in range(0, 9):
        plot_histogram(bel)
        bel = discrete_filter(bel, 1)
        print("sum belief", np.sum(bel))
        
    for i in range(0, 3):
        plot_histogram(bel)
        bel = discrete_filter(bel, -1)
        print("sum belief", np.sum(bel))
    
    plt.ioff()
    plt.show()
    
if __name__ == "__main__":
    main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
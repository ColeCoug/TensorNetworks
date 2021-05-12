# -*- coding: utf-8 -*-
""" 
script_binaryMERA.py
---------------------------------------------------------------------
Script file demonstrating how the auto-generated code from the "TensorTrace" \
software can be implemented in a tensor network algorithm (in this case \
an optimization of a binary MERA for the ground state of the 1D transverse \
field quantum Ising model on a finite lattice). This script calls the \
"binaryMERA.py" function file as automatically generated from the example \
TensorTrace project "binaryMERA.ttp" included with the distribution.\ 

by Glen Evenbly (www.glenevenbly.com) - last modified 30/8/2019
"""

from scipy.sparse.linalg import eigsh
from numpy import linalg as LA
import numpy as np
from binaryMERA import binaryMERA 

# set simulation parameters
chi = 6
chi_p = 4
n_levels = 3
n_iterations = 2000
n_sites = 3*(2**(n_levels + 1))

# define hamiltonian
sX = np.array([[0, 1], [1, 0]])
sY = np.array([[0, -1j], [1j, 0]])
sZ = np.array([[1, 0], [0,-1]])
ham_s = (-np.kron(sX,sX)+0.5*np.kron(np.eye(2),sZ)+0.5*np.kron(np.eye(2),sZ));
ham_init = 0.5*np.kron(np.eye(8),np.kron(ham_s,np.eye(2)))+np.kron(np.eye(4),np.kron(ham_s,np.eye(4)))+0.5*np.kron(np.eye(2),np.kron(ham_s,np.eye(8)));
chi_b = 4;

# initialize tensors
uDis = [0 for x in range(n_levels)]
uDis[0] = np.eye(chi_b**2,chi_b**2).reshape(chi_b,chi_b,chi_b,chi_b) 
wIso = [0 for x in range(n_levels)]
wIso[0] = np.random.rand(chi_b,chi_b,chi)
hamThree = [0 for x in range(n_levels+1)]
hamThree[0] = (ham_init - max(LA.eigvalsh(ham_init))*np.eye(chi_b**3)).reshape(chi_b,chi_b,chi_b,chi_b,chi_b,chi_b);
rhoThree = [0 for x in range(n_levels+1)] 
rhoThree[0] = np.random.rand(chi_b,chi_b,chi_b,chi_b,chi_b,chi_b)
for k in range(n_levels-1):
    uDis[k+1] = (np.eye(chi**2,chi_p**2)).reshape(chi,chi,chi_p,chi_p) 
    wIso[k+1] = np.random.rand(chi_p,chi_p,chi)
    hamThree[k+1] = np.random.rand(chi,chi,chi,chi,chi,chi)
    rhoThree[k+1] = np.random.rand(chi,chi,chi,chi,chi,chi)

hamThree[n_levels] = np.random.rand(chi,chi,chi,chi,chi,chi)
rhoThree[n_levels] = np.random.rand(chi,chi,chi,chi,chi,chi)

# do optimization iterations
for p in range(n_iterations):
    
    # sweep over all levels
    for z in range(n_levels):
        if p > 5:
            # optimise disentanglers
            tensor_list = [uDis[z], wIso[z], hamThree[z], rhoThree[z+1]]
            uEnv = binaryMERA(tensor_list, 1, 1) + binaryMERA(tensor_list, 1, 2) + binaryMERA(tensor_list, 2, 1) + binaryMERA(tensor_list, 2, 2)
            uSize = uEnv.shape
            utemp,stemp,vtemph = LA.svd(uEnv.reshape(uSize[0]*uSize[1],uSize[2]*uSize[3]),full_matrices=False)
            uDis[z] = (-utemp @ vtemph).reshape(uSize);
        
        # optimise isometries
        tensor_list = [uDis[z], wIso[z], hamThree[z], rhoThree[z+1]]
        Wenv = binaryMERA(tensor_list, 1, 3) + binaryMERA(tensor_list, 1, 4) + binaryMERA(tensor_list, 1, 5) + binaryMERA(tensor_list, 2, 3) + binaryMERA(tensor_list, 2, 4) + binaryMERA(tensor_list, 2, 5);
        wSize = Wenv.shape
        utemp,stemp,vtemph = LA.svd(Wenv.reshape(wSize[0]*wSize[1],wSize[2]),full_matrices=False);
        wIso[z] = (-utemp @ vtemph).reshape(wSize);
        
        # lift Hamiltonian
        tensor_list = [uDis[z], wIso[z], hamThree[z], rhoThree[z+1]]
        hamThree[z+1] = binaryMERA(tensor_list, 1, 12) + binaryMERA(tensor_list, 2, 12)

    # diagonalize Hamiltonian
    ham_top = (hamThree[n_levels]+hamThree[n_levels].transpose(1,2,0,4,5,3)+hamThree[n_levels].transpose(2,0,1,5,3,4)).reshape(chi**3,chi**3)
    dtemp,vtemp = eigsh(0.5*(ham_top + np.conj(ham_top.T)),k=1,which='SA')
    vtemp = vtemp / LA.norm(vtemp);
    rhoThree[n_levels] = (vtemp @ np.conj(vtemp.T)).reshape(chi,chi,chi,chi,chi,chi);
    
    # lower the density matrix
    for z in range(n_levels-1,-1,-1):
        tensor_list = [uDis[z], wIso[z], hamThree[z], rhoThree[z+1]]
        rhoThree[z] = 0.5*(binaryMERA(tensor_list, 1, 6) + binaryMERA(tensor_list, 2, 6));
    
    # compute energy and magnetization
    Energy_per_site = np.trace(rhoThree[0].reshape(chi_b**3,chi_b**3) @ ham_init)/2;
    ExpectX = np.trace(rhoThree[0].reshape(chi_b**3,chi_b**3) @ np.kron(np.eye(32),sX));
    EnExact = (-2/np.sin(np.pi/(2*n_sites))) / n_sites
    EnError = Energy_per_site - EnExact
    print('Iteration: %d of %d, Energy: %f, Energy Error: %e, XMag: %e\n' % (p,n_iterations,Energy_per_site,EnError,ExpectX))






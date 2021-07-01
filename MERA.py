"""
MERA.py

Cole Coughlin
last updated July 2021

This is class creates a MERA network with the specified number of layers, branches from the top tensor,
and eventually even the number of top tensors. Once the network is generated, you are able to optimize the
groundstate energy of the system by iteratively sweeping through every tensor in the network and updating it.
Currently set up to optomize Transverse Ising model Hamiltonian.
"""

from scipy.sparse.linalg import eigsh
from numpy import linalg as LA
import numpy as np
from binaryMERAfull3 import binaryMERAfull3
import math
import matplotlib.pyplot as plt

class MERA(object):
    # Variables for MERA
    branches = 0
    layers = 0
    numTopTensors = 1
    h = 1
    # Tensors in network
    uDis = []
    wIso = []
    rhoThree = []
    hamThree = []

    # define hamiltonian - Currently set up for Transverse Ising Model with magnetic field h
    sX = np.array([[0, 1], [1, 0]])
    sY = np.array([[0, -1j], [1j, 0]])
    sZ = np.array([[1, 0], [0, -1]])
    ham_s = (-np.kron(sX, sX) + 0.5 * h * np.kron(np.eye(2), sZ) + 0.5 * h * np.kron(np.eye(2), sZ))
    ham_init = 0.5 * np.kron(np.eye(8), np.kron(ham_s, np.eye(2))) + np.kron(np.eye(4), np.kron(ham_s, np.eye(4))) + 0.5 * np.kron(np.eye(2), np.kron(ham_s, np.eye(8)))
    chi = 6   # bond dimension between isometries and rhoThree
    chi_p = 4 # bond dimension between disnetanglers and isometries
    chi_b = 4 # bond dimension on outermost layer to perform calculations of groundstate
    n_sites = 0

    # Constructor for binary MERA
    def __init__(self,branches,layers,numTopTensors=1):
        # initialize network variables
        self.branches = branches
        self.layers = layers
        self.numTopTensors = numTopTensors
        self.n_sites = 3 * (2 ** (layers))

        chi = self.chi
        chi_b = self.chi_b
        chi_p = self.chi_p

        # initialize tensors in network
        # get the total number of disentanglers and isometries in the network. The number is the same for both
        index = 0
        for l in range(1,layers+1):
            index = index + self.numNodesOnLayer(l)

        # initialize tensors for network
        self.uDis = [0 for x in range(index)]
        self.wIso = [0 for x in range(index)]
        # There will be a rhoThree for every isometry as well as one for every outgoing disentangler edge on the bottom layer
        self.rhoThree = [0 for x in range(index+self.numNodesOnLayer(layers+1))]
        self.hamThree = [0 for x in range(index*2)]

        # initialize disentanglers and isometries
        for i in range(index):
            if i >= index - self.numNodesOnLayer(layers):
                self.uDis[i] = np.eye(chi_b ** 2, chi_b ** 2).reshape(chi_b, chi_b, chi_b, chi_b)
                self.wIso[i] = np.random.rand(chi_b, chi_b, chi)
            else:
                self.uDis[i] = (np.eye(chi ** 2, chi_p ** 2)).reshape(chi, chi, chi_p, chi_p)
                self.wIso[i] = np.random.rand(chi_p, chi_p, chi)

        # initialize local hamiltonians
        for i in range(index*2):
            if i >= index*2 - self.numNodesOnLayer(layers)*2:
                self.hamThree[i] = (self.ham_init - max(LA.eigvalsh(self.ham_init)) * np.eye(chi_b ** 3)).reshape(chi_b, chi_b, chi_b, chi_b, chi_b, chi_b)
            else:
                self.hamThree[i] = np.random.rand(chi, chi, chi, chi, chi, chi)

        # initialize rhoThrees
        for i in range(index+self.numNodesOnLayer(layers+1)):
            if i >= index:
                self.rhoThree[i] = np.random.rand(chi_b, chi_b, chi_b, chi_b, chi_b, chi_b)
            else:
                self.rhoThree[i] = np.random.rand(chi, chi, chi, chi, chi, chi)

    # Function gets and returns tensors in enviroment
    def getLoweredRho(self, leadingEdge, layer):
        # get the index of the tensors in the enviroment
        index = 0
        for l in range(1, layer+1):
            index = index + self.numNodesOnLayer(l)

        return index + leadingEdge

    # Function gets and returns tensors in enviroment
    def getLiftedHamiltonian(self, leadingEdge, layer):
        # get the index of the tensors in the enviroment
        index = 0
        for l in range(1, layer-1):
            index = index + self.numNodesOnLayer(l)

        return 2*index + math.floor(leadingEdge/2)

    # Function gets and returns tensors in enviroment
    def getEnviroment(self, leadingEdge, layer):
        # get the index of the tensors in the enviroment
        index = 0
        for l in range(1,layer):
            index = index + self.numNodesOnLayer(l)
        #add the offset for start of enviroment
        if layer==1:
            tensor_list = [self.hamThree[2 * index + leadingEdge],
                           self.uDis[index + math.floor(leadingEdge / 2)],
                           self.uDis[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + math.floor(leadingEdge / 2)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 2) % self.numNodesOnLayer(layer)],
                           self.rhoThree[0].transpose(math.floor(leadingEdge / 2),
                                                 (math.floor(leadingEdge / 2) + 1) % 3,
                                                 (math.floor(leadingEdge / 2) + 2) % 3,
                                                 (math.floor(leadingEdge / 2)) + 3,
                                                 (math.floor(leadingEdge / 2) + 1) % 3 + 3,
                                                 (math.floor(leadingEdge / 2) + 2) % 3 + 3)]
            tensor_list2 = [self.hamThree[2 * index + (leadingEdge+1)% self.numNodesOnLayer(layer)],
                           self.uDis[index + math.floor(leadingEdge / 2)],
                           self.uDis[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + math.floor(leadingEdge / 2)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 2) % self.numNodesOnLayer(layer)],
                           self.rhoThree[0].transpose(math.floor(leadingEdge / 2),
                                                      (math.floor(leadingEdge / 2) + 1) % 3,
                                                      (math.floor(leadingEdge / 2) + 2) % 3,
                                                      (math.floor(leadingEdge / 2)) + 3,
                                                      (math.floor(leadingEdge / 2) + 1) % 3 + 3,
                                                      (math.floor(leadingEdge / 2) + 2) % 3 + 3)]
        else:
            tensor_list = [self.hamThree[2 * index + leadingEdge],
                           self.uDis[index + math.floor(leadingEdge / 2)],
                           self.uDis[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + math.floor(leadingEdge / 2)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 2) % self.numNodesOnLayer(layer)],
                           self.rhoThree[index + math.floor(leadingEdge / 2)]]
            tensor_list2 = [self.hamThree[2 * index + (leadingEdge+1)% self.numNodesOnLayer(layer)],
                           self.uDis[index + math.floor(leadingEdge / 2)],
                           self.uDis[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + math.floor(leadingEdge / 2)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)],
                           self.wIso[index + (math.floor(leadingEdge / 2) + 2) % self.numNodesOnLayer(layer)],
                           self.rhoThree[index + math.floor(leadingEdge / 2)]]

        return tensor_list,tensor_list2, index + math.floor(leadingEdge / 2),index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer),index + (math.floor(leadingEdge / 2) + 1) % self.numNodesOnLayer(layer)

    def numNodesOnLayer(self, layer):
        return int(self.numTopTensors*self.branches*(2**(layer-1)))

    # This method sweeps through every tensor in the MERA and optomizes the enviroments
    # and does the entire sweep a number of times to minimize the ground state energy
    def optimizeMERA(self, n_iterations):
        energy = []
        energyError = []
        # Loop through the number of iterations
        for p in range(n_iterations):
            # sweep over all layers of networks starting at the outtermost layer
            for z in range(self.layers, 0, -1):
                # loop through all the outgoing indices on the disentanglers at the current level
                randomOffset = np.random.randint(0,self.numNodesOnLayer(z))*2
                for a in range(self.numNodesOnLayer(z)):
                    #randomly chose point to start optomization around layer
                    i = (2*a + randomOffset)%(self.numNodesOnLayer(z)*2)
                    # i=a*2

                    # OPTIMIZE DISENTANGLERS

                    # Dis 1

                    tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i,z) # returns list of tensors[hamThree, uDis1, uDis2, wIso1, wIso2, wIso3, rhoThree]

                    uEnv = binaryMERAfull3(tensor_list, 1, 2) + binaryMERAfull3(tensor_list2, 2, 2)
                    uSize = uEnv.shape
                    utemp, stemp, vtemph = LA.svd(uEnv.reshape(uSize[0] * uSize[1], uSize[2] * uSize[3]),
                                                  full_matrices=False)
                    # update tensor with optimized version
                    self.uDis[updateInd] = (-utemp @ vtemph).reshape(uSize)

                    # Dis 2

                    tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i, z)

                    uEnv = binaryMERAfull3(tensor_list, 1, 3) + binaryMERAfull3(tensor_list2, 2, 3)
                    uSize = uEnv.shape
                    utemp, stemp, vtemph = LA.svd(uEnv.reshape(uSize[0] * uSize[1], uSize[2] * uSize[3]),
                                                  full_matrices=False)
                    # update tensor with optimized version
                    self.uDis[updateInd2] = (-utemp @ vtemph).reshape(uSize)

                    # OPTIMIZE ISOMETRIES

                    # Iso 1

                    # tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i, z)

                    # Wenv = binaryMERAfull3(tensor_list, 1, 4) + binaryMERAfull3(tensor_list2, 2, 4)
                    # wSize = Wenv.shape
                    # utemp, stemp, vtemph = LA.svd(Wenv.reshape(wSize[0] * wSize[1], wSize[2]), full_matrices=False)
                    # # update isometry
                    # self.wIso[updateInd] = (-utemp @ vtemph).reshape(wSize)

                    # Iso 2

                    tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i, z)

                    Wenv = binaryMERAfull3(tensor_list, 1, 5) + binaryMERAfull3(tensor_list2, 2, 5)
                    wSize = Wenv.shape
                    utemp, stemp, vtemph = LA.svd(Wenv.reshape(wSize[0] * wSize[1], wSize[2]), full_matrices=False)
                    # update isometry
                    self.wIso[updateInd2] = (-utemp @ vtemph).reshape(wSize)

                    # Iso 3

                    tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i, z)

                    # Wenv = binaryMERAfull3(tensor_list, 1, 6) + binaryMERAfull3(tensor_list2, 2, 6)
                    # wSize = Wenv.shape
                    # utemp, stemp, vtemph = LA.svd(Wenv.reshape(wSize[0] * wSize[1], wSize[2]), full_matrices=False)
                    # # update isometry
                    # self.wIso[updateInd3] = (-utemp @ vtemph).reshape(wSize)

                    # lift Hamiltonian

                    tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i, z)

                    liftedHam = self.getLiftedHamiltonian(i,z)
                    if z != 1:
                        self.hamThree[liftedHam] = binaryMERAfull3(tensor_list, 1, 12) + binaryMERAfull3(tensor_list2, 2, 12)
                    elif a == 0:
                        ham_top = binaryMERAfull3(tensor_list, 1, 12) + binaryMERAfull3(tensor_list2, 2, 12)
                    else:
                        ham_top = ham_top + binaryMERAfull3(tensor_list, 1, 12) + binaryMERAfull3(tensor_list2, 2, 12)

            # diagonalize Hamiltonian
            ham_top = ham_top.reshape(self.chi ** 3, self.chi ** 3)
            dtemp, vtemp = eigsh(0.5 * (ham_top + np.conj(ham_top.T)), k=1, which='SA')
            vtemp = vtemp / LA.norm(vtemp)
            self.rhoThree[0] = (vtemp @ np.conj(vtemp.T)).reshape(self.chi, self.chi, self.chi, self.chi, self.chi, self.chi)

            # lower the density matrix
            for z in range(1,self.layers+1):
                for a in range(self.numNodesOnLayer(z)):
                    i = 2*a
                    tensor_list, tensor_list2, updateInd, updateInd2, updateInd3 = self.getEnviroment(i,z)
                    updateInd = self.getLoweredRho(i,z)
                    self.rhoThree[updateInd] = binaryMERAfull3(tensor_list, 1, 1)
                    self.rhoThree[updateInd+1] = binaryMERAfull3(tensor_list2, 2, 1)

            # compute energy and magnetization
            energyPerSiteTotal = 0
            for a in range(self.numNodesOnLayer(self.layers)):
                i = 2*a
                summedEnergy = (self.rhoThree[len(self.rhoThree)-1 - i] + self.rhoThree[len(self.rhoThree)-2 - i])/2
                summedEnergy = np.trace(summedEnergy.reshape(self.chi_b ** 3, self.chi_b ** 3) @ self.ham_init)/2
                energyPerSiteTotal = energyPerSiteTotal + summedEnergy


            Energy_per_site = energyPerSiteTotal/(self.n_sites/2)
            EnExact = (-2 / np.sin(np.pi / (2 * self.n_sites))) / self.n_sites
            EnError = Energy_per_site - EnExact
            print('Iteration: %d of %d, Energy: %f, Energy Error: %e\n' % (p, n_iterations, Energy_per_site, EnError))
            energy.append(Energy_per_site)
            energyError.append(EnError)

        return energy, energyError
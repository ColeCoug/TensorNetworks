# binaryMERAfull3.py 
import numpy as np 
from ncon import ncon 

def binaryMERAfull3(tensors_in, which_network=None, which_env=0): 
	""" 
Auto-generated network contraction function from 'TensorTrace' software, 
see (www.tensortrace.com) for details, (c) Glen Evenbly, 2019. 
Requires the network contraction routine 'ncon' to be in the working directory, 
(included in the TensorTrace install directory, or also found at 'www.tensortrace.com'). 
------------------------------- 
Input variables: 
------------------------------- 
1st input 'tensors_in' is a list of the unique tensors: tensors_in = [hamThree, uDis1, uDis2, wIso1, wIso2, wIso3, rhoThree] 
2nd input 'which_network' dictates which network to evaluate (1-4) 
3rd input 'which_env' allows one to specify a tensor environment to evaluate from a closed tensor network. 
	 -set 'which_env = 0' to evaluate the scalar from a closed network (i.e. no environment). 
	 -set 'which_env = n' to evaluate environment of the nth tensor from the closed network. 
""" 

	# General project info: 
	# ------------------------------- 
	# Generated on: 26/6/2021
	# Generated from: /Applications/tensortrace(v1.03m)/
	# Index dims: Ind1 = 2, Ind2 = 2, Ind3 = 2, Ind4 = 2; 
 
	# --- Info for Network-1 --- 
	# -------------------------- 
	# network is CLOSED 
	# total contraction cost (in scalar multiplications): 2.30*10^3
	# contraction order: (((((((T1*T2)*T7)*(T4*T9))*(T3*T5))*(T8*T10))*(T6*T11))*T12)
	# 1st leading order cost: (Ind1^9)
	# 2nd leading order cost: (Ind1^8)
	# tensors_N1 = [hamThree,uDis1,uDis2,wIso1,wIso2,wIso3,np.conj(uDis1),np.conj(uDis2),np.conj(wIso1),np.conj(wIso2),np.conj(wIso3),rhoThree] 
	# connects_N1 = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,4],[10,1,11],[2,3,12],[4,5,13],[20,19,9,8],[18,17,7,6],[10,9,21],[8,7,22],[6,5,23],[21,22,23,11,12,13]] 
	# dims_N1 = [[Ind1,Ind1,Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1,Ind1,Ind1]] 
	# cont_order_N1 = [5, 7, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 18, 8, 17, 4, 6, 11, 21, 12, 22, 13, 23,]; 

	# --- Info for Network-2 --- 
	# -------------------------- 
	# network is CLOSED 
	# total contraction cost (in scalar multiplications): 2.30*10^3
	# contraction order: (((((((T1*T8)*T3)*(T6*T11))*(T2*T5))*(T7*T10))*(T4*T9))*T12)
	# 1st leading order cost: (Ind1^9)
	# 2nd leading order cost: (Ind1^8)
	# tensors_N2 = [hamThree,uDis1,uDis2,wIso1,wIso2,wIso3,np.conj(uDis1),np.conj(uDis2),np.conj(wIso1),np.conj(wIso2),np.conj(wIso3),rhoThree] 
	# connects_N2 = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,11],[17,8,18],[9,10,19],[11,12,20],[1,2,16,15],[3,4,14,13],[17,16,23],[15,14,22],[13,12,21],[23,22,21,18,19,20]] 
	# dims_N2 = [[Ind1,Ind1,Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1,Ind1,Ind1]] 
	# cont_order_N2 = [12, 3, 4, 6, 5, 17, 13, 11, 15, 9, 7, 10, 2, 14, 1, 8, 16, 20, 21, 19, 22, 18, 23,]; 

	# --- Info for Network-3 --- 
	# -------------------------- 
	# -- Network is empty. -- 

	# --- Info for Network-4 --- 
	# -------------------------- 
	# -- Network is empty. -- 


	# Contraction Code: 
	# ------------------------------- 

	if len(tensors_in) == 0: # auto-generate random tensors of default dims 
		Ind1 = 2 
		Ind2 = 2 
		Ind3 = 2 
		Ind4 = 2 
		all_dims = [[Ind1,Ind1,Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1],[Ind1,Ind1,Ind1,Ind1,Ind1,Ind1]]; 
		tensors_in = [0 for x in range(len(all_dims))] 
		for k in range(len(all_dims)): 
			tensors_in[k] = np.random.rand(*all_dims[k]) 


	if which_network == 1: 
		if which_env == 0: 
			connects = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,4],[10,1,11],[2,3,12],[4,5,13],[20,19,9,8],[18,17,7,6],[10,9,21],[8,7,22],[6,5,23],[21,22,23,11,12,13]] 
			cont_order = [5, 7, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 18, 8, 17, 4, 6, 11, 21, 12, 22, 13, 23,] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 1: 
			connects = [[-4,-5,1,2],[-6,17,3,4],[10,1,11],[2,3,12],[4,5,13],[-1,-2,9,8],[-3,17,7,6],[10,9,21],[8,7,22],[6,5,23],[21,22,23,11,12,13]] 
			cont_order = [5, 7, 3, 10, 13, 23, 6, 22, 17, 4, 12, 21, 11, 8, 9, 1, 2] 
			return ncon([tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 2: 
			connects = [[20,19,18,-1,-2,16],[16,17,3,4],[10,-3,11],[-4,3,12],[4,5,13],[20,19,9,8],[18,17,7,6],[10,9,21],[8,7,22],[6,5,23],[21,22,23,11,12,13]] 
			cont_order = [5, 7, 3, 10, 13, 23, 6, 22, 17, 4, 12, 21, 11, 8, 9, 20, 19, 18, 16] 
			return ncon([tensors_in[0],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 3: 
			connects = [[20,19,18,14,15,-1],[14,15,1,2],[10,1,11],[2,-3,12],[-4,5,13],[20,19,9,8],[18,-2,7,6],[10,9,21],[8,7,22],[6,5,23],[21,22,23,11,12,13]] 
			cont_order = [5, 7, 14, 15, 10, 20, 19, 1, 9, 13, 23, 6, 22, 18, 8, 11, 21, 2, 12] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 4: 
			connects = [[20,19,18,14,15,16],[14,15,-2,2],[16,17,3,4],[2,3,12],[4,5,13],[20,19,9,8],[18,17,7,6],[-1,9,21],[8,7,22],[6,5,23],[21,22,23,-3,12,13]] 
			cont_order = [5, 7, 14, 15, 3, 20, 19, 13, 23, 6, 22, 17, 4, 12, 18, 16, 2, 8, 9, 21] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 5: 
			connects = [[20,19,18,14,15,16],[14,15,1,-1],[16,17,-2,4],[10,1,11],[4,5,13],[20,19,9,8],[18,17,7,6],[10,9,21],[8,7,22],[6,5,23],[21,22,23,11,-3,13]] 
			cont_order = [5, 7, 14, 15, 10, 20, 19, 1, 9, 13, 23, 6, 22, 18, 8, 11, 21, 16, 4, 17] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 6: 
			connects = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,-1],[10,1,11],[2,3,12],[20,19,9,8],[18,17,7,6],[10,9,21],[8,7,22],[6,-2,23],[21,22,23,11,12,-3]] 
			cont_order = [7, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 18, 8, 17, 11, 21, 12, 22, 6, 23] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 7: 
			connects = [[-1,-2,18,14,15,16],[14,15,1,2],[16,17,3,4],[10,1,11],[2,3,12],[4,5,13],[18,17,7,6],[10,-3,21],[-4,7,22],[6,5,23],[21,22,23,11,12,13]] 
			cont_order = [5, 7, 14, 15, 3, 10, 13, 23, 6, 22, 17, 4, 12, 21, 11, 18, 16, 1, 2] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 8: 
			connects = [[20,19,-1,14,15,16],[14,15,1,2],[16,-2,3,4],[10,1,11],[2,3,12],[4,5,13],[20,19,9,8],[10,9,21],[8,-3,22],[-4,5,23],[21,22,23,11,12,13]] 
			cont_order = [5, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 13, 23, 11, 21, 4, 12, 8, 22] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 9: 
			connects = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,4],[-1,1,11],[2,3,12],[4,5,13],[20,19,-2,8],[18,17,7,6],[8,7,22],[6,5,23],[-3,22,23,11,12,13]] 
			cont_order = [5, 7, 14, 15, 3, 20, 19, 13, 23, 6, 22, 17, 4, 12, 18, 16, 2, 8, 1, 11] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 10: 
			connects = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,4],[10,1,11],[2,3,12],[4,5,13],[20,19,9,-1],[18,17,-2,6],[10,9,21],[6,5,23],[21,-3,23,11,12,13]] 
			cont_order = [5, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 13, 23, 11, 21, 4, 12, 18, 17, 6] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 11: 
			connects = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,4],[10,1,11],[2,3,12],[4,-2,13],[20,19,9,8],[18,17,7,-1],[10,9,21],[8,7,22],[21,22,-3,11,12,13]] 
			cont_order = [7, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 18, 8, 17, 11, 21, 12, 22, 4, 13] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 12: 
			connects = [[20,19,18,14,15,16],[14,15,1,2],[16,17,3,4],[10,1,-4],[2,3,-5],[4,5,-6],[20,19,9,8],[18,17,7,6],[10,9,-1],[8,7,-2],[6,5,-3]] 
			cont_order = [5, 7, 14, 15, 3, 10, 20, 19, 1, 9, 16, 2, 18, 8, 17, 4, 6] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5])],connects,cont_order=cont_order,check_network=False) 
		else: 
			raise ValueError(('requested environment (%i) is out of range for current network; please set "which_env" in range [0-12]')%(which_env)) 


	elif which_network == 2: 
		if which_env == 0: 
			connects = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,11],[17,8,18],[9,10,19],[11,12,20],[1,2,16,15],[3,4,14,13],[17,16,23],[15,14,22],[13,12,21],[23,22,21,18,19,20]] 
			cont_order = [12, 3, 4, 6, 5, 17, 13, 11, 15, 9, 7, 10, 2, 14, 1, 8, 16, 20, 21, 19, 22, 18, 23,] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 1: 
			connects = [[1,-4,8,9],[-5,-6,10,11],[17,8,18],[9,10,19],[11,12,20],[1,-1,16,15],[-2,-3,14,13],[17,16,23],[15,14,22],[13,12,21],[23,22,21,18,19,20]] 
			cont_order = [12, 17, 15, 9, 18, 23, 16, 22, 1, 8, 19, 21, 20, 10, 11, 14, 13] 
			return ncon([tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 2: 
			connects = [[2,3,4,-2,6,5],[6,5,10,11],[17,-3,18],[-4,10,19],[11,12,20],[-1,2,16,15],[3,4,14,13],[17,16,23],[15,14,22],[13,12,21],[23,22,21,18,19,20]] 
			cont_order = [12, 3, 4, 6, 5, 17, 13, 11, 15, 18, 23, 16, 22, 2, 14, 20, 21, 10, 19] 
			return ncon([tensors_in[0],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 3: 
			connects = [[2,3,4,7,-1,-2],[1,7,8,9],[17,8,18],[9,-3,19],[-4,12,20],[1,2,16,15],[3,4,14,13],[17,16,23],[15,14,22],[13,12,21],[23,22,21,18,19,20]] 
			cont_order = [12, 3, 4, 17, 15, 9, 18, 23, 16, 22, 1, 8, 19, 21, 20, 2, 7, 14, 13] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 4: 
			connects = [[2,3,4,7,6,5],[1,7,-2,9],[6,5,10,11],[9,10,19],[11,12,20],[1,2,16,15],[3,4,14,13],[-1,16,23],[15,14,22],[13,12,21],[23,22,21,-3,19,20]] 
			cont_order = [12, 3, 4, 6, 5, 13, 11, 15, 9, 7, 10, 2, 14, 1, 20, 21, 19, 22, 16, 23] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 5: 
			connects = [[2,3,4,7,6,5],[1,7,8,-1],[6,5,-2,11],[17,8,18],[11,12,20],[1,2,16,15],[3,4,14,13],[17,16,23],[15,14,22],[13,12,21],[23,22,21,18,-3,20]] 
			cont_order = [12, 3, 4, 6, 5, 17, 13, 11, 15, 18, 23, 16, 22, 2, 14, 20, 21, 7, 8, 1] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 6: 
			connects = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,-1],[17,8,18],[9,10,19],[1,2,16,15],[3,4,14,13],[17,16,23],[15,14,22],[13,-2,21],[23,22,21,18,19,-3]] 
			cont_order = [3, 4, 6, 5, 17, 15, 9, 18, 23, 16, 22, 1, 8, 19, 2, 7, 14, 10, 13, 21] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 7: 
			connects = [[-2,3,4,7,6,5],[-1,7,8,9],[6,5,10,11],[17,8,18],[9,10,19],[11,12,20],[3,4,14,13],[17,-3,23],[-4,14,22],[13,12,21],[23,22,21,18,19,20]] 
			cont_order = [12, 3, 4, 6, 5, 17, 13, 11, 9, 7, 10, 18, 23, 20, 21, 8, 19, 14, 22] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 8: 
			connects = [[2,-1,-2,7,6,5],[1,7,8,9],[6,5,10,11],[17,8,18],[9,10,19],[11,12,20],[1,2,16,15],[17,16,23],[15,-3,22],[-4,12,21],[23,22,21,18,19,20]] 
			cont_order = [12, 17, 15, 9, 18, 23, 16, 22, 1, 8, 19, 21, 20, 10, 11, 2, 7, 6, 5] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 9: 
			connects = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,11],[-1,8,18],[9,10,19],[11,12,20],[1,2,-2,15],[3,4,14,13],[15,14,22],[13,12,21],[-3,22,21,18,19,20]] 
			cont_order = [12, 3, 4, 6, 5, 13, 11, 15, 9, 7, 10, 2, 14, 1, 20, 21, 19, 22, 8, 18] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[4]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 10: 
			connects = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,11],[17,8,18],[9,10,19],[11,12,20],[1,2,16,-1],[3,4,-2,13],[17,16,23],[13,12,21],[23,-3,21,18,19,20]] 
			cont_order = [12, 3, 4, 6, 5, 17, 13, 11, 9, 7, 10, 18, 23, 20, 21, 8, 19, 2, 1, 16] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[5]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 11: 
			connects = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,11],[17,8,18],[9,10,19],[11,-2,20],[1,2,16,15],[3,4,14,-1],[17,16,23],[15,14,22],[23,22,-3,18,19,20]] 
			cont_order = [3, 4, 6, 5, 17, 15, 9, 18, 23, 16, 22, 1, 8, 19, 2, 7, 14, 10, 11, 20] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),tensors_in[6]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 12: 
			connects = [[2,3,4,7,6,5],[1,7,8,9],[6,5,10,11],[17,8,-4],[9,10,-5],[11,12,-6],[1,2,16,15],[3,4,14,13],[17,16,-1],[15,14,-2],[13,12,-3]] 
			cont_order = [12, 3, 4, 6, 5, 17, 13, 11, 15, 9, 7, 10, 2, 14, 1, 8, 16] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[2],tensors_in[3],tensors_in[4],tensors_in[5],np.conj(tensors_in[1]),np.conj(tensors_in[2]),np.conj(tensors_in[3]),np.conj(tensors_in[4]),np.conj(tensors_in[5])],connects,cont_order=cont_order,check_network=False) 
		else: 
			raise ValueError(('requested environment (%i) is out of range for current network; please set "which_env" in range [0-12]')%(which_env)) 


	elif which_network == 3: 
		raise ValueError(('selected network (%i) is invalid: network is empty.')%(which_network)) 

	elif which_network == 4: 
		raise ValueError(('selected network (%i) is invalid: network is empty.')%(which_network)) 

	else: 
		raise ValueError('requested network is out of range; please set "which_network" in range [1-4].') 


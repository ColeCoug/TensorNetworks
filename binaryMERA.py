# binaryMERA.py 
import numpy as np 
from ncon import ncon 

def binaryMERA(tensors_in, which_network=None, which_env=0): 
	""" 
Auto-generated network contraction function from 'TensorTrace' software, 
see (www.tensortrace.com) for details, (c) Glen Evenbly, 2019. 
Requires the network contraction routine 'ncon' to be in the working directory, 
(included in the TensorTrace install directory, or also found at 'www.tensortrace.com'). 
------------------------------- 
Input variables: 
------------------------------- 
1st input 'tensors_in' is a list of the unique tensors: tensors_in = [uDis, wIso, hamThree, rhoThree] 
2nd input 'which_network' dictates which network to evaluate (1-4) 
3rd input 'which_env' allows one to specify a tensor environment to evaluate from a closed tensor network. 
	 -set 'which_env = 0' to evaluate the scalar from a closed network (i.e. no environment). 
	 -set 'which_env = n' to evaluate environment of the nth tensor from the closed network. 
""" 

	# General project info: 
	# ------------------------------- 
	# Generated on: 16/9/2019
	# Generated from: C:\Users\gevenbly3\Dropbox\Gamemaker\Saves\Included\binaryMERA.ttp
	# Index dims: chi = 6, chi_p = 4, Ind3 = 2, Ind4 = 2; 
 
	# --- Info for Network-1 --- 
	# -------------------------- 
	# network is CLOSED 
	# total contraction cost (in scalar multiplications): 4.58*10^6
	# contraction order: (((((((T1*T3)*(T2*(T6*T8)))*T7)*T9)*(T5*T11))*(T4*T10))*T12)
	# 1st leading order cost: (chi^4)*(chi_p^5)
	# 2nd leading order cost: (chi^3)*(chi_p^6)
	tensors_N1 = [uDis,uDis,wIso,wIso,wIso,hamThree,np.conj(uDis),np.conj(uDis),np.conj(wIso),np.conj(wIso),np.conj(wIso),rhoThree]
	connects_N1 = [[1,2,17,16],[4,6,15,14],[16,15,22],[8,17,21],[14,13,23],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,12],[10,11,19],[8,9,18],[12,13,20],[18,19,20,21,22,23]]
	dims_N1 = [[chi,chi,chi_p,chi_p],[chi,chi,chi_p,chi_p],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi,chi,chi,chi,chi,chi],[chi,chi,chi_p,chi_p],[chi,chi,chi_p,chi_p],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi,chi,chi,chi,chi,chi]]
	cont_order_N1 = [5, 7, 13, 4, 6, 16, 2, 15, 1, 3, 11, 10, 14, 12, 8, 17, 9, 22, 19, 23, 20, 21, 18,];

	# --- Info for Network-2 --- 
	# -------------------------- 
	# network is CLOSED 
	# total contraction cost (in scalar multiplications): 4.58*10^6
	# contraction order: ((((((((T1*T6)*T7)*(T2*T3))*T8)*T9)*(T4*T10))*(T5*T11))*T12)
	# 1st leading order cost: (chi^4)*(chi_p^5)
	# 2nd leading order cost: (chi^3)*(chi_p^6)
	# tensors_N2 = [uDis,uDis,wIso,wIso,wIso,hamThree,np.conj(uDis),np.conj(uDis),np.conj(wIso),np.conj(wIso),np.conj(wIso),rhoThree] 
	# connects_N2 = [[1,3,16,15],[5,20,14,13],[15,14,22],[7,16,23],[13,12,21],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,11],[9,10,18],[7,8,17],[11,12,19],[17,18,19,23,22,21]] 
	# dims_N2 = [[chi,chi,chi_p,chi_p],[chi,chi,chi_p,chi_p],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi,chi,chi,chi,chi,chi],[chi,chi,chi_p,chi_p],[chi,chi,chi_p,chi_p],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi_p,chi_p,chi],[chi,chi,chi,chi,chi,chi]] 
	# cont_order_N2 = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 7, 16, 8, 12, 13, 11, 22, 18, 23, 17, 21, 19,]; 

	# --- Info for Network-3 --- 
	# -------------------------- 
	# -- Network is empty. -- 

	# --- Info for Network-4 --- 
	# -------------------------- 
	# -- Network is empty. -- 


	# Contraction Code: 
	# ------------------------------- 

	if len(tensors_in) == 0: # auto-generate random tensors of default dims 
		chi = 6 
		chi_p = 4 
		Ind3 = 2 
		Ind4 = 2 
		all_dims = [[chi,chi,chi_p,chi_p],[chi_p,chi_p,chi],[chi,chi,chi,chi,chi,chi],[chi,chi,chi,chi,chi,chi]]; 
		tensors_in = [0 for x in range(len(all_dims))] 
		for k in range(len(all_dims)): 
			tensors_in[k] = np.random.rand(*all_dims[k]) 


	if which_network == 1: 
		if which_env == 0: 
			connects = [[1,2,17,16],[4,6,15,14],[16,15,22],[8,17,21],[14,13,23],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,12],[10,11,19],[8,9,18],[12,13,20],[18,19,20,21,22,23]] 
			cont_order = [5, 7, 13, 4, 6, 16, 2, 15, 1, 3, 11, 10, 14, 12, 8, 17, 9, 22, 19, 23, 20, 21, 18,] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 1: 
			connects = [[4,6,15,14],[-4,15,22],[8,-3,21],[14,13,23],[3,5,7,-2,4,6],[-1,3,9,10],[5,7,11,12],[10,11,19],[8,9,18],[12,13,20],[18,19,20,21,22,23]] 
			cont_order = [5, 7, 13, 4, 6, 8, 21, 18, 20, 23, 19, 9, 10, 14, 3, 11, 12, 15, 22] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 2: 
			connects = [[1,2,17,16],[16,-3,22],[8,17,21],[-4,13,23],[3,5,7,2,-1,-2],[1,3,9,10],[5,7,11,12],[10,11,19],[8,9,18],[12,13,20],[18,19,20,21,22,23]] 
			cont_order = [5, 7, 13, 16, 8, 21, 18, 20, 23, 19, 9, 10, 1, 17, 22, 2, 12, 11, 3] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 3: 
			connects = [[1,2,17,-1],[4,6,-2,14],[8,17,21],[14,13,23],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,12],[10,11,19],[8,9,18],[12,13,20],[18,19,20,21,-3,23]] 
			cont_order = [5, 7, 13, 4, 6, 8, 21, 18, 20, 23, 19, 9, 10, 14, 3, 11, 12, 1, 2, 17] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 4: 
			connects = [[1,2,-2,16],[4,6,15,14],[16,15,22],[14,13,23],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,12],[10,11,19],[-1,9,18],[12,13,20],[18,19,20,-3,22,23]] 
			cont_order = [5, 7, 13, 4, 6, 16, 2, 15, 1, 3, 11, 10, 14, 12, 22, 19, 23, 20, 9, 18] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 5: 
			connects = [[1,2,17,16],[4,6,15,-1],[16,15,22],[8,17,21],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,12],[10,11,19],[8,9,18],[12,-2,20],[18,19,20,21,22,-3]] 
			cont_order = [5, 7, 4, 6, 16, 2, 15, 1, 3, 11, 10, 8, 21, 18, 17, 22, 9, 19, 12, 20] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 6: 
			connects = [[1,-4,17,16],[-5,-6,15,14],[16,15,22],[8,17,21],[14,13,23],[1,-1,9,10],[-2,-3,11,12],[10,11,19],[8,9,18],[12,13,20],[18,19,20,21,22,23]] 
			cont_order = [13, 16, 8, 21, 18, 20, 23, 19, 9, 10, 1, 17, 22, 15, 14, 12, 11] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 7: 
			connects = [[-1,2,17,16],[4,6,15,14],[16,15,22],[8,17,21],[14,13,23],[-2,5,7,2,4,6],[5,7,11,12],[-4,11,19],[8,-3,18],[12,13,20],[18,19,20,21,22,23]] 
			cont_order = [5, 7, 13, 4, 6, 16, 2, 15, 8, 21, 18, 20, 23, 19, 17, 22, 14, 11, 12] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 8: 
			connects = [[1,2,17,16],[4,6,15,14],[16,15,22],[8,17,21],[14,13,23],[3,-1,-2,2,4,6],[1,3,9,10],[10,-3,19],[8,9,18],[-4,13,20],[18,19,20,21,22,23]] 
			cont_order = [13, 16, 8, 21, 18, 20, 23, 19, 9, 10, 1, 17, 22, 15, 14, 2, 3, 4, 6] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 9: 
			connects = [[1,2,17,16],[4,6,15,14],[16,15,22],[8,17,21],[14,13,23],[3,5,7,2,4,6],[1,3,9,-1],[5,7,-2,12],[8,9,18],[12,13,20],[18,-3,20,21,22,23]] 
			cont_order = [5, 7, 13, 4, 6, 16, 2, 15, 1, 3, 8, 21, 18, 20, 23, 17, 22, 14, 12, 9] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 10: 
			connects = [[1,2,17,16],[4,6,15,14],[16,15,22],[-1,17,21],[14,13,23],[3,5,7,2,4,6],[1,3,-2,10],[5,7,11,12],[10,11,19],[12,13,20],[-3,19,20,21,22,23]] 
			cont_order = [5, 7, 13, 4, 6, 16, 2, 15, 1, 3, 11, 10, 14, 12, 22, 19, 23, 20, 17, 21] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 11: 
			connects = [[1,2,17,16],[4,6,15,14],[16,15,22],[8,17,21],[14,-2,23],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,-1],[10,11,19],[8,9,18],[18,19,-3,21,22,23]] 
			cont_order = [5, 7, 4, 6, 16, 2, 15, 1, 3, 11, 10, 8, 21, 18, 17, 22, 9, 19, 14, 23] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 12: 
			connects = [[1,2,17,16],[4,6,15,14],[16,15,-5],[8,17,-4],[14,13,-6],[3,5,7,2,4,6],[1,3,9,10],[5,7,11,12],[10,11,-2],[8,9,-1],[12,13,-3]] 
			cont_order = [5, 7, 13, 4, 6, 16, 2, 15, 1, 3, 11, 10, 14, 12, 8, 17, 9] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1])],connects,cont_order=cont_order,check_network=False) 
		else: 
			raise ValueError(('requested environment (%i) is out of range for current network; please set "which_env" in range [0-12]')%(which_env)) 


	elif which_network == 2: 
		if which_env == 0: 
			connects = [[1,3,16,15],[5,20,14,13],[15,14,22],[7,16,23],[13,12,21],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,11],[9,10,18],[7,8,17],[11,12,19],[17,18,19,23,22,21]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 7, 16, 8, 12, 13, 11, 22, 18, 23, 17, 21, 19,] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 1: 
			connects = [[5,20,14,13],[-4,14,22],[7,-3,23],[13,12,21],[2,4,6,-1,-2,5],[2,4,8,9],[6,20,10,11],[9,10,18],[7,8,17],[11,12,19],[17,18,19,23,22,21]] 
			cont_order = [14, 7, 12, 21, 19, 23, 17, 18, 11, 10, 20, 13, 22, 8, 9, 5, 6, 2, 4] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 2: 
			connects = [[1,3,16,15],[15,-3,22],[7,16,23],[-4,12,21],[2,4,6,1,3,-1],[2,4,8,9],[6,-2,10,11],[9,10,18],[7,8,17],[11,12,19],[17,18,19,23,22,21]] 
			cont_order = [1, 3, 2, 4, 7, 12, 21, 19, 23, 17, 18, 11, 10, 16, 6, 8, 9, 15, 22] 
			return ncon([tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 3: 
			connects = [[1,3,16,-1],[5,20,-2,13],[7,16,23],[13,12,21],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,11],[9,10,18],[7,8,17],[11,12,19],[17,18,19,23,-3,21]] 
			cont_order = [1, 3, 2, 4, 7, 12, 21, 19, 23, 17, 18, 11, 10, 16, 6, 8, 9, 5, 13, 20] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 4: 
			connects = [[1,3,-2,15],[5,20,14,13],[15,14,22],[13,12,21],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,11],[9,10,18],[-1,8,17],[11,12,19],[17,18,19,-3,22,21]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 12, 21, 19, 13, 22, 11, 18, 8, 17] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 5: 
			connects = [[1,3,16,15],[5,20,14,-1],[15,14,22],[7,16,23],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,11],[9,10,18],[7,8,17],[11,-2,19],[17,18,19,23,22,-3]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 7, 16, 8, 22, 18, 23, 17, 11, 19] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 6: 
			connects = [[-4,-5,16,15],[-6,20,14,13],[15,14,22],[7,16,23],[13,12,21],[-1,-2,8,9],[-3,20,10,11],[9,10,18],[7,8,17],[11,12,19],[17,18,19,23,22,21]] 
			cont_order = [14, 7, 12, 21, 19, 23, 17, 18, 11, 10, 20, 13, 22, 8, 9, 16, 15] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 7: 
			connects = [[1,3,16,15],[5,20,14,13],[15,14,22],[7,16,23],[13,12,21],[-1,-2,6,1,3,5],[6,20,10,11],[-4,10,18],[7,-3,17],[11,12,19],[17,18,19,23,22,21]] 
			cont_order = [14, 1, 3, 7, 12, 21, 19, 23, 17, 18, 11, 10, 20, 13, 22, 16, 15, 6, 5] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 8: 
			connects = [[1,3,16,15],[5,-2,14,13],[15,14,22],[7,16,23],[13,12,21],[2,4,-1,1,3,5],[2,4,8,9],[9,-3,18],[7,8,17],[-4,12,19],[17,18,19,23,22,21]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 7, 12, 21, 19, 23, 17, 18, 16, 8, 9, 13, 22] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 9: 
			connects = [[1,3,16,15],[5,20,14,13],[15,14,22],[7,16,23],[13,12,21],[2,4,6,1,3,5],[2,4,8,-1],[6,20,-2,11],[7,8,17],[11,12,19],[17,-3,19,23,22,21]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 7, 12, 21, 19, 23, 17, 16, 8, 13, 22, 11] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 10: 
			connects = [[1,3,16,15],[5,20,14,13],[15,14,22],[-1,16,23],[13,12,21],[2,4,6,1,3,5],[2,4,-2,9],[6,20,10,11],[9,10,18],[11,12,19],[-3,18,19,23,22,21]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 12, 21, 19, 13, 22, 11, 18, 16, 23] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 11: 
			connects = [[1,3,16,15],[5,20,14,13],[15,14,22],[7,16,23],[13,-2,21],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,-1],[9,10,18],[7,8,17],[17,18,-3,23,22,21]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 7, 16, 8, 22, 18, 23, 17, 13, 21] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),tensors_in[3]],connects,cont_order=cont_order,check_network=False) 
		elif which_env == 12: 
			connects = [[1,3,16,15],[5,20,14,13],[15,14,-5],[7,16,-4],[13,12,-6],[2,4,6,1,3,5],[2,4,8,9],[6,20,10,11],[9,10,-2],[7,8,-1],[11,12,-3]] 
			cont_order = [14, 1, 3, 2, 4, 15, 5, 6, 20, 9, 10, 7, 16, 8, 12, 13, 11] 
			return ncon([tensors_in[0],tensors_in[0],tensors_in[1],tensors_in[1],tensors_in[1],tensors_in[2],np.conj(tensors_in[0]),np.conj(tensors_in[0]),np.conj(tensors_in[1]),np.conj(tensors_in[1]),np.conj(tensors_in[1])],connects,cont_order=cont_order,check_network=False) 
		else: 
			raise ValueError(('requested environment (%i) is out of range for current network; please set "which_env" in range [0-12]')%(which_env)) 


	elif which_network == 3: 
		raise ValueError(('selected network (%i) is invalid: network is empty.')%(which_network)) 

	elif which_network == 4: 
		raise ValueError(('selected network (%i) is invalid: network is empty.')%(which_network)) 

	else: 
		raise ValueError('requested network is out of range; please set "which_network" in range [1-4].') 


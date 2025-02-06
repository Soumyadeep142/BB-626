from numpy import *
from matplotlib.pyplot import *


k_on=10
k_off=7

ensembles=50
iteration=10000
k_tot=k_on+k_off
P_on=k_on/k_tot
P_off=k_off/k_tot
L_points_all=[]
t_points_all=[]
for e in range(ensembles):
	print(e)
	t=0
	L=2
	L_points=[L]
	t_points=[t]
	for i in range(iteration):
		A=random.uniform()
		if A<P_on:
			L=L+1
		else:
			L=L-1
		B=random.uniform()
		delt=-1/k_tot*log(B)
		t+=delt
		L_points.append(L)
		t_points.append(t)
	L_points_all.append(L_points)
	t_points_all.append(t_points)
	#plot(t_points, L_points)

#xlabel('time')
#ylabel('Length')
#show()
	
max_t=max([max(i) for i in t_points_all])
t_points_range=arange(0,max_t,1)
sig_sq_array=[]
for t in t_points_range:
	L_points_time=[]
	for (L,i) in zip(L_points_all, t_points_all):
		for (o,m) in zip(L,i):
			A1=m-t
			if A1<=0:
				L_fin=o
		L_points_time.append(L_fin)
	L_points_time_sq=[l**2 for l in L_points_time]
	sig_sq=mean(L_points_time_sq)-(mean(L_points_time))**2
	sig_sq_array.append(sig_sq)
print(sig_sq_array)
scatter(t_points_range, sig_sq_array)
show()
			
			
#Soumyadeep Kundu-24D1064

from numpy import *
from matplotlib.pyplot import *


kf=10
kr=5
L_ini=100

ensembles=100
iteration=2500
k_tot=kf+kr
P_on=kf/k_tot
P_off=kr/k_tot
L_points_all=[]
t_points_all=[]
for e in range(ensembles):
	#print(e)
	t=0
	L=L_ini
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
	plot(t_points, L_points)

xlabel('time')
ylabel('Length')
title("Polymer length")
savefig('Ensembles.pdf')

clf()
	
max_t=min([max(i) for i in t_points_all])
t_points_range=arange(0,max_t,1)
sig_sq_array=[]
L_point_array=[]
for t in t_points_range:
	L_points_time=[]
	for (L,i) in zip(L_points_all, t_points_all):
		for (o,m) in zip(L,i):
			A1=m-t
			if A1<=0:
				L_fin=o
		L_points_time.append(L_fin)
	L_point_array.append(mean(L_points_time))
	L_points_time_sq=[l**2 for l in L_points_time]
	sig_sq=mean(L_points_time_sq)-(mean(L_points_time))**2
	sig_sq_array.append(sig_sq)

scatter(t_points_range, sig_sq_array)
x_points=arange(0, max_t, 1)
y_points=[(kf+kr)*x+L_ini for x in x_points]
plot(x_points, y_points, color='red')
text(120, 1000, fr"slope=$k_f+k_r$={kf+kr}")
title("Variance of Polymer length")
xlabel('Time')
ylabel(r"$\sigma^2$")

savefig("Sigma.pdf")
clf()

scatter(t_points_range, L_point_array)
x_points=arange(0, max_t, 1)
y_points=[(kf-kr)*x+L_ini for x in x_points]
plot(x_points, y_points, color='red')
text(120, 400, f"slope=$k_f-k_r$={kf-kr}")
xlabel('Time')
ylabel(r"$<l>$")
title("Average Polymer length")
savefig("Avg_Length.pdf")
			
			
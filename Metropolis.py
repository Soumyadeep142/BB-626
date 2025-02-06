#Soumyadeep_Kundu
#24D1064

from numpy import *
from matplotlib.pyplot import *

def Energy(J, h, i, j):
	return -J*i*j-h*i
J_range=[1, 1, 10, 1]
h_range=[1, 0.1, 1, -1]
N=100
MC_Steps=2000
no=0
figure(figsize=(20,16))
suptitle("Periodic Ising model")
for (J,h) in zip(J_range, h_range):
	no+=1
	S_range=[]
	for i in range(N):
		S_range.append(random.choice([1, -1]))
	E_old=0
	for i in range(N):
		j=(i+1)%N
		E_old+=Energy(J, h, S_range[i], S_range[j])
	MC_Energy=[]
	MC_Steps_range=[]
	for k in range(MC_Steps):
		for i in range(N):
			E=0
			A=random.randint(0,N)
			S_range[A]=S_range[A]*(-1)
			for l in range(N):
				m=(l+1)%N
				E+=Energy(J, h, S_range[l],S_range[m])
			delE=E-E_old
			if delE>0:
				r=random.random()
				p=exp(-delE)
				if r>p:
					S_range[A]=S_range[A]*(-1)
				else:
					E_old=E
			else:
				E_old=E
		MC_Energy.append(E_old)
		MC_Steps_range.append(k)
	subplot(2, 2, no)
	plot(MC_Steps_range, MC_Energy)
	title(f'J={J}, h={h}')
	xlabel("Monte-Carlo Steps")
	ylabel("Energy")
savefig("Energy_MC_Steps.pdf")





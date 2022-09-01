import os
import scipy.io as sio
from os.path import join as pjoin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


f_data4 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_FULL_RECORD_ts.mat')
mat_trn = sio.loadmat(f_data4)
sorted(mat_trn.keys())
f_data1 = pjoin('/Users/qi/Dropbox/Results_chapter1/ORAS5_LF_SECS_SSH.mat')
mat_oras5 = sio.loadmat(f_data1)
sorted(mat_oras5.keys())
nemo_trn = mat_trn['secs_trns']
oras5_trn = mat_oras5['ts_vol']



#Ttick=['58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']

#Ttick_oras5=['75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
     
    
fig = plt.figure(figsize=[45, 20])
fig.subplots_adjust(left=0.005,
                    bottom=0.05, 
                    right=0.5, 
                    top=0.6, hspace=0.2, wspace=0.05)
ax = fig.add_subplot(111)  

T_nemo=np.arange(1958, 2016.1, 2)
#---------------------------------------------------------------------   
for n in range(0,10,1):
    if n==0:
        m=n+1
        ax_current = plt.subplot(5,2, m)
        ax_current.set_ylabel("VF (Sv)")
    if n>0 and n<5:
        m=n+1+n
        ax_current = plt.subplot(5,2, m)
        ax_current.set_ylabel("VF (Sv)")
    if n==5:
        m=2
        ax_current = plt.subplot(5,2, m)
    if n==6:
        m=4
        ax_current = plt.subplot(5,2, m)
    if n==7:
        m=6
        ax_current = plt.subplot(5,2, m)
    if n==8:
        m=8
        ax_current = plt.subplot(5,2, m)
    if n==9:
        m=10
        ax_current = plt.subplot(5,2, m)
    ax_current.plot(np.arange(1958,2016,1/12),nemo_trn[:,n], "k-", label="NEMO")
    ax_current.plot(np.arange(1975,2015,1/12),oras5_trn[:,n], "b-", label="ORAS5")
    ax_current.set_ylim(0,4)
    plt.xlim(1958, 2016)
    ax_current.set_title('('+str(n+1)+')', pad=7)
#   ax_current.legend(loc="upper right")
    ax_current.set_xticks(T_nemo)
    #ax_current.set_xticklabels(Ttick)  
    if m<9:
        plt.setp(ax_current,xticklabels=[])
    if m==8:
        ax_current.set_ylim(0,15)
    if m==10:
        ax_current.set_ylim(0,25)
    if m>8:
        ax_current.set_xlabel("Year")
            
            

fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup05.png',dpi=150, bbox_inches ='tight')

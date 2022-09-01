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


nemo_lf_vol = mat_trn['lf_vol_hy']
#oras5_lf_vol = mat_oras5['lf_vol_hy']
#nemo_lf_bp=mat_trn['lf_bp_hy']
#nemo_lf_sth=mat_trn['lf_sth_hy']

#nemo_lf_ssh = 100*mat_trn['lf_ssh_hy']
#oras5_lf_ssh = 100*mat_oras5['lf_ssh_hy']


#-----------------------------------------------------------------
f_data2 = pjoin('/Users/qi/Dropbox/Results_chapter1/TWOSAT_VF_FROM_NEMO_withoutb.mat')
mat_vari2 = sio.loadmat(f_data2)
sorted(mat_vari2.keys())

al_nemo = mat_vari2['lf_vf_fromnemo']
#al_ssh = mat_vari2['lf_ssh_hy']

f_data3 = pjoin('/Users/qi/Dropbox/Results_chapter1/VF_FROM_ORAS5_withoutb.mat')
mat_vari3 = sio.loadmat(f_data3)
sorted(mat_vari3.keys())
al_oras5 = mat_vari3['lf_oras5vol_hy']



f_data5 = pjoin('/Users/qi/Dropbox/Results_chapter1/ORAS5_EXTEND_VOL.mat')
mat_vari5 = sio.loadmat(f_data5)
sorted(mat_vari5.keys())
oras5_full = mat_vari5['lf_extend']
#---------------------------------------------------------------
#jpl and all satellites by nemo 
f_data6 = pjoin('/Users/qi/Dropbox/Results_chapter1/ALLSAT_VF_FROM_NEMO_withoutb.mat')
mat_vari6 = sio.loadmat(f_data6)
sorted(mat_vari6.keys())

allsat_nemo = mat_vari6['lf_allsat_bynemo']
#al_ssh = mat_vari2['lf_ssh_hy']

f_data7 = pjoin('/Users/qi/Dropbox/Results_chapter1/JPL_VF_FROM_NEMO_withoutb.mat')
mat_vari7 = sio.loadmat(f_data7)
sorted(mat_vari7.keys())
jpl_nemo = mat_vari7['lf_jpl_bynemo']

#-----------------------------------------------------------
#jpl and all satellites by oras5
f_data8 = pjoin('/Users/qi/Dropbox/Results_chapter1/ALLSAT_VF_FROM_ORAS5_withoutb.mat')
mat_vari8 = sio.loadmat(f_data8)
sorted(mat_vari8.keys())

allsat_oras5 = mat_vari8['lf_recon_alsat']
#al_ssh = mat_vari2['lf_ssh_hy']

f_data9 = pjoin('/Users/qi/Dropbox/Results_chapter1/JPL_VF_FROM_ORAS5_withoutb.mat')
mat_vari9 = sio.loadmat(f_data9)
sorted(mat_vari9.keys())
jpl_oras5 = mat_vari9['lf_recon_jpl']

#Ttick=['58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']

#Ttick_oras5=['75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
   


rdln=np.full([100],np.nan)
rdln_x=np.full([100],np.nan)
for n in range(100):
    rdln[n]=n/3
    rdln_x[n]=1975
   
fig = plt.figure(figsize=[50, 20])
fig.subplots_adjust(left=0.005,
                    bottom=0.05, 
                    right=0.5, 
                    top=0.6, hspace=0.2, wspace=0.05)
ax = fig.add_subplot(111)  

T_nemo=np.arange(1993, 2022.1, 1)
#---------------------------------------------------------------------   
for n in range(0,10,1):
    if n==0:
        m=n+1
        ax_current = plt.subplot(5,2, m)
        ax_current.set_ylabel("VF (Sv)")
        #ax_current.set_ylim(-0.1,1)
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
    #ax_current.plot(np.arange(1958.5,2015.5,1/12),nemo_lf_vol[:,n], "k-")
    #ax_current.plot(np.arange(1958.5,2014.5,1/12),oras5_full[:,n], "b-")
    ax_current.plot(np.arange(1993.5,2021.1,1/12),al_nemo[:,n], "orange")
    #ax_current.plot(np.arange(1993.5,2021.1,1/12),al_oras5[:,n], "gold",label='Two-sat by oras5')
    ax_current.plot(np.arange(1993.5,2021.05,1/12),allsat_nemo[:,n], "g-")
    #ax_current.plot(np.arange(1993.5,2021.05,1/12),allsat_oras5[:,n], "skyblue",label='All-sat by oras5')
    ax_current.plot(np.arange(1993.5,2021.51,1/12),jpl_nemo[:,n], "orchid")
    #ax_current.plot(np.arange(1993.5,2021.05,1/12),allsat_oras5[:,n], "skyblue",laebl='cnes by oras5')
    #ax_current.plot(np.arange(1993.5,2021.51,1/12),jpl_oras5[:,n], "plum",label='jpl by oras5')
    #ax_current.plot(rdln_x,rdln,'--k',linewidth=1)
    plt.xlim(1993, 2022)
    ax_current.legend(loc="upper left",prop={'size': 6})
    ax_current.set_title('('+str(n+1)+')', pad=7)
    ax_current.set_xticks(T_nemo)

    #ax_current.set_xticklabels(Ttick)  
    if m<9:
        plt.setp(ax_current,xticklabels=[])
    #if m==8:
        #ax_current.set_ylim(2,7)
    #if m==10:
        #ax_current.set_ylim(2,7)#
    if m>8:
        ax_current.set_xlabel("Year")
            
            

fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/fig06.png',dpi=150, bbox_inches ='tight')
    


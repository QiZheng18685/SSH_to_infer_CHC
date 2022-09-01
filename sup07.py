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




f_data2 = pjoin('/Users/qi/Dropbox/Results_chapter1/ORAS5_RECON_VOL')
mat_oras2 = sio.loadmat(f_data2)
sorted(mat_oras2.keys())


oras5_lf_vol = mat_oras5['ts_vol']
oras5_lf_ssh = 100*mat_oras5['ts_ssh']
oras5_recon=mat_oras2['vf_ssh']

#Ttick=['58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']

#Ttick_oras5=['75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
    
T_oras=np.arange(1975, 2015.1, 2)
T_nemo=np.arange(1975, 2015.1, 2)        
    
fig = plt.figure(figsize=[18,15],constrained_layout=True)
plt.clf()
widths = [4]
heights = [2, 2, 2, 2, 2, 2, 2 , 2 , 2, 2]
spec5 = fig.add_gridspec(ncols=1, nrows=10, width_ratios=widths,
                        height_ratios=heights, wspace=0.001) 

ax_current = fig.add_subplot(spec5[0,0])
#---------------------------------------------------------------------   

twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,0], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,0], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,0], "b-", label="NEMO SSH diff")

#p3, = ax_current.plot(np.arange(1993.5,2021.05,1/12),al_nemo[:,0], "g-", label="reconstructed VF")
#p4, = twin1.plot(np.arange(1993.5,2021.1,1/12),al_ssh[:,0], "b--", label="altimetry SSH diff")
#ax_current.legend(loc="upper left")
#twin1.legend(loc="upper right")
#p3, = twin2.plot(np.arange(1958.5,2015.5,1/12),nemo_lf_bp[:,0], "g-", label="filtered ssh")
#twin2.spines.right.set_position(("axes", 1.1))
#twin2.set_ylabel("BP")
#twin2.yaxis.label.set_color(p3.get_color())
ax_current.set_ylim(-0.5, 3)
twin1.set_ylim(-2,9)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#twin2.yaxis.label.set_color(p3.get_color())
tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax_current.set_title('(a) Transect 1', pad=7)
#ax_current.xaxis.set_visible(False)
plt.setp(ax_current,xticklabels=[])

#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
      
ax_current = fig.add_subplot(spec5[1,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,1], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,1], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,1], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(-0.5, 3)
twin1.set_ylim(-2,9)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")

ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#twin2.yaxis.label.set_color(p3.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax_current.set_title('(b) Transect 2', pad=7)
plt.setp(ax_current,xticklabels=[])
#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------



ax_current = fig.add_subplot(spec5[2,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,2], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,2], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,2], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(-0.5, 3)
twin1.set_ylim(-2,9)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")

ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#twin2.yaxis.label.set_color(p3.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax_current.set_title('(c) Transect 3', pad=7)
plt.setp(ax_current,xticklabels=[])
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#-----------------------------------7-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[3,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,3], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,3], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,3], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(0, 3)
twin1.set_ylim(0,13)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")

ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
##twin2.yaxis.label.set_color(p3.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax_current.set_title('(d) Transect 4', pad=7)
plt.setp(ax_current,xticklabels=[])
#----------------------------------------------------------------------------------------
#-----------------------------------8----------------------------------------------


#-------------------------------------------------------------------------------------

ax_current = fig.add_subplot(spec5[4,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,4], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,4], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,4], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(0, 3)
twin1.set_ylim(2,15)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")
plt.xlim(1975, 2015)
plt.xticks(np.arange(1985,2015,2))
ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#twin2.yaxis.label.set_color(p3.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
plt.setp(ax_current,xticklabels=[])
ax_current.set_title('(e) Transect 5', pad=7)

#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------

#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[5,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,5], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,5], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,5], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(0.5, 3)
twin1.set_ylim(2,17)

ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")

ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
#twin2.yaxis.label.set_color(p3.get_color())
plt.setp(ax_current,xticklabels=[])

ax_current.set_title('(f) Transect 6', pad=7)


#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------



ax_current = fig.add_subplot(spec5[6,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,6], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,6], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,6], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(0.5, 3)
twin1.set_ylim(2,17)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")

ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
#twin2.yaxis.label.set_color(p3.get_color())
plt.setp(ax_current,xticklabels=[])
ax_current.set_title('(g) Transect 7', pad=7)


#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------

#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[7,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,7], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,7], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,7], "b-", label="NEMO SSH diff")

#p
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.set_ylim(0.5, 3.5)
twin1.set_ylim(2,17)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")
#twin2.set_ylabel("STH")

ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#twin2.yaxis.label.set_color(p3.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)

plt.setp(ax_current,xticklabels=[])
ax_current.set_title('(h) Transect 8 ', pad=7)
#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------

    
ax_current = fig.add_subplot(spec5[8,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,8], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,8], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,8], "b-", label="NEMO SSH diff")

ax_current.set_ylim(0,15)
twin1.set_ylim(3,35)
#twin2.set_ylabel("STH")
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
#twin2.yaxis.label.set_color(p3.get_color())
plt.setp(ax_current,xticklabels=[])
ax_current.set_title('(i) Transect 9', pad=7)
#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------
#---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
      
ax_current = fig.add_subplot(spec5[9,0])
twin1 = ax_current.twinx()
#twin2 = ax_current.twinx()
p1, = ax_current.plot(np.arange(1975,2015,1/12),oras5_lf_vol[:,9], "k-", label="NEMO VF")
p2, = ax_current.plot(np.arange(1975,2015,1/12),oras5_recon[:,9], "g-", label="Recon VF")
p3, = twin1.plot(np.arange(1975,2015,1/12),oras5_lf_ssh[:,9], "b-", label="NEMO SSH diff")

ax_current.set_ylim(0,30)
twin1.set_ylim(3,40)
ax_current.set_ylabel("VF (Sv)")
twin1.set_ylabel("SSH diff (cm)")
#twin2.set_ylabel("STH")
plt.xlim(1975, 2015)
plt.xticks(np.arange(1975,2015,2))
plt.xticks(T_nemo)
ax_current.yaxis.label.set_color(p1.get_color())
#twin1.yaxis.label.set_color(p2.get_color())
#tkw = dict(size=4, width=1.5)
#twin1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#twin2.tick_params(axis='y', colors=p3.get_color(), **tkw)
#twin2.yaxis.label.set_color(p3.get_color())
#plt.setp(ax_current,xticklabels=[])
ax_current.set_title('(j) Transect 10', pad=7)
  

ax_current.set_xlabel("Year")

# =============================================================================
fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup07.png',dpi=150, bbox_inches ='tight')
# =============================================================================








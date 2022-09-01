#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:27:06 2022

@author: qi
"""



import os
import scipy.io as sio
from os.path import join as pjoin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#---------------------------------------------------------------------
#load NEMO data
#----------------------------------------------------------------------
f_data1 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/NEMO_SSH.mat')
mat_vari1 = sio.loadmat(f_data1)
sorted(mat_vari1.keys())
ssh = 100*mat_vari1['ssh_mn']
#---------------------------------------------------------------------
#load U and V and current speed 

f_data2 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_AVGCHC_SPEED.mat')
mat_vari2 = sio.loadmat(f_data2)
sorted(mat_vari2.keys())
vmag = mat_vari2['avg_spe_mn']

f_data3 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/bathymetry_ORCA12.mat')
mat_vari3 = sio.loadmat(f_data3)
sorted(mat_vari3.keys())
bathy = mat_vari3['bathy']

f_data4 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/NEMO_SECS_LONLAT.mat')
mat_vari4 = sio.loadmat(f_data4)
sorted(mat_vari4.keys())
lon_secs = mat_vari4['lon_tran']
lat_secs = mat_vari4['lat_tran']

f_data5 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_secs_spd_mn_ts.mat')
mat_vari5 = sio.loadmat(f_data5)
sorted(mat_vari5.keys())

nemo_sec = 100*mat_vari5['sec_mag_mn']

f_data6 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_SECS_LONLAT.mat')
lbl = sio.loadmat(f_data6)
sorted(lbl.keys())
ylbl = lbl['lbl_dis']*0.001

str_lbl=np.full([40,10],np.nan)
for n in range(40):
    for s in range(10):
        str_lbl[n,s]=str(round(ylbl[n,s]))


#---------------------------------
#load ORAS5 data
#---------------------------------

f_data7 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/ORAS5_GEO_SURFACE_MN.mat')
mat_vari7 = sio.loadmat(f_data7)
sorted(mat_vari7.keys())

oras5_ssh = 100*mat_vari7['int_ssh_mn']

f_data8 = pjoin('/Users/qi/Dropbox/Results_chapter1/ORAS5_GEO_AVG_MN.mat')
mat_vari8 = sio.loadmat(f_data8)
sorted(mat_vari8.keys())
oras5_spd = mat_vari8['int_avg_spd_mn']



f_data10 = pjoin('/Users/qi/Dropbox/Results_chapter1/ORAS5_MN_SPEED_TS.mat')
mat_vari10 = sio.loadmat(f_data10)
sorted(mat_vari10.keys())

oras5_sec = 100*mat_vari10['sec_vel_mn']



rdln=np.full([100],np.nan)
rdln_x=np.full([100],np.nan)
for n in range(100):
    rdln[n]=n
    rdln_x[n]=0

#---------------------------------------------------------
#figure
#---------------------------------------------------------


fig = plt.figure(figsize=[10,11],constrained_layout=True)
plt.clf()
widths = [5,5]
heights = [4,4,4]
spec5 = fig.add_gridspec(ncols=2, nrows=3, width_ratios=widths,
                        height_ratios=heights, wspace=0.04) 

ax1 = fig.add_subplot(spec5[0,0])
ax2 = fig.add_subplot(spec5[0,1])
ax3 = fig.add_subplot(spec5[1,0])
ax4 = fig.add_subplot(spec5[1,1])
ax5 = fig.add_subplot(spec5[2,0])
ax6 = fig.add_subplot(spec5[2,1])

#Spectral
# Panel a - summer
#-------------------------------------------------
ax_current = ax3

masked_array = np.ma.array(ssh, mask=np.isnan(ssh))
cmap_current =matplotlib.cm.jet
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67., -59, -48], vmin=-30, vmax=15)
ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

for s in range(0,10):
    ax_current.plot(lon_secs[:,s],lat_secs[:,s],color='white')

ax_current.text(-78.5,lat_secs[0,0]-0.1,'1',color='white',fontweight="bold")
ax_current.text(-78.5,lat_secs[0,1]-0.1,'2', color='white',fontweight="bold")
ax_current.text(-78.5,lat_secs[0,2]-0.1,'3',color='white',fontweight="bold")
ax_current.text(-78.2,lat_secs[0,3]-0.2,'4', color='white',fontweight="bold")
ax_current.text(-77.1,lat_secs[0,4]-0.3,'5',color='white',fontweight="bold")
ax_current.text(-75.8,lat_secs[0,5]-0.4,'6',color='white',fontweight="bold")
ax_current.text(-74.5,lat_secs[0,6]-0.4,'7',color='white',fontweight="bold")
ax_current.text(-73.2,lat_secs[0,7]-0.3,'8', color='white',fontweight="bold")
ax_current.text(-72.1,lat_secs[0,8]-0.3,'9',color='white',fontweight="bold")
ax_current.text(-68.2,lat_secs[0,9]-0.5,'10',color='white',fontweight="bold")


ax_current.set_ylabel('Lat ($^\degree$S)')
ax_current.set_xlabel('Lon ($^\degree$W)')
ax_current.set_title("(b)", pad=7)

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

#-----------------------------------------------
ax_current = ax1
vmag_here=100*vmag
masked_array = np.ma.array(vmag_here, mask=np.isnan(vmag_here))
cmap_current =matplotlib.cm.hot_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=0, vmax=10)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_ylabel('Lat ($^\degree$S)')
ax_current.set_xlabel('Lon ($^\degree$W)')
ax_current.set_title("(a)", pad=7)


#-------------------------------------------------
ax_current = ax4

masked_array = np.ma.array(oras5_ssh, mask=np.isnan(oras5_ssh))
cmap_current =matplotlib.cm.jet
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67., -59, -48], vmin=-30, vmax=15)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')

#ax_current.set_xticklabels([r'80',r'79', r'78',r'77',r'76',r'75',r'74',r'73',r'72',r'71',r'70',r'69',r'68',r'67'])
#ax_current.set_xticks([-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67])
#ax_current.set_yticklabels([r'59',r'58', r'57',r'56',r'55',r'54',r'53',r'52',r'51',r'50',r'49',r'48'])
#ax_current.set_yticks([-59,-58,-57,-56,-55,-54,-53,-52,-51,-50,-49,-48])
ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

CS=ax_current.contour(bathy.T, levels=[500], colors='white', linestyles='dashed',alpha=1,origin='lower',extent=[-80, -67, -59, -48])

for s in range(0,10):
    ax_current.plot(lon_secs[:,s],lat_secs[:,s],color='white')

ax_current.text(-78.5,lat_secs[0,0]-0.1,'1',color='white',fontweight="bold")
ax_current.text(-78.5,lat_secs[0,1]-0.1,'2', color='white',fontweight="bold")
ax_current.text(-78.5,lat_secs[0,2]-0.1,'3',color='white',fontweight="bold")
ax_current.text(-78.2,lat_secs[0,3]-0.2,'4', color='white',fontweight="bold")
ax_current.text(-77.1,lat_secs[0,4]-0.3,'5',color='white',fontweight="bold")
ax_current.text(-75.8,lat_secs[0,5]-0.4,'6',color='white',fontweight="bold")
ax_current.text(-74.5,lat_secs[0,6]-0.4,'7',color='white',fontweight="bold")
ax_current.text(-73.2,lat_secs[0,7]-0.3,'8', color='white',fontweight="bold")
ax_current.text(-72.1,lat_secs[0,8]-0.3,'9',color='white',fontweight="bold")
ax_current.text(-68.2,lat_secs[0,9]-0.5,'10',color='white',fontweight="bold")

ax_current.set_title("(e)", pad=7)
cbar.set_label('cm', rotation=0, x=-1, y=1.05)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_ylabel('Lat ($^\degree$S)')
ax_current.set_xlabel('Lon ($^\degree$W)')

#-----------------------------------------------
ax_current = ax2

vmag_here=100*oras5_spd
masked_array = np.ma.array(vmag_here, mask=np.isnan(vmag_here))

cmap_current =matplotlib.cm.hot_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=0, vmax=10)


cbar = fig.colorbar(cs, ax=ax_current,extend='both')
ax_current.set_title("(d)", pad=7)
ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])
ax_current.set_ylabel('Lat ($^\degree$S)')
ax_current.set_xlabel('Lon ($^\degree$W)')
cbar.set_label('cm/s', rotation=0, x=0.5, y=1.1)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)




ofs=0
#----------------------------------------------------------------------
ax_current = ax5
for s in range(0,8):
    ofs=ofs+5
    cs = ax_current.plot(ylbl[:,s],nemo_sec[:,s]+ofs,label=str(s+1))
    ax_current.legend(loc="upper left",prop={'size': 6})
    ax_current.plot(rdln_x,rdln,'--k',linewidth=0.05)
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-140,61,20))
ax_current.set_xlim([-140, 61])
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(c)", pad=7)
ax_current.set_ylim([0, 65])

#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)


ofsn=0
#--------------------------------------------------------------------
ax_current = ax6
for s in range(0,8):
    ofsn=ofsn+5
    cs = ax_current.plot(ylbl[:,s],oras5_sec[:,s]+ofsn,label=str(s+1))
    ax_current.legend(loc="upper left",prop={'size': 6})
    ax_current.plot(rdln_x,rdln,'--k',linewidth=0.05)
    #plt.legend(loc=1, prop={'size': 16})

ax_current.set_xlabel('Distance (km)')
ax_current.set_xlim([-140, 61])
ax_current.set_xticks(np.arange(-140,61,20))
ax_current.set_ylim([0, 65])
#ax_current.set_xticks(np.arange(0,40,8))
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(f)", pad=7)




# =============================================================================
# fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/fig01.png',dpi=150, bbox_inches ='tight')
# =============================================================================

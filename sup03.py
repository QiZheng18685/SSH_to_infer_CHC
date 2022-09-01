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
f_data1 = pjoin('/Users/qi/Dropbox/Results_chapter1/TWOSAT_SSH_MN.mat')
mat_vari1 = sio.loadmat(f_data1)
sorted(mat_vari1.keys())
twosat_ssh = 100*mat_vari1['al_ssh_mn']

f_all = pjoin('/Users/qi/Dropbox/Results_chapter1/ALLSAT_SSH_MN.mat')
mat_all = sio.loadmat(f_all)
sorted(mat_all.keys())
allsat_ssh = 100*mat_all['msk_ssh_mn']


f_jpl = pjoin('/Users/qi/Dropbox/Results_chapter1/JPL_SSH_MN.mat')
mat_jpl = sio.loadmat(f_jpl)
sorted(mat_jpl.keys())
jpl_ssh = 100*mat_jpl['remsk_ssh_mn']

#---------------------------------------------------------------------
#load U and V and current speed 

f_data2 = pjoin('/Users/qi/Dropbox/Results_chapter1/TWOSAT_VEL_MN.mat')
mat_vari2 = sio.loadmat(f_data2)
sorted(mat_vari2.keys())
twosat_mag = mat_vari2['mag_mn']
twosat_u = mat_vari2['u_mn']
twosat_v = mat_vari2['v_mn']

f_data3 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/bathymetry_ORCA12.mat')
mat_vari3 = sio.loadmat(f_data3)
sorted(mat_vari3.keys())
bathy = mat_vari3['bathy']

f_data4 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/NEMO_SECS_LONLAT.mat')
mat_vari4 = sio.loadmat(f_data4)
sorted(mat_vari4.keys())
lon_secs = mat_vari4['lon_tran']
lat_secs = mat_vari4['lat_tran']

f_data5 = pjoin('/Users/qi/Dropbox/Results_chapter1/ALLSAT_VEL_MN.mat')
mat_vari5 = sio.loadmat(f_data5)
sorted(mat_vari5.keys())
allsat_mag = mat_vari5['mag_mn']
allsat_u = mat_vari5['u_mn']
allsat_v = mat_vari5['v_mn']

f_data6 = pjoin('/Users/qi/Dropbox/Results_chapter1/JPL_VEL_MN.mat')
mat_vari6 = sio.loadmat(f_data6)
sorted(mat_vari6.keys())
jpl_mag = mat_vari6['mag_mn']
jpl_u = mat_vari6['u_mn']
jpl_v = mat_vari6['v_mn']

#f_data5 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_secs_spd_mn_ts.mat')
#mat_vari5 = sio.loadmat(f_data5)
#sorted(mat_vari5.keys())

#nemo_sec = 100*mat_vari5['sec_mag_mn']

#f_data6 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_SECS_LONLAT.mat')
#lbl = sio.loadmat(f_data6)
#sorted(lbl.keys())
#ylbl = lbl['lbl_dis']*0.001

#str_lbl=np.full([40,10],np.nan)
#for n in range(40):
#    for s in range(10):
#        str_lbl[n,s]=str(round(ylbl[n,s]))



#---------------------------------------------------------
#figure
#---------------------------------------------------------


fig = plt.figure(figsize=[10,11],constrained_layout=True)
plt.clf()
widths = [5,5,5]
heights = [4,4,4,4]
spec5 = fig.add_gridspec(ncols=3, nrows=4, width_ratios=widths,
                        height_ratios=heights, wspace=0.04) 

ax1 = fig.add_subplot(spec5[0,0])
ax2 = fig.add_subplot(spec5[0,1])
ax3 = fig.add_subplot(spec5[0,2])

ax4 = fig.add_subplot(spec5[1,0])
ax5 = fig.add_subplot(spec5[1,1])
ax6 = fig.add_subplot(spec5[1,2])

ax7 = fig.add_subplot(spec5[2,0])
ax8 = fig.add_subplot(spec5[2,1])
ax9 = fig.add_subplot(spec5[2,2])

ax10 = fig.add_subplot(spec5[3,0])
ax11= fig.add_subplot(spec5[3,1])
ax12 = fig.add_subplot(spec5[3,2])


#Spectral
# Panel a - summer
#-------------------------------------------------
ax_current = ax1

twossh = np.ma.array(twosat_ssh, mask=np.isnan(twosat_ssh))
cmap_current =matplotlib.cm.jet
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(twossh.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67., -59, -48], vmin=-35, vmax=18)
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

ax_current.set_title("(a) two-sat", pad=7)

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

#-----------------------------------------------
ax_current = ax4
vmag_here=100*twosat_mag
masked_array = np.ma.array(vmag_here, mask=np.isnan(vmag_here))
cmap_current =matplotlib.cm.hot_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=0, vmax=15)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_ylabel('Lat ($^\degree$S)')

ax_current.set_title("(b)", pad=7)



ax_current = ax7
v_here=100*twosat_v
masked_array = np.ma.array(v_here, mask=np.isnan(v_here))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=-6, vmax=6)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_ylabel('Lat ($^\degree$S)')

ax_current.set_title("(c)", pad=7)



ax_current = ax10
u_here=100*twosat_u
masked_array = np.ma.array(u_here, mask=np.isnan(u_here))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=-6, vmax=6)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_ylabel('Lat ($^\degree$S)')
ax_current.set_xlabel('Lon ($^\degree$W)')
ax_current.set_title("(d)", pad=7)









#-------------------------------------------------
ax_current = ax2
allssh = np.ma.array(allsat_ssh, mask=np.isnan(allsat_ssh))
cmap_current =matplotlib.cm.jet
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(allssh.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67., -59, -48], vmin=-35, vmax=18)
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


ax_current.set_title("(e) all-sat", pad=7)

ax_current.tick_params(top=False,bottom=True,left=True,right=False)


#-----------------------------------------------------------------
ax_current = ax5
vmag_here=100*allsat_mag
masked_array = np.ma.array(vmag_here, mask=np.isnan(vmag_here))
cmap_current =matplotlib.cm.hot_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=0, vmax=15)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_title("(f)", pad=7)



ax_current = ax8
v_here=100*allsat_v
masked_array = np.ma.array(v_here, mask=np.isnan(v_here))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=-6, vmax=6)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_title("(g)", pad=7)



ax_current = ax11
u_here=100*allsat_u
masked_array = np.ma.array(u_here, mask=np.isnan(u_here))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=-6, vmax=6)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_xlabel('Lon ($^\degree$W)')
ax_current.set_title("(h)", pad=7)



#-------------------------------------------------
ax_current = ax3
jpl = np.ma.array(jpl_ssh, mask=np.isnan(jpl_ssh))
cmap_current =matplotlib.cm.jet
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(jpl.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67., -59, -48], vmin=-35, vmax=18)
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


ax_current.set_title("(i) JPL", pad=7)

cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('cm', rotation=0, x=0.5, y=1.01)
#ax_current.set_ylabel('SSH (cm)')
ax_current.tick_params(top=False,bottom=True,left=True,right=False)


#-----------------------------------------------------------------
ax_current = ax6
vmag_here=100*jpl_mag
masked_array = np.ma.array(vmag_here, mask=np.isnan(vmag_here))
cmap_current =matplotlib.cm.hot_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=0, vmax=15)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)


cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('cm/s', rotation=0, x=0.5, y=1.1)
ax_current.set_title("(j)", pad=7)



ax_current = ax9
v_here=100*jpl_v
masked_array = np.ma.array(v_here, mask=np.isnan(v_here))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=-6, vmax=6)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('cm/s', rotation=0, x=0.5, y=1.1)


ax_current.set_title("(k)", pad=7)



ax_current = ax12
u_here=100*jpl_u
masked_array = np.ma.array(u_here, mask=np.isnan(u_here))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67, -59, -48], vmin=-6, vmax=6)
ax_current.tick_params(top=False,bottom=True,left=True,right=False)
#CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

ax_current.set_xticklabels([r'80', r'78',r'76',r'74',r'72',r'70',r'68'])
ax_current.set_xticks([-80,-78,-76,-74,-72,-70,-68])
ax_current.set_yticklabels([r'59', r'57',r'55',r'53',r'51',r'49'])
ax_current.set_yticks([-59,-57,-55,-53,-51,-49])

cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('cm/s', rotation=0, x=0.5, y=1.1)

ax_current.tick_params(top=False,bottom=True,left=True,right=False)

ax_current.set_xlabel('Lon ($^\degree$W)')
ax_current.set_title("(l)", pad=7)





# =============================================================================
fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup03.png',dpi=150, bbox_inches ='tight')
# =============================================================================


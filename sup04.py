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

rdln=np.full([100],np.nan)
rdln_x=np.full([100],np.nan)
for n in range(100):
    rdln[n]=n
    rdln_x[n]=0

#---------------------------------
#load ORAS5 data
#---------------------------------



f_data10 = pjoin('/Users/qi/Dropbox/Results_chapter1/ORAS5_MN_SPEED_TS.mat')
mat_vari10 = sio.loadmat(f_data10)
sorted(mat_vari10.keys())

oras5_sec = 100*mat_vari10['sec_vel_mn']

#---------------------------------------------------------
#figure
#---------------------------------------------------------


fig = plt.figure(figsize=[10,9],constrained_layout=True)
plt.clf()
widths = [4,4]
heights = [4,4,4,4,4]
spec5 = fig.add_gridspec(ncols=2, nrows=5, width_ratios=widths,
                        height_ratios=heights, wspace=0.05) 

ax1 = fig.add_subplot(spec5[0,0])
ax2 = fig.add_subplot(spec5[0,1])
ax3 = fig.add_subplot(spec5[1,0])
ax4 = fig.add_subplot(spec5[1,1])
ax5 = fig.add_subplot(spec5[2,0])
ax6 = fig.add_subplot(spec5[2,1])
ax7 = fig.add_subplot(spec5[3,0])
ax8 = fig.add_subplot(spec5[3,1])
ax9 = fig.add_subplot(spec5[4,0])
ax10 = fig.add_subplot(spec5[4,1])
#Spectral
# Panel a - summer
#-------------------------------------------------



#----------------------------------------------------------------------
ax_current = ax1
s=0
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-160,81,40))
ax_current.set_xlim([-160, 81])
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(a) 1", pad=7)
ax_current.set_ylim([0, 8])
ax_current.set_yticks(np.arange(0,9,2))
#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)


#--------------------------------------------------------------------
ax_current = ax3
s=1
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-160,81,40))
ax_current.set_xlim([-160, 81])
ax_current.set_ylim([0, 10])
ax_current.set_yticks(np.arange(0,11,2))
#ax_current.set_xticks(np.arange(0,40,8))
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(b) 2", pad=7)



ax_current = ax5
s=2
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-160,81,40))
ax_current.set_xlim([-160, 81])
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(c) 3", pad=7)
ax_current.set_ylim([0, 140])
ax_current.set_ylim([0, 20])
ax_current.set_yticks(np.arange(0,21,5))
#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)


#--------------------------------------------------------------------
ax_current = ax7
s=3
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.plot(rdln_x,rdln,'--r')
ax_current.set_xlabel('Distance (km)')
ax_current.set_xlim([-200, 121])
ax_current.set_xticks(np.arange(-200,121,40))
ax_current.set_ylim([0, 20])
#ax_current.set_xticks(np.arange(0,40,8))
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(d) 4", pad=7)


ax_current = ax9
s=4
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-200,121,40))
ax_current.set_xlim([-200, 121])
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(e) 5", pad=7)
ax_current.set_ylim([0, 35])
ax_current.set_yticks(np.arange(0, 36,5))
#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)


#--------------------------------------------------------------------
ax_current = ax2
s=5

ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
    #plt.legend(loc=1, prop={'size': 16})

ax_current.set_xlabel('Distance (km)')
ax_current.set_xlim([-180, 101])
ax_current.set_xticks(np.arange(-180,101,40))
ax_current.set_ylim([0, 30])
#ax_current.set_xticks(np.arange(0,40,8))
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(f) 6", pad=7)



ax_current = ax4
s=6
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-180,81,40))
ax_current.set_xlim([-180, 81])
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(g) 7", pad=7)
ax_current.set_ylim([0, 30])

#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)


#--------------------------------------------------------------------
ax_current = ax6
s=7
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
    #plt.legend(loc=1, prop={'size': 16})

ax_current.set_xlabel('Distance (km)')
ax_current.set_xlim([-180, 80])
ax_current.set_xticks(np.arange(-180,81,40))
ax_current.set_ylim([0, 30])
#ax_current.set_xticks(np.arange(0,40,8))
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(h) 8", pad=7)



ax_current = ax8
s=8
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
ax_current.set_xlabel('Distance (km)')
ax_current.set_xticks(np.arange(-180,121,40))
ax_current.set_xlim([-180, 120])
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(i) 9", pad=7)
ax_current.set_ylim([0, 40])

#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)


#--------------------------------------------------------------------
ax_current = ax10
s=9
ax_current.plot(ylbl[:,s],nemo_sec[:,s],label='NEMO',color='k')
ax_current.plot(ylbl[:,s],oras5_sec[:,s],label='ORAS5',color='b')
ax_current.plot(rdln_x,rdln,'--r')
ax_current.legend(loc="upper left",prop={'size': 6})
    #plt.legend(loc=1, prop={'size': 16})

ax_current.set_xlabel('Distance (km)')
ax_current.set_xlim([-180, 120])
ax_current.set_xticks(np.arange(-180,121,40))
ax_current.set_ylim([0, 100])
#ax_current.set_xticks(np.arange(0,40,8))
#ax_current.set_xticklabels(str_lbl[::8,0])
ax_current.set_ylabel('Speed (cm/s)')
ax_current.set_title("(j) 10", pad=7)





fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup04.png',dpi=150, bbox_inches ='tight')


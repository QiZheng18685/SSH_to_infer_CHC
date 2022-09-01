#this script is used to plot the mean transport at each transect
import os
import scipy.io as sio
from os.path import join as pjoin
import numpy as np
import matplotlib.pyplot as plt

import matplotlib

from matplotlib import colors, ticker

#------------------------------------NEMO---------------------------------
data1 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/NEMO_SECS_TRANSPORT.mat')
vari1=sio.loadmat(data1)
secs=vari1['trns_secs_mn']

f_data6 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_SECS_LONLAT.mat')
lbl = sio.loadmat(f_data6)
sorted(lbl.keys())
ylbl = lbl['lbl_dis']*0.001

        
str_lbl=np.full([40,10],np.nan)
for n in range(40):
    for s in range(10):
        str_lbl[n,s]=str(round(ylbl[n,s]))

pp=np.arange(0,40,6)
#---------------------------------
#figures
#---------------------------------

fig = plt.figure(figsize=[15,19],constrained_layout=True)
plt.clf()
widths = [4, 4]
heights = [2, 2, 2, 2, 2]
spec5 = fig.add_gridspec(ncols=2, nrows=5, width_ratios=widths,
                        height_ratios=heights, wspace=0.02) 

# =============================================================================
# transect1
# =============================================================================

ax_current = fig.add_subplot(spec5[0,0])

s=0
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                   aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])
ax_current.set_ylabel('Depth (m)', labelpad=5)

# =============================================================================
# transect2
# =============================================================================

ax_current = fig.add_subplot(spec5[1,0])

s=1
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])
ax_current.set_ylabel('Depth (m)', labelpad=5)

# # =============================================================================
# # transect3
# # =============================================================================

ax_current = fig.add_subplot(spec5[2,0])
s=2
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])
ax_current.set_ylabel('Depth (m)', labelpad=5)
# # =============================================================================
# # transect4
# # =============================================================================

ax_current = fig.add_subplot(spec5[3,0])

s=3
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])
ax_current.set_ylabel('Depth (m)', labelpad=5)
# # =============================================================================
# # transect5
# # =============================================================================

ax_current = fig.add_subplot(spec5[4,0])

s=4
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')#
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])
ax_current.set_ylabel('Depth (m)', labelpad=5)
ax_current.set_xlabel('Distance (km)')

# =============================================================================
# transect6
# =============================================================================

ax_current = fig.add_subplot(spec5[0,1])
s=5
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
ax_current.set_xticks(pp)
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticklabels(str_lbl[::6,s])


# =============================================================================
# transect7
# =============================================================================

ax_current = fig.add_subplot(spec5[1,1])

s=6
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])


# =============================================================================
# transect8
# =============================================================================

ax_current = fig.add_subplot(spec5[2,1])

s=7
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])

# =============================================================================
# transect9
# =============================================================================

ax_current = fig.add_subplot(spec5[3,1])

s=8
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=-0.02,vmax=0.02)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])

# =============================================================================
# transect10
# =============================================================================

ax_current = fig.add_subplot(spec5[4,1])

s=9
masked_array = np.ma.array(secs[0:50,:,s], mask=np.isnan(secs[0:50,:,s]))
cmap_current =matplotlib.cm.seismic
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array,origin='upper', cmap=cmap_current,
                    aspect='auto', extent=[0, 40, 500,0],vmin=0.01,vmax=0.03)
t='('+str(s+1)+')'
ax_current.set_title(t, pad=7, fontweight="bold")
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv 10m$^{-1}$', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_xticks(pp)
ax_current.set_xticklabels(str_lbl[::6,s])
ax_current.set_xlabel('Distance (km)')






# # =============================================================================
fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup01.png',dpi=150, bbox_inches ='tight')
# # =============================================================================

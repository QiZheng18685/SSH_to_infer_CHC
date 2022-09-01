


import os
import scipy.io as sio
from os.path import join as pjoin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#---------------------------------------------------------------------
#load NEMO data
#----------------------------------------------------------------------

#---------------------------------------------------------------------
#load U and V and current speed 

#twosat-nemo

#allsat-twosat
f_data6 = pjoin('/Users/qi/Dropbox/Results_chapter1/ALLSAT_SSH_MN.mat')
mat_vari6 = sio.loadmat(f_data6)
sorted(mat_vari6.keys())
allsat_mn = 100*mat_vari6['msk_ssh_mn']


f_data7 = pjoin('/Users/qi/Dropbox/Results_chapter1/TWOSAT_SSH_MN.mat')
mat_vari7 = sio.loadmat(f_data7)
sorted(mat_vari7.keys())
twosat_mn = 100*mat_vari7['al_ssh_mn']

diff_two_all=allsat_mn-twosat_mn

f_data4 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/NEMO_SECS_LONLAT.mat')
mat_vari4 = sio.loadmat(f_data4)
sorted(mat_vari4.keys())
lon_secs = mat_vari4['lon_tran']
lat_secs = mat_vari4['lat_tran']


f_data5 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/bathymetry_ORCA12.mat')
mat_vari5 = sio.loadmat(f_data5)
sorted(mat_vari5.keys())
bathy = mat_vari5['bathy']


    
fig = plt.figure(figsize=[5,4],constrained_layout=True)
plt.clf()
widths = [5]
heights = [5]
spec5 = fig.add_gridspec(ncols=1, nrows=1, width_ratios=widths,
                        height_ratios=heights, wspace=0.05) 



ax_current = fig.add_subplot(spec5[0,0])

masked_array = np.ma.array(diff_two_all, mask=np.isnan(diff_two_all))
cmap_current =matplotlib.cm.RdBu_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array.T, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[-80, -67., -59, -48], vmin=-2, vmax=2)
ax_current.set_xticklabels([r'80',r'79', r'78',r'77',r'76',r'75',r'74',r'73',r'72',r'71',r'70',r'69',r'68',r'67'])
ax_current.set_xticks([-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67])

ax_current.set_yticklabels([r'59',r'58', r'57',r'56',r'55',r'54',r'53',r'52',r'51',r'50',r'49',r'48'])
ax_current.set_yticks([-59,-58,-57,-56,-55,-54,-53,-52,-51,-50,-49,-48])
CS=ax_current.contour(bathy.T, levels=[500], colors='white',linestyles='dashed', alpha=1,origin='lower',extent=[-80, -67, -59, -48])

#CS=ax_current.contour(bathy.T, levels=[0], colors='black', alpha=1,origin='lower',extent=[-80, -67, -59, -48])
#CS=ax_current.contour(bathy.T, levels=[0.5], colors=blakc,linestyles='dashed',  alpha=1,origin='lower',extent=[-80, -67, -59, -48])

for s in range(0,10):
    ax_current.plot(lon_secs[:,s],lat_secs[:,s],color='black')

ax_current.text(-78.5,lat_secs[0,0]-0.1,'1',color='black',fontweight="bold")
ax_current.text(-78.5,lat_secs[0,1]-0.1,'2', color='black',fontweight="bold")
ax_current.text(-78.5,lat_secs[0,2]-0.1,'3',color='black',fontweight="bold")
ax_current.text(-78.2,lat_secs[0,3]-0.2,'4', color='black',fontweight="bold")
ax_current.text(-77.1,lat_secs[0,4]-0.3,'5',color='black',fontweight="bold")
ax_current.text(-75.8,lat_secs[0,5]-0.4,'6',color='black',fontweight="bold")
ax_current.text(-74.5,lat_secs[0,6]-0.4,'7',color='black',fontweight="bold")
ax_current.text(-73.2,lat_secs[0,7]-0.3,'8', color='black',fontweight="bold")
ax_current.text(-72.1,lat_secs[0,8]-0.3,'9',color='black',fontweight="bold")
ax_current.text(-68.2,lat_secs[0,9]-0.5,'10',color='black',fontweight="bold")

ax_current.set_xlabel('Lon ($^\degree$W)')

ax_current.set_ylabel('Lat ($^\degree$S)')

cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

ax_current.set_xticklabels([r'80',r'79', r'78',r'77',r'76',r'75',r'74',r'73',r'72',r'71',r'70',r'69',r'68',r'67'])
ax_current.set_xticks([-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67])
ax_current.set_yticklabels([r'59',r'58', r'57',r'56',r'55',r'54',r'53',r'52',r'51',r'50',r'49',r'48'])
ax_current.set_yticks([-59,-58,-57,-56,-55,-54,-53,-52,-51,-50,-49,-48])
cbar.set_label('cm', rotation=0, x=-0.1, y=1.02)
#ax_current.set_title('(d)', pad=7)

# =============================================================================
fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup09.png',dpi=150, bbox_inches ='tight')
# =============================================================================



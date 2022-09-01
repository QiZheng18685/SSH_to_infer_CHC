import os
import scipy.io as sio
from os.path import join as pjoin
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


f_data4 = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_SECS_VF_VOL_15_40.mat')
mat_trn = sio.loadmat(f_data4)
sorted(mat_trn.keys())
nemo_trn = mat_trn['sum_tran_15_40']

f_data = pjoin('/Users/qi/Dropbox/Results_chapter1/NEMO_SECS_LONLAT.mat')
lbl = sio.loadmat(f_data)
sorted(lbl.keys())
ylbl = lbl['lbl_dis_15_40']

f_data5 = pjoin('/Users/qi/Dropbox/Results_chapter1/data/ORAS5_VERTICAL_TRAN.mat')
mat_trn5 = sio.loadmat(f_data5)
sorted(mat_trn5.keys())
oras5_trn = mat_trn5['sum_tran_15_40']

str_lbl=np.full([26,10],np.nan)
for n in range(26):
    for s in range(10):
        str_lbl[n,s]=str(round(ylbl[n,s]*0.001))



T_oras=np.arange(1975, 2015.1, 2)
T_nemo=np.arange(1958, 2016.1, 2)

TT_nemo=np.arange(1958,2016,1/4)
TT_oras=np.arange(1975,2015,1/4)
pp=np.arange(15,41,5)
PP=np.arange(15,41,1)

ylbl_TT1=np.full([160],np.nan)
ylbl_TT2=np.full([160],np.nan)
for n in range(160):
    ylbl_TT1[n]=PP[7]
    ylbl_TT2[n]=PP[15]
    
ylbl_TT1_nemo=np.full([232],np.nan)
ylbl_TT2_nemo=np.full([232],np.nan)
for n in range(232):
    ylbl_TT1_nemo[n]=PP[7]
    ylbl_TT2_nemo[n]=PP[15]


fig = plt.figure(figsize=[23,23],constrained_layout=True)
plt.clf()
widths = [4, 3]
heights = [2, 2, 2, 2, 2, 2, 2 , 2 , 2, 2]
spec5 = fig.add_gridspec(ncols=2, nrows=10, width_ratios=widths,
                        height_ratios=heights, wspace=0.03) 

ax_current = fig.add_subplot(spec5[0,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,0], mask=np.isnan(nemo_trn[:,:,0]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(a) NEMO: Transect 1'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,0])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[0,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,0,:], mask=np.isnan(oras5_trn[:,0,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(TT_oras)
t='(k) ORAS5: Transect 1'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,0])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
      
ax_current = fig.add_subplot(spec5[1,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,1], mask=np.isnan(nemo_trn[:,:,1]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(b) NEMO: Transect 2'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,1])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[1,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,1,:], mask=np.isnan(oras5_trn[:,1,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_oras)
t='(l) ORAS5: Transect 2'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,1])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)
 


ax_current = fig.add_subplot(spec5[2,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,2], mask=np.isnan(nemo_trn[:,:,2]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(c) NEMO: Transect 3'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,2])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------6-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[2,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,2,:], mask=np.isnan(oras5_trn[:,2,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_oras)
t='(m) ORAS5: Transect 3'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,2])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)


#----------------------------------------------------------------------------------------
#-----------------------------------7-----------------------------------------------
#---------------------------------------------------------------------------------------
      
ax_current = fig.add_subplot(spec5[3,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,3], mask=np.isnan(nemo_trn[:,:,3]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(d) NEMO: Transect 4'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,3])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------8----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[3,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,3,:], mask=np.isnan(oras5_trn[:,3,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_oras)
t='(n) ORAS5: Transect 4'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,3])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)




ax_current = fig.add_subplot(spec5[4,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,4], mask=np.isnan(nemo_trn[:,:,4]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(e) NEMO: Transect 5'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,4])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[4,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,4,:], mask=np.isnan(oras5_trn[:,4,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_oras)
t='(o) ORAS5: Transect 5'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,4])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)

#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[5,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,5], mask=np.isnan(nemo_trn[:,:,5]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(f) NEMO: Transect 6'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,5])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[5,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,5,:], mask=np.isnan(oras5_trn[:,5,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_oras)
t='(p) ORAS5: Transect 6'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,5])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)


ax_current = fig.add_subplot(spec5[6,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,6], mask=np.isnan(nemo_trn[:,:,6]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_nemo)
t='(g) NEMO: Transect 7'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,6])
ax_current.set_ylabel('Distance (km)')
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[6,1])
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,6,:], mask=np.isnan(oras5_trn[:,6,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.5)
ax_current.set_xticks(T_oras)
t='(q) ORAS5: Transect 7'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,6])
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)


#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
      
ax_current = fig.add_subplot(spec5[7,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,7], mask=np.isnan(nemo_trn[:,:,7]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=0.8)
ax_current.set_xticks(T_nemo)
t='(h) NEMO: Transect 8'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,7])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[7,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,7,:], mask=np.isnan(oras5_trn[:,7,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=0.8)
ax_current.set_xticks(T_oras)
t='(r) ORAS5: Transect 8'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)

ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,7])
plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)



    
ax_current = fig.add_subplot(spec5[8,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,8], mask=np.isnan(nemo_trn[:,:,8]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=2)
ax_current.set_xticks(T_nemo)
t='(i) NEMO: Transect 9'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,8])
ax_current.set_xticks(T_nemo)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
#----------------------------------------------------------------------------------------
#-----------------------------------2-----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[8,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,8,:], mask=np.isnan(oras5_trn[:,8,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 40], vmin=0,vmax=2)
ax_current.set_xticks(T_oras)
t='(s) ORAS5: Transect 9'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,8])

plt.setp(ax_current,xticklabels=[])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)
ax_current.set_xticks(T_oras)
ax_current.tick_params(top=False,bottom=True,left=True,right=False,labelbottom=False)

#--
#----------------------------------------------------------------------------------------
#-----------------------------------3-----------------------------------------------
#---------------------------------------------------------------------------------------
      
ax_current = fig.add_subplot(spec5[9,0])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(nemo_trn[:,:,9], mask=np.isnan(nemo_trn[:,:,9]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
             aspect='auto', extent=[1958, 2016, 15, 40], vmin=0,vmax=3)
ax_current.set_xticks(T_nemo)
t='(j) NEMO: Transect 10'
ax_current.set_title(t, pad=7)
#cbar = fig.colorbar(cs, ax=ax_current,extend='both')
#cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_ylabel('Distance (km)')
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,9])
ax_current.plot(TT_nemo,ylbl_TT1_nemo,'b',linewidth=2)
ax_current.plot(TT_nemo,ylbl_TT2_nemo,'b',linewidth=2)
ax_current.set_xlabel('Year')
#----------------------------------------------------------------------------------------
#-----------------------------------4----------------------------------------------
#---------------------------------------------------------------------------------------
ax_current = fig.add_subplot(spec5[9,1])
#   if s<8:
#       ax_current.xaxis.set_visible(False)
masked_array = np.ma.array(oras5_trn[:,9,:], mask=np.isnan(oras5_trn[:,9,:]))
cmap_current =matplotlib.cm.gist_heat_r
cmap_current.set_bad('grey', 1.)
cs = ax_current.imshow(masked_array, origin='lower', cmap=cmap_current,
                       aspect='auto', extent=[1975, 2015, 15, 41], vmin=0,vmax=3)
ax_current.set_xticks(T_oras)
t='(t) ORAS5: Transect 10'
ax_current.set_title(t, pad=7)
cbar = fig.colorbar(cs, ax=ax_current,extend='both')
cbar.set_label('Sv', rotation=0, labelpad=-0.1, y=1.1)
ax_current.set_yticks(pp)
ax_current.set_yticklabels(str_lbl[::5,9])
ax_current.plot(TT_oras,ylbl_TT1,'b',linewidth=2)
ax_current.plot(TT_oras,ylbl_TT2,'b',linewidth=2)
ax_current.set_xlabel('Year')

    
    
fig.savefig('/Users/qi/Dropbox/Results_chapter1/paper_codes/sup02.png',dpi=150, bbox_inches ='tight')

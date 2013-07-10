from pyCMBS import *
import os
import numpy as np
from matplotlib import pylab as pl

pl.close('all')

file='air.mon.mean.nc'
if not os.path.exists(file):
    try:
        os.system('wget ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis.derived/surface/air.mon.mean.nc')
    except:
        raise ValueError, 'Can not download sampled data file from NCEP server. Please try manually'

    if not os.path.exists(file):
        raise ValueError, 'Something with the file download went wrong!'

#--- read data ---
D = Data('./air.mon.mean.nc', 'air', lat_name='lat',lon_name='lon',read=True)

#--- generic plotting examples ---
print '**********************************'
print 'Basic plotting ...'
print '**********************************'
print 'The map_plot function always plots the temporal mean field!'
map_plot(D) #simple plot of data matrix
map_plot(D,use_basemap=True)

map_plot(D,show_timeseries=True,use_basemap=True,title='show_timeseries=True')
map_plot(D,show_zonal=True,use_basemap=True,title='show_zonal=True')
map_plot(D,show_histogram=True,use_basemap=True,title='show_histogram=True')

f=pl.figure()
ax1=f.add_subplot(221)
ax2=f.add_subplot(222)
ax3=f.add_subplot(223)
ax4=f.add_subplot(224)

map_plot(D,use_basemap=True,title='vmin=-30.,vmax=30.,cmap_data=RdBu_r',vmin=-30.,vmax=30.,cmap_data='RdBu_r',ax=ax1)
map_plot(D,contours=True,use_basemap=True,levels=np.arange(-50.,50.,10.),title='contours=True',ax=ax2)
map_plot(D,show_stat=True,use_basemap=True,title='show_stat=True',ax=ax3)
map_plot(D,show_stat=True,stat_type='median',use_basemap=True,title='show_stat=True,stat_type="median"',ax=ax4)

pl.show()





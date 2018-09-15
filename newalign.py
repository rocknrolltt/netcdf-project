import xarray as xr

import glob

import numpy as np


latitudes=np.linspace(20.0000,50.0000,100001)
longitudes=np.linspace(-130.0000,-100.0000,100001)
AREASCORE=np.full((100001,100001),255,dtype=np.uint8)
AREAFUEL=np.full((100001,100001),255,dtype=np.uint8)
datasets_WFHS= xr.DataArray(AREASCORE,name='AREASCORE',dims=['latitude','longitude'],coords={'latitude':latitudes,'longitude': longitudes})
print ("created empty array")


for d in glob.glob(r'Z:\travelers\shp\test\*WFHS.nc'):
	d=xr.open_dataset(d)
	d=d.reindex({'latitude': latitudes, 'longitude': longitudes}, method='nearest', tolerance=0.0001)
	print ('done reindex')
	d=d.fillna(255).astype(np.uint8)
	print ("done fillna")
	datasets_WFHS = xr.where(d==255, datasets_WFHS['AREASCORE'], d['AREASCORE'])
	print ("done np where")

# datasets_AF= xr.DataArray(AREAFUEL,name='AREAFUEL',dims=['latitude','longitude'],coords={'latitude':latitudes,'longitude': longitudes})

# for t in glob.glob(r'Z:\travelers\shp\test\*AF.nc'):
	# t=xr.open_dataset(t)
	# t=t.reindex({'latitude': latitudes, 'longitude': longitudes}, 'nearest', tolerance=0.0001)
	# t=t.fillna(255).astype(np.uint8)
	# datasets_AF= xr.where(t==255, datasets_AF['AREAFUEL'], t['AREAFUEL'])


# datasets = xr.merge([datasets_WFHS, datasets_AF], join='outer')

datasets_WFHS.to_netcdf(r"Z:\travelers\shp\test\results.nc")
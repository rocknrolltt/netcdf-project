import xarray as xr

import glob

import numpy as np
from netCDF4 import Dataset

outf=Dataset(r'D:\twu\fireline\travelers\results.nc','w',format='NETCDF4_CLASSIC')
lats=np.linspace(20.0000,50.0000,100001)
lons=np.linspace(-130.0000,-100.0000,100001)


lat=outf.createDimension('lon',len(lats))
lon=outf.createDimension('lat',len(lons))
longitude=outf.createVariable('longitude',np.float64,('lon',))
latitude=outf.createVariable('latitude',np.float64,('lat',))
WFHS=outf.createVariable('AREASCORE',np.int8,('lon','lat'))

longitude[:]=lons
latitude[:]=lats
AREASCORE=np.full((100001,100001),255,dtype=np.uint8)

WFHS[:,:]=AREASCORE

outf.description="AREASCORE for 13 states"
longitude.units="degrees east"
latitude.units='degrees north'

print ("created empty array")
sourcef=outf.variables['AREASCORE'][:]

for d in glob.glob(r'D:\twu\fireline\travelers\test\*WFHS.nc'):
	inf=Dataset(d)

	d_AS=inf.variables['AREASCORE'][:]
	d_AS=d_AS.astype(int)
	d_AS[np.isnan(d_AS)]=255
	sourcef[]
	sourcef[(d_AS<=30)]=d_AS
	outf.variables['AREASCORE'][:]=sourcef
	d.close()
	print ("finish asign")


outf.close()
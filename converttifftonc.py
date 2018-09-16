import xarray as xr

import glob

import numpy as np
from netCDF4 import Dataset
import rasterio


with rasterio.drivers():
	src=rasterio.open(r"D:\twu\fireline\travelers\AF.tiff","r")
	sr1=rasterio.open(r"D:\twu\fireline\travelers\access.tiff","r")
	sr2=rasterio.open(r"D:\twu\fireline\travelers\slope.tiff","r")
	dst_transform=src.transform
	dst_width=src.width
	#print (dst_width)
	
	dst_height=src.height
	#print (dst_height)
	#print (dst_transform)
	#xmin = dst_transform[0]
	xmin=-124.8633388437681333
	#xmax = dst_transform[0] + dst_transform[1]*dst_width
	xmax=-93.4969608019406024
	#print (xmax)
	#ymin = dst_transform[3] + dst_transform[5]*dst_height
	ymin=25.8314103514306339
	#print(ymin)
	#ymax = dst_transform[3]
	ymax=49.0579894904837488
	print (dst_transform)
	print (dst_transform[1])
	print (dst_transform[5])

	dst_width=dst_width
	dst_height=dst_height
	outf=Dataset(r'D:\twu\fireline\travelers\WFHS.nc','w',format='NETCDF4')
	lats=np.linspace(ymin,ymax,dst_height)
	#print (len(lats))
	
	lons=np.linspace(xmin,xmax,dst_width)
	#print (len(lons))
	if dst_transform[1] < 0:
		lons = lons[::-1]
	if dst_transform[5] < 0:
		lats = lats[::-1]

	lat=outf.createDimension('lon',len(lons))
	lon=outf.createDimension('lat',len(lats))
	longitudes=outf.createVariable('longitude',np.float64,('lon',))
	latitudes=outf.createVariable('latitude',np.float64,('lat',))
	SHIA=outf.createVariable('AREASCORE',np.uint8,('lat','lon'))
	#print (longitudes.shape)
	#print (lons.shape)
	#lons=lons[::-1]
	longitudes[:]=lons
	#lats=lats[::-1]
	latitudes[:]=lats
	im=src.read()
	src.close()
	im1=sr1.read()
	sr1.close()
	
	im2=sr2.read()
	sr2.close()
	valid=im!=255
	im[valid] *= im2[valid]
	im[valid] += im1[valid]
	im[im>=250]==255
	SHIA[:,:]=im

	outf.description="AREASCORE for 13 states"
	longitudes.units="degrees east"
	latitudes.units='degrees north'

	print ("created empty array")




# outf.close()

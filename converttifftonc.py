import xarray as xr

import glob

import numpy as np
from netCDF4 import Dataset
import rasterio


with rasterio.drivers():
	src=rasterio.open(r"V:\twu\fireline\travelers\access.tiff","r")
	sr1=rasterio.open(r"D:\twu\fireline\travelers\.tiff","r")
	sr2=rasterio.open(r"D:\twu\fireline\travelers\slope.tiff","r")
	dst_transform=src.transform
	dst_width=src.width
	print (dst_width)
	
	dst_height=src.height
	print (dst_height)
	print (dst_transform)
	#xmin = dst_transform[0]
	xmin=-124.8633388437681333
	#xmax = dst_transform[0] + dst_transform[1]*dst_width
	xmax=-93.4969608019406024
	print (xmax)
	#ymin = dst_transform[3] + dst_transform[5]*dst_height
	ymin=25.8314103514306339
	print(ymin)
	#ymax = dst_transform[3]
	ymax=49.0579894904837488

	dst_width=dst_width
	dst_height=dst_height
	outf=Dataset(r'V:\twu\fireline\travelers\access.nc','w',format='NETCDF4')
	lats=np.linspace(ymin,ymax,dst_width)
	print (len(lats))
	
	lons=np.linspace(xmin,xmax,dst_height)
	print (len(lons))

	lat=outf.createDimension('lon',len(lons))
	lon=outf.createDimension('lat',len(lats))
	longitudes=outf.createVariable('longitude',np.float64,('lon',))
	latitudes=outf.createVariable('latitude',np.float64,('lat',))
	SHIA=outf.createVariable('ACCESS',np.uint8,('lon','lat'))
	print (longitudes.shape)
	print (lons.shape)
	longitudes[:]=lons
	latitudes[:]=lats
	im=src.read()
	im=src.fliplr(im)
	src.close()
	# im1=sr1.read()
	# sr1.close()
	
	# im2=sr2.read()
	# sr2.close()
	# im=im*im2+im1
	# im[im>=250]==255
	SHIA[:,:]=im

	outf.description="Access for 13 states"
	longitudes.units="degrees east"
	latitudes.units='degrees north'

	print ("created empty array")




# outf.close()

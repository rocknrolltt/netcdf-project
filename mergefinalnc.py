import xarray as xr
import dask
import glob

import numpy as np

#d=xr.open_dataset(r'D:\twu\fireline\travelers\AF.nc')
#d=d.set_index(lat='latitude',inplace=True)
#d=d.set_index(lon='longitude',inplace=True)
#d.to_netcdf(r'D:\twu\fireline\travelers\new_AF.nc')
#a=xr.open_dataset(r'D:\twu\fireline\travelers\access.nc')
#a=a.set_index(lat='latitude',inplace=True)
#a=a.set_index(lon='longitude',inplace=True)
#a.to_netcdf(r'D:\twu\fireline\travelers\new_access.nc')
#b=xr.open_dataset(r'D:\twu\fireline\travelers\slope.nc')
#b=b.set_index(lat='latitude',inplace=True)
#b=b.set_index(lon='longitude',inplace=True)
#b.to_netcdf(r'D:\twu\fireline\travelers\new_slope.nc')
#c=xr.open_dataset(r'D:\twu\fireline\travelers\fuel.nc')
#c=c.set_index(lat='latitude',inplace=True)
#c=c.set_index(lon='longitude',inplace=True)
#c.to_netcdf(r'D:\twu\fireline\travelers\new_fuel.nc')
#f=xr.open_dataset(r'D:\twu\fireline\travelers\shia.nc')
#f=f.set_index(lat='latitude',inplace=True)
#f=f.set_index(lon='longitude',inplace=True)
#f.to_netcdf(r'D:\twu\fireline\travelers\new_shia.nc')
# e=xr.open_dataset(r'D:\twu\fireline\travelers\WFHS.nc')
# e=e.set_index(lat='latitude',inplace=True)
# e=e.set_index(lon='longitude',inplace=True)
# e.to_netcdf(r'D:\twu\fireline\travelers\new_WFHS.nc')

# mgd=xr.merge([d,a,b,c,f,e],join='outer')

# hh=xr.open_dataset(r'V:\twu\fireline\travelers\final\fuel_shia_final.nc')


# dd=xr.open_dataset(r'V:\twu\fireline\travelers\final\third_access_AF_final.nc')
# cc=xr.open_dataset(r'V:\twu\fireline\travelers\final\WFHS_Slope_final.nc')

# ds = xr.merge([hh, dd,cc], join='outer')

# # for fname in glob.glob(r'V:\twu\fireline\travelers\final\*.nc'):
	# # ds=xr.open_mfdataset(fname)
# ds.to_netcdf(r"V:\twu\fireline\travelers\fireline_all.nc")


hh=xr.open_dataset(r'D:\twu\fireline\travelers\new_AF.nc')
hh=hh.fillna(255).astype(np.uint8)

dd=xr.open_dataset(r'D:\twu\fireline\travelers\new_access.nc')
dd=dd.fillna(255).astype(np.uint8)


ff=xr.open_dataset(r'D:\twu\fireline\travelers\new_slope.nc')
ff=ff.fillna(255).astype(np.uint8)
ss=xr.open_dataset(r'D:\twu\fireline\travelers\new_shia.nc')
ss=ss.fillna(255).astype(np.uint8)
aa=xr.open_dataset(r'D:\twu\fireline\travelers\new_fuel.nc')
aa=aa.fillna(255).astype(np.uint8)
tt=xr.open_dataset(r'D:\twu\fireline\travelers\new_WFHS.nc')
tt=tt.fillna(255).astype(np.uint8)
# # datasets = xr.merge([hh, dd], join='exact')

datasets = xr.merge([hh,ff,ss,dd,aa,tt], join='outer')


datasets.to_netcdf(r"D:\twu\fireline\travelers\Fireline_13states.nc")

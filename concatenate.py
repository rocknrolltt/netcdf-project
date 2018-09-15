import xarray as xr

import glob

import numpy as np


hh=xr.open_dataset(r'Z:\travelers\shp\test\peo_WA_WFHS.nc')
#hh=hh.fillna(31).astype(np.uint8)
ff=xr.open_dataset(r'Z:\travelers\shp\test\peo_WA_AF.nc')
#ff=ff.fillna(31).astype(np.uint8)
ss=xr.open_dataset(r'Z:\travelers\shp\test\peo_WA_SLOPE.nc')
#ss=ss.fillna(31).astype(np.uint8)
ac=xr.open_dataset(r'Z:\travelers\shp\test\peo_WA_ACCESS.nc')
#ac=ac.fillna(31).astype(np.uint8)
fuel=xr.open_dataset(r'Z:\travelers\shp\test\peo_WA_FUEL.nc')
#fuel=fuel.fillna(31).astype(np.uint8)
shia=xr.open_dataset(r'Z:\travelers\shp\test\peo_WA_SHIA.nc')
#shia=shia.fillna(31).astype(np.uint8)

for d in glob.glob(r'Z:\travelers\shp\test\*_WFHS.nc'):
	d=xr.open_dataset(d,autoclose=True)
	
	hh=d.combine_first(hh)
	#hh=hh.fillna(31).astype(np.uint8)
for t in glob.glob(r'Z:\travelers\shp\test\*AF.nc'):
	t=xr.open_dataset(t,autoclose=True)
	
	ff=t.combine_first(ff)
	#ff=ff.fillna(31).astype(np.uint8)
for s in glob.glob(r'Z:\travelers\shp\test\*SLOPE.nc'):
	s=xr.open_dataset(s,autoclose=True)
	
	ss=s.combine_first(ss)
	#ss=ss.fillna(31).astype(np.uint8)
for a in glob.glob(r'Z:\travelers\shp\test\*ACCESS.nc'):
	a=xr.open_dataset(a,autoclose=True)
	
	ac=a.combine_first(ac)
	#ac=ac.fillna(31).astype(np.uint8)
for f in glob.glob(r'Z:\travelers\shp\test\*FUEL.nc'):
	f=xr.open_dataset(f,autoclose=True)
	
	fuel=f.combine_first(fuel)
	#fuel=fuel.fillna(31).astype(np.uint8)
for sh in glob.glob(r'Z:\travelers\shp\test\*SHIA.nc'):
	sh=xr.open_dataset(sh,autoclose=True)
	
	shia=sh.combine_first(shia)
	#shia=shia.fillna(31).astype(np.uint8)



datasets = xr.merge([hh,ff,ss,ac,fuel,shia], join='outer')


datasets.to_netcdf(r"Z:\travelers\shp\test\results.nc")
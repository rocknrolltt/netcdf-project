import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

ds=xr.open_dataset(r"D:\twu\fireline\travelers\shia.nc")
#print (ds)
var1=ds.SHIA
var1.plot()
plt.show()


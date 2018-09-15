from osgeo import gdal
from osgeo.gdalconst import *
from osgeo import osr
import time
import numpy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from osgeo import ogr

import matplotlib.pyplot as plt
import matplotlib as mpl
import rasterio
from rasterio.merge import merge


import geopandas
from geopandas import *
import os

from matplotlib import colors
import matplotlib.patches as mpatches


outfp=r"D:\twu\fireline\travelers\slope.tiff"
with rasterio.drivers():
	src=rasterio.open(r"D:\twu\fireline\travelers\fuelslopemosaic.tiff","r")
	out_profile=src.profile.copy()
	out_affine=out_profile.pop("affine")
	out_profile["transform"]=out_affine
	im=src.read()
	im[im!=255]=im[im!=255]/10
	im[im==4]=5
	
	
	
	# im[im!=255]=im[im!=255]%10
	# im[(im==5)|(im==0)]=0
	# im[im==3]=5
	# im[im==2]=3
	
						# if value2%10==4:
						# Fuel="NF"
					# elif value2%10==6:
						# Fuel="WA"
					# elif value2%10==5 or value2%10 ==0:
						# Fuel="F0"
					# elif value2%10==2:
						# Fuel="F3"
					# elif value2%10==3:
						# Fuel="F5"
					# else:
						# Fuel="F1"
	# im[(im>0)&(im<=49)]=0
	# im[(im>=61)&(im<=96)]=1
	# im[(im>=111)&(im<=146)]=3
	# im[(im>=161)&(im<=196)]=5
	#im[im!=255]=im[im!=255]%100
	#im[im<100]=0
	# im[(im>=100)&(im!=255)]=im[(im>=100)&(im!=255)]/100
	# if value3>0 and value3<=46:
	# value3="0"
				# elif value3>=61 and value3<=96:
					# value3="1"
				# elif value3>=111 and value3<=146:
					# value3="3"
				# elif value3>=161 and value3<=194:
					# value3="5"
	print (im.max())
	print (im.min())

	#im=im%100
	with rasterio.open(outfp,"w",**out_profile) as dest:
		dest.write(im)
	src.close()







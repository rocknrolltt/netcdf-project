require(raster)
require(rgdal)
require(maptools)
require(raster)
require(stringr)

setwd("D:/twu/fireline/travelers/")
rr<-raster("AF.tiff")
writeRaster(rr,"AF_nc_try.nc")
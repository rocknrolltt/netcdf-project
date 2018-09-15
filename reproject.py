# """""""'"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# "Author: Ting Wu"														"""
# "Date: 6/18/2015""													"""
# "This script unzip files and convert shapefile to netCDF file"		"""
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os, sys, tarfile,subprocess
#from aershp import call_shape2grid
import glob
#import gdal,gdalconst,numpy,ogr,osgeo
#gdal.AllRegister
import time
import rasterio
from rasterio import crs
from datetime import datetime, timedelta
from rasterio.warp import calculate_default_transform, reproject, Resampling
import geopandas as gpd
import numpy as np
from rasterio import crs




# shp to netcdf conversion


os.chdir(r'D:\ArcFireLine\FireRing\Hartford\2016')



AZcountylist=["cno","apa","cuz","gee","ghm","gla","moh","mrc","nav","paz","pin","pma","yav","yma","coc"]
COcountylist=["ads","alm","ara","arc","bac","bld","bmf","bnt","cek",
		"cha","chy","cnj","cos","cus","cwl","den","det","dol","dug",
			"eag","elb","fem","gaf","glp","gra","gun","hin","hue","jak",
			"jfe","kit","kiw","laa","lap","lar","lgn","lke","lnk","mes","mff","min","mor","mot","mtz","ote","our","pas","php",
			"pky","prw","ptk","pub","rib","rig","rtt","saj","sam",
			"sau","sed","smm","tll","uma","wel","wtn"]
IDcountylist=["ada","adm","ban","ber","bnw","bin","bla","bos","bon","bov","bou","btt","cam","can","cbo","cas","clk","clr","cst","elm","frk","fmt",
			  "gem","god","idh","jfs","jer","koo","lat","lem","lis","lin","mdi","mid","nez","one","owy","pay","pow","sho","tet","tnf","vll","whg"]
MTcountylist=["bvr","bhr","bne","bwt","cbn","crt","csd","cho","csr","dan","dws","drl","fal","frg","flh","gal","grf","glc","gdv","grt","hli","jrs","jdb","lae","lac","lbr","lic","mcc","man","mea","mnl","mis",
 			  "mus","par","pet","phl","pon","pwr","pwl","prr","rav","rcl","roo","rbd","snd","srd","svb","slw","swg","ttn","tol","tre","vly","wtl","wib","yel"]
NMcountylist=["brn","cat","chv","cib","cox","cur","deb","doa","edd","grn","gua","hrd","hid","lea","lcn","lam","lun","mck","mra","otr","qua","rio","ros","sdv","sju","smg","sfe","ser","sor","tao","trr","uno","val"]
ORcountylist=["bak","btn","kam","cla","cou","coo","cok","crr","des","dgl","gil","gat","har","hoo","jac","jff","jos","kla","lka","lne","lil","lnn","mal","mao","mrr","mlt","pok","she","til","umt","uni","wao","was","wat","wee","yhl"]
TXcountylist=["and","adw","ang","arn","ach","arm","ata","aus","bly","bdr","bst","byl","bee","bll","bex","bln","brd","bsq","bwi","bza","bzs","brw","brs","brk","bwn",
 			  "brl","brt","cld","clh","cll","cmr","cmp","crs","css","ctr","chm","chk","chl","cly","cch","cke","com","cln","clg","crd","cml","cmn","cnc","coe","cry",
 			  "ctt","crn","cck","crb","clb","dll","dls","daw","dfs","dlt","dnt","dwt","dck","dmm","dnl","dvl","est","ect","edw","ell","elp","ert","fll","fnn","fyt",
 			  "fsh","fly","foa","ftb","fnk","fst","fri","gns","glv","grz","gll","gls","gld","gnz","gry","grs","grg","grm","gdl","hal","hll","ham","han","hrm","hrn",
 			  "hrr","hrs","hrt","hsk","hay","hmp","hnd","hdg","hil","hck","hod","hpk","hst","how","hud","hnt","htc","iri","jck","jks","jsp","jfd","jfr","jmh","jmw",
 			  "jhn","jns","kar","kfm","ken","knd","knt","krr","kmb","kig","knn","klb","knx","lmr","lmb","lmp","lsl","lvc","lee","leo","lib","lim","lip","lvo","lln","lov",
 			  "lbb","lyn","mcl","mln","mml","mds","mrn","mrt","msn","mtg","mav","mdn","mnr","ndl","mlm","mll","mtl","mng","mgm","mre","mrs","mty","ncg","nvr","nwt","nln","nue"
 			  ,"pch","old","orn","plp","pnl","prk","prm","pcs","plk","ptt","prs","rns","rnd","rea","rel","rrv","ree","ref","rob","rbs","rck","rnn","rsk","sab","sag","sjc","spt",
 			  "ssb","sch","scr","shk","shl","shr","smi","som","str","stp","stg","stw","stt","sws","tar","tay","trl","try","thr","tts","tgr","trv","trt","tty","ups","upt","uva","vvr",
 			  "vzn","vic","wlk","wll","wrd","wsh","wbb","wrt","wlr","wch","wlb","wlc","wlm","wls","wnk","wse","wod","yok","yng","zap","zav"]

UTcountylist=["bea","box","cac","car","dag","dav","dch","emr","gfd","gnd","iro","jua","kne","mld","mgn","piu","ric","stl","sun","san","sev","sum","too","unt","uta","waa","war","way","web"]
WAcountylist=["ams","aso","ben","che","clm","cak","clu","cow","dog","fer","fra","gar","gnt","grh","isl","jef","kin","ksp","ktt","kli","lew","lkn","mas","oka","pac","peo","prc","sjn","ska","skm","sno","spk","ste","thu","wkk","wal","whc","whm","yak"]
WYcountylist=["alb","bgh","cpb","cao","cvr","cro","fmo","gos","hot","jon","lrm","lco","nat","nio","pak","plt","srn","sbl","swe","ton","uin","wsk","wst"]
NVcountylist=["chc","crk","dou","elk","esm","eur","hum","lan","lnc","lyo","mrl","nye","per","sto","who","wte","cct"]
CAcountylist=["ala","alp","ama","bte","cal","cco","col","del","eld","fre","gln","hmb","imp","iny","kng","krn","lag","lak","las","mad",
			  "mar","men","mer","mnt","mod","mon","mrp","nap","nev","org","pla","plu","riv","sac","sbb","sbn","sbr","scl","sdg","sfr",
			  "sha","sir","sis","sjq","slo","smt","snc","sol","son","sta","sut","teh","tlm","trn","tul","ven","yol","yub"]
OKcountylist=["adi","alf","ato","bev","bec","bli","bry","cad","cnd","cre","che","ctw","cim","clv","coa","cmc","cot","cra","cee","cer","dlw","dew","els","gfi","gvn","grd","gan","gre","hmn","hrp","has","hug","jcs","jsn","joh","kay","kfs","kio","lti"
	,"lef","lcl","log","lve","maj","msh","may","mcn","mcu","mci","mur","msk","nob","now","okf","okl","okm","osa","ott","paw","pyn","pit","pnt","pot","pus","rog","rgr","sem","seq","sph","tex","tmn","tsa","wag","win","wit","woo","wdw"]

for county in  OKcountylist:
	inshp="OK/%s/%sloc.shp"%(county,county)
	outshp="OK/%s/%slocrepro.shp"%(county,county)
	inshp_pd=gpd.read_file(inshp)
	inshp_pd['new_FUEL'] = inshp_pd['FUEL'].map({'NF': 0, 'F1': 1, 'F3': 3, 'F5': 5})
	inshp_pd['new_SLOPE'] = inshp_pd['SLOPE'].map({'S1': 1, 'S2': 2, 'S3': 3, 'S5': 5})
	inshp_pd['new_ACCESS'] = inshp_pd['ACCESS'].map({'A0': 0, 'A1': 1, 'A3': 3, 'A5': 5})
	inshp_pd['new_SHIA'] = inshp_pd['SHIA'].map({'Y': 1, 'N': 0})
	del inshp_pd['FUEL']
	del inshp_pd['SLOPE']
	del inshp_pd['ACCESS']
	del inshp_pd['SHIA']
	
	inshp_pd_repro=inshp_pd.to_crs({'init': 'epsg:4326'})
	inshp_pd_repro.to_file(driver='ESRI Shapefile',filename=outshp)
	# with rasterio.open("X:/travelers/shp/GRID/AZ/%s/%sfrshiag/w001001.adf"%(county,county),"r") as src:
		# dst_crs=crs.CRS.from_epsg(4326)
		# dst_transform, dst_width, dst_height = calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
		# xmin = dst_transform[2]
		# xmax = dst_transform[2] + dst_transform[0]*dst_width
		# ymin = dst_transform[5] + dst_transform[4]*dst_height
		# ymax = dst_transform[5]
	# outputf = "X:/travelers/shp/output/%s_AZ_AF.nc"%(county)
	# args = ['shape2grid.py',outshp,outputf,'AREAFUEL','--ll', str(ymin),str(xmin),	 '--ur', str(ymax),str(xmax), '-s',str(dst_height), str(dst_width),'--attr','AREAFUEL','AZ']	
	# subprocess.call(args)

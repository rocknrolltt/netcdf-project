from osgeo import gdal
from osgeo import osr
import numpy as np
import netCDF4 as net
import gdal
import rasterio
from rasterio import crs
from rasterio.merge import merge
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.mask import mask
import geopandas as gpd



 
AZcountylist=["gla","moh","mrc","nav","paz","pin","pma","yav","yma","coc"]#"cno","apa","cuz","gee","ghm",
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


state=['AZ']#,'CO','ID','MT','NM','OR','TX','UT','WA','NV','CA','OK','WY']


for st in state:
	print (st)
	if st=="AZ":
		ls=AZcountylist
	if st=="CO":
		ls=COcountylist
	if st=="ID":
		ls=IDcountylist
	if st=="MT":
		ls=MTcountylist
	if st=="NM":
		ls=NMcountylist
	if st=="OR":
		ls=ORcountylist
	if st=="TX":
		ls=TXcountylist
	if st=="UT":
		ls=UTcountylist
	if st=="WA":
		ls=WAcountylist
	if st=="NV":
		ls=NVcountylist
	if st=="CA":
		ls=CAcountylist
	if st=="OK":
		ls=OKcountylist
	if st=="WY":
		ls=WYcountylist
	src_file_to_mosaic=[]
	outf='D:/twu/fireline/travelers/tiffs/merge.tiff'
	for county in ls:
		print (county)
		try:

			with rasterio.drivers():
				src=rasterio.open('D:/twu/fireline/travelers/tiffs/bon_ID_WFHS.tiff')
				src_1=rasterio.open('D:/twu/fireline/travelers/tiffs/peop_WA_WFHS.tiff')
				#src_file_to_mosaic.append()
				src_file_to_mosaic=[src,src_1]
				print ("open")
				mosaic,out_trans=merge(src_file_to_mosaic)
				print ("merge")
				mosaic=mosaic.astype(np.int8)
				with rasterio.open(outf,"w",driver='GTiff',dtype="uint8", nodata=255,compress="lzw",height=mosaic.shape[1],count=1, width=mosaic.shape[2],transform=out_trans,crs="EPSG:4326") as dest:
					dest.write(mosaic,1)
					print ("done")

					
		except Exception as e:
			print (str(e))
			continue
	print (county)
	print (st)
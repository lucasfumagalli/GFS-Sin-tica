import matplotlib.pyplot as plt 
from osgeo import gdal 
from mpl_toolkits.basemap import Basemap 
import numpy as np
from numpy import linspace 
from numpy import meshgrid 
import matplotlib.patheffects as path_effects
import datetime as dt
import matplotlib
from datetime import datetime
from datetime import date
import scipy.ndimage as ndimage
import matplotlib.image as image
import csv
#import wget
import matplotlib.patheffects as path_effects
print('Todos as bibliotecas foram instaladas com sucesso.')
#quit()

plt.rcParams['axes.xmargin'] = 0



print('\n\nPROGRAMA GFS v 15 DIAS\nMeteorologista: Lucas A. F. Coelho')

now = datetime.now()
hora= now.strftime("%H")
minutos= now.strftime("%M")
dia= now.strftime("%d")
dia='25'
mes= now.strftime("%m")
ano= now.strftime("%Y")



print('\n\nInício do processo:', dia,'/',mes,'/',ano,' ',hora,':',minutos,'\n\n')

dti=['015','111','039','135','063','159','087','183','375']

grib0 = gdal.Open('gfs.t12z.pgrb2.0p25.f015.txt')  
grib1 = gdal.Open('gfs.t12z.pgrb2.0p25.f039.txt')  
grib2 = gdal.Open('gfs.t12z.pgrb2.0p25.f063.txt')  
grib3 = gdal.Open('gfs.t12z.pgrb2.0p25.f087.txt')  
grib4 = gdal.Open('gfs.t12z.pgrb2.0p25.f111.txt')  
grib5 = gdal.Open('gfs.t12z.pgrb2.0p25.f135.txt')  
grib6 = gdal.Open('gfs.t12z.pgrb2.0p25.f159.txt')  
grib7 = gdal.Open('gfs.t12z.pgrb2.0p25.f183.txt')  
grib8 = gdal.Open('gfs.t12z.pgrb2.0p25.f375.txt')  


       
extent = [120, -90, 360,0]
min_lon = extent[0]; max_lon = extent[2]; min_lat = extent[1]; max_lat = extent[3]


print('Montando arquivo Grib 0')
grib0 = gdal.Translate('subsected_grib.grb', grib0, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 1')
grib1 = gdal.Translate('subsected_grib.grb', grib1, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 2')
grib2 = gdal.Translate('subsected_grib.grb', grib2, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 3')
grib3 = gdal.Translate('subsected_grib.grb', grib3, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 4')
grib4 = gdal.Translate('subsected_grib.grb', grib4, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 5')
grib5 = gdal.Translate('subsected_grib.grb', grib5, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 6')
grib6 = gdal.Translate('subsected_grib.grb', grib6, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 7')
grib7 = gdal.Translate('subsected_grib.grb', grib7, projWin = [min_lon, max_lat, max_lon, min_lat])    
print('Montando arquivo Grib 8')
grib8 = gdal.Translate('subsected_grib.grb', grib8, projWin = [min_lon, max_lat, max_lon, min_lat])  

varnumber = 277
varnumber2 = 349

v0 = grib0.GetRasterBand(varnumber)
v0 = v0.ReadAsArray() 

v1 = grib1.GetRasterBand(varnumber)
v1 = v1.ReadAsArray() 

v2 = grib2.GetRasterBand(varnumber)
v2 = v2.ReadAsArray() 

v3 = grib3.GetRasterBand(varnumber)
v3 = v3.ReadAsArray() 

v4 = grib4.GetRasterBand(varnumber)
v4 = v4.ReadAsArray() 

v5 = grib5.GetRasterBand(varnumber)
v5 = v5.ReadAsArray() 

v6 = grib6.GetRasterBand(varnumber)
v6 = v6.ReadAsArray() 

v7 = grib7.GetRasterBand(varnumber)
v7 = v7.ReadAsArray() 

v8 = grib8.GetRasterBand(varnumber)
v8 = v8.ReadAsArray() 



vm = (v0+v1+v2+v3+v4+v5+v6+v7+v8)/9
print(np.min(vm), np.max(vm))

data_inicial=dt.datetime(int(ano),int(mes),int(dia))

print('\n\n3. Montando figuras\n\n')

ax = plt.figure(figsize=(15,12))
ax.subplots_adjust(wspace=0.05) 
for i in range(8):
    ax1= ax.add_subplot(4,2,i+1)
    m = Basemap(llcrnrlon=120, llcrnrlat=-90, urcrnrlon=360, urcrnrlat=0,resolution='h')
   # m = Basemap(projection='merc',llcrnrlat=-65,urcrnrlat=0,llcrnrlon=0,urcrnrlon=360,lat_ts=20,resolution='c')
    m.drawparallels(np.arange( -90., 90.,10.),labels=[1,0,0,0],fontsize=5,linewidth=0.2,  dashes=[4, 2], color='gray')
    m.drawmeridians(np.arange(-180.,180.,30.),labels=[0,0,0,1],fontsize=5,linewidth=0.2,  dashes=[4, 2], color='gray')    
    m.drawcountries(linewidth=0.2,color='k')
    m.drawcoastlines(linewidth=0.2,color='k')
    m.fillcontinents('gainsboro',lake_color=(0,0,0,0),zorder=-10)             #  m.bluemarble()
    

    if i ==0: gribi = grib0
    if i ==1: gribi = grib4
    if i ==2: gribi = grib1
    if i ==3: gribi = grib5
    if i ==4: gribi = grib2
    if i ==5: gribi = grib6
    if i ==6: gribi = grib3
    if i ==7: gribi = grib7
        
        
    vi = gribi.GetRasterBand(varnumber)
    vi = vi.ReadAsArray() 
           
    hi = gribi.GetRasterBand(varnumber2)
    hi = hi.ReadAsArray() 

    print(np.max(hi))

    v = vi     -vm
    print(np.min(v),  np.max(v))   

    x = linspace(min_lon, max_lon, v.shape[1])
    y = linspace(max_lat, min_lat, v.shape[0])
    x, y = m(*np.meshgrid(x, y))   
    
    cores = [

    '#B40000','#F50000','#FF3737','#FF6E6E','#FFA5A5','#FFDCDC','#FFFFFF00','#DCDCFF','#A5A5FF','#6E6EFF','#3737FF','#0000F5','#0000B4']

    #levels=[-70,-60,-50,-40,-30,-20,-10,10,20,30,40,50,60,70]
    levels=np.arange(-80,80.1,.1)
   # plotA = m.contourf(x, y, v, colors=cores,levels=levels)             
    plotA = m.contourf(x, y, v, cmap = 'seismic_r',levels=levels) 
    plot = m.contour(x, y, v, linewidths=.1, colors='black',levels=np.arange(10,210,10))          
    labels=plt.clabel(plot, fontsize=4, inline=True ,rightside_up=True,inline_spacing=1,fmt="%i")    
    for z in labels:
        z.set_rotation(0)          

    plot = m.contour(x, y, v, linewidths=.1, linestyles='solid', colors='black',levels=np.arange(-400,0,10))            
    labels=plt.clabel(plot, fontsize=4,inline=True ,rightside_up=True,inline_spacing=1,fmt="%i") 
    for z in labels:
        z.set_rotation(0)       

    plot = m.contour(x, y, hi, linewidths=1, colors='black',levels=np.arange(0,10000,100))          
    labels=plt.clabel(plot, fontsize=5, inline=True ,rightside_up=True,inline_spacing=1,fmt="%i")    
    for z in labels:
        z.set_rotation(0)          



    data0=data_inicial+dt.timedelta(hours=9+int(dti[i]))
    data1=data_inicial+dt.timedelta(hours=9+int(dti[8]))      
    dia0= data0.strftime("%d")
    mes0= data0.strftime("%m")
    ano0= data0.strftime("%Y")
    
    plt.title(''+str(dia0)+'/'+str(mes0)+'/'+str(ano0)+'',fontweight='bold',fontsize=9,loc='left', va='center')    

    
   # fig.text(0.9,0.785,'✆ (45) 32225180\n', fontsize=10, fontweight='bold', color='#3EE45C',ha='right', va='center')    
   # fig.text(0.9,0.785,'\n✉ lucasfumagalli@gmail.com', fontsize=10, fontweight='bold', color='#EA4335',ha='right', va='center')    

        
      #  cax = fig.add_axes([0.9024, 0.2185, 0.02, 0.5532])
      #  fig.colorbar(plotA, shrink=.6, cax=cax) 
ax.text(0.5,.9,'GFS-FV3: 250 hPa Meridional wind anomaly and 500 hPa geopotential height: ',fontweight='bold', ha='center',va='center', fontsize = 13)          
plt.savefig('GFSRossbyWaveActivity_'+str(ano)+'_'+str(mes)+'_'+str(dia)+'.png',bbox_inches='tight', dpi=500, transparent=False)              
  

print('\n\n4. Arquivos salvos\n\n')

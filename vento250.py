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



print('PROGRAMA GFS v 15 DIASMeteorologista: Lucas A. F. Coelho')

now = datetime.now()
hora= now.strftime("%H")
minutos= now.strftime("%M")
dia= now.strftime("%d")
#dia='13'
mes= now.strftime("%m")
ano= now.strftime("%Y")



print('Início do processo:', dia,'/',mes,'/',ano,' ',hora,':',minutos,'')

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
grib0 = gdal.Translate('subsected_grib.grb', grib0, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 1')
grib1 = gdal.Translate('subsected_grib.grb', grib1, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 2')
grib2 = gdal.Translate('subsected_grib.grb', grib2, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 3')
grib3 = gdal.Translate('subsected_grib.grb', grib3, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 4')
grib4 = gdal.Translate('subsected_grib.grb', grib4, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 5')
grib5 = gdal.Translate('subsected_grib.grb', grib5, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 6')
grib6 = gdal.Translate('subsected_grib.grb', grib6, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 7')
grib7 = gdal.Translate('subsected_grib.grb', grib7, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])    
print('Montando arquivo Grib 8')
grib8 = gdal.Translate('subsected_grib.grb', grib8, projWin = [min_lon  , max_lat  , max_lon , min_lat  ])  


varnumber = 277
varnumber2 = 276


u0 = grib0.GetRasterBand(varnumber2)
u0 = u0.ReadAsArray() 

u1 = grib1.GetRasterBand(varnumber2)
u1 = u1.ReadAsArray() 

u2 = grib2.GetRasterBand(varnumber2)
u2 = u2.ReadAsArray() 

u3 = grib3.GetRasterBand(varnumber2)
u3 = u3.ReadAsArray() 

u4 = grib4.GetRasterBand(varnumber2)
u4 = u4.ReadAsArray() 

u5 = grib5.GetRasterBand(varnumber2)
u5 = u5.ReadAsArray() 

u6 = grib6.GetRasterBand(varnumber2)
u6 = u6.ReadAsArray() 

u7 = grib7.GetRasterBand(varnumber2)
u7 = u7.ReadAsArray() 

u8 = grib8.GetRasterBand(varnumber2)
u8 = u8.ReadAsArray() 


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


data_inicial=dt.datetime(int(ano),int(mes),int(dia))

print('3. Montando figuras')

ax = plt.figure(figsize=(15,12))
ax.subplots_adjust(wspace=0.05) 
for i in range(8):
    ax1= ax.add_subplot(4,2,i+1)
    m = Basemap(llcrnrlon=120, llcrnrlat=-90, urcrnrlon=360, urcrnrlat=0,resolution='h')
   # m = Basemap(projection='merc',llcrnrlat=-65,urcrnrlat=0,llcrnrlon=0,urcrnrlon=360,lat_ts=20,resolution='c')
    m.drawparallels(np.arange( -90., 90.,15.),labels=[1,0,0,0],fontsize=8,linewidth=0.2,  dashes=[4, 2], color='gray')
    m.drawmeridians(np.arange(-180.,180.,30.),labels=[0,0,0,1],fontsize=8,linewidth=0.2,  dashes=[4, 2], color='gray')    
    m.drawcountries(linewidth=0.2,color='lime')
    m.drawcoastlines(linewidth=0.2,color='lime')
  #  m.fillcontinents('gainsboro',lake_color=(0,0,0,0),zorder=-10)             
    m.bluemarble()
    
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

    ui = gribi.GetRasterBand(varnumber2)
    ui = ui.ReadAsArray()            

    speed = np.sqrt(ui*ui + vi*vi)


    x = linspace(min_lon, max_lon, speed.shape[1])
    y = linspace(max_lat, min_lat, speed.shape[0])
    x, y = m(*np.meshgrid(x, y))   
    
    levels=np.arange(30,70.1,.1)
   # plotA = m.contourf(x, y, speed, colors=cores,levels=levels)             
    plotA = m.contourf(x, y, speed, cmap = 'gnuplot2',levels=levels) 
    plotB = m.contourf(x, y, speed, colors = 'white',levels=np.arange(70,300,10)) 

    data0=data_inicial+dt.timedelta(hours=9+int(dti[i]))
    data1=data_inicial+dt.timedelta(hours=9+int(dti[8]))      
    dia0= data0.strftime("%d")
    mes0= data0.strftime("%m")
    ano0= data0.strftime("%Y")
    
    plt.title(''+str(dia0)+'/'+str(mes0)+'/'+str(ano0)+'',fontweight='bold',fontsize=9,loc='left', va='center')    

    
ax.text(0.9,0.91,'✆ (45) 32225180', fontsize=9, fontweight='bold', color='#3EE45C',ha='right', va='center')    
ax.text(0.9,0.90,'✉ lucasfumagalli@gmail.com', fontsize=9, fontweight='bold', color='#EA4335',ha='right', va='center')    
ax.text(0.5,.9,'GFS-FV3 250 hPa JET STREAM', fontweight='bold', ha='center',va='center', fontsize = 13)          
ax.text(0.8,0.06,'m $s^{-1}$', fontsize=9, fontweight='bold', color='k',ha='center', va='center')    

cax = ax.add_axes([0.25, 0.07, 0.5, 0.011])

ax.colorbar(plotA, shrink=.6, orientation='horizontal',  boundaries= [0]+ levels + [10], extendfrac='auto',  extend='max', fraction=.1, cax=cax) 

        

plt.savefig('GFS250hpawind_'+str(ano)+'_'+str(mes)+'_'+str(dia)+'.png',bbox_inches='tight', dpi=500, transparent=False)              
  

print('4. Arquivos salvos')

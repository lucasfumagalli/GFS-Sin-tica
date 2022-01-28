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
#dia='13'
mes= now.strftime("%m")
ano= now.strftime("%Y")



print('\n\nInício do processo:', dia,'/',mes,'/',ano,' ',hora,':',minutos,'\n\n')

rodada = '12'

if int(rodada) == 12:
   z=['015','111','039','135','063','159','087','183','375']


if int(rodada) == 6:
   z=['000','093','021','117','045','141','069','165','357']

grib0 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[0]+'.txt')  
grib1 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[1]+'.txt')  
grib2 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[2]+'.txt')  
grib3 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[3]+'.txt')  
grib4 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[4]+'.txt')  
grib5 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[5]+'.txt')  
grib6 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[6]+'.txt')  
grib7 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[7]+'.txt')  
grib8 = gdal.Open('gfs.t'+rodada+'z.pgrb2.0p25.f'+z[8]+'.txt')  


       
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

u250 = 276
v250 = 277
T500 = 350


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
    if i ==1: gribi = grib1
    if i ==2: gribi = grib2
    if i ==3: gribi = grib3
    if i ==4: gribi = grib4
    if i ==5: gribi = grib5
    if i ==6: gribi = grib6
    if i ==7: gribi = grib7
        
        
    u = gribi.GetRasterBand(u250)
    u = u.ReadAsArray() 
           
    v = gribi.GetRasterBand(v250)
    v = v.ReadAsArray() 

    T = gribi.GetRasterBand(T500)
    T = T.ReadAsArray() 


    x = linspace(min_lon, max_lon, v.shape[1])
    y = linspace(max_lat, min_lat, v.shape[0])
    x, y = m(*np.meshgrid(x, y))   
    


    cores = ['#4700A1','#4D11A2','#613BAD','#967BC7','#CFC3E5','#FFFFFF','#FCC9C9','#F98A95','#F4405E','#F4002E','#F30000','#D00000','#D00000']            


    levels=[-50,-22,-21,-20,-19,-18,-9,-8,-7,-6,-5,-4,20]
    plotA = m.contourf(x, y, T, colors=cores, levels=levels)             
    plotB = m.streamplot(x, y, u, v, color='black', density=8, linewidth=0.2, arrowstyle='->',arrowsize=0.35) 




    data0=data_inicial+dt.timedelta(hours=9+int(z[i]))
    data1=data_inicial+dt.timedelta(hours=9+int(z[8]))      
    dia0= data0.strftime("%d")
    mes0= data0.strftime("%m")
    ano0= data0.strftime("%Y")
    
    plt.title(''+str(dia0)+'/'+str(mes0)+'/'+str(ano0)+'',fontweight='bold',fontsize=9,loc='left', va='center')    

    
   # fig.text(0.9,0.785,'✆ (45) 32225180\n', fontsize=10, fontweight='bold', color='#3EE45C',ha='right', va='center')    
   # fig.text(0.9,0.785,'\n✉ lucasfumagalli@gmail.com', fontsize=10, fontweight='bold', color='#EA4335',ha='right', va='center')    

        
      #  cax = fig.add_axes([0.9024, 0.2185, 0.02, 0.5532])
      #  fig.colorbar(plotA, shrink=.6, cax=cax) 
ax.text(0.9,0.91,'✆ (53) 991605100', fontsize=9, fontweight='bold', color='#3EE45C',ha='right', va='center')    
ax.text(0.9,0.90,'✉ lucasfumagalli@gmail.com', fontsize=9, fontweight='bold', color='#EA4335',ha='right', va='center')    
ax.text(0.5,.9,'GFS-FV3 250 hPa streamline and 500 hPa temperature ',fontweight='bold', ha='center',va='center', fontsize = 13)          
ax.text(0.8,0.065,'C', fontsize=9, fontweight='bold', color='k',ha='center', va='center')    
cax = ax.add_axes([0.25, 0.07, 0.5, 0.011])
ax.colorbar(plotA, shrink=.6, orientation='horizontal',  boundaries= [0]+ levels + [10], extendfrac='auto',  extend='max', fraction=.1, cax=cax) 


plt.savefig('T500UV250_'+str(ano)+'_'+str(mes)+'_'+str(dia)+'.png',bbox_inches='tight', dpi=500, transparent=False)              
  

print('\n\n4. Arquivos salvos\n\n')

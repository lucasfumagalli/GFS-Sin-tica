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

matplotlib.rcParams.update({'font.size': 10})
plt.rcParams['axes.xmargin'] = 0

plt.rcParams['axes.xmargin'] = 0



print('\n\nPROGRAMA GFS v 15 DIAS\nMeteorologista: Lucas A. F. Coelho')

now = datetime.now()
hora= now.strftime("%H")
minutos= now.strftime("%M")
dia= now.strftime("%d")
#dia='08'
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


data_inicial=dt.datetime(int(ano),int(mes),int(dia))

data0=data_inicial+dt.timedelta(hours=9+int(z[0]))
data1=data_inicial+dt.timedelta(hours=9+int(z[7]))      
dia0= data0.strftime("%d")
mes0= data0.strftime("%m")
ano0= data0.strftime("%Y")
dia1= data1.strftime("%d")
mes1= data1.strftime("%m")
ano1= data1.strftime("%Y")

print('\n\n3. Montando figuras\n\n')


fig = plt.figure(figsize=(15,15))
for i in range(3):
    ax= fig.add_subplot(3,1,i+1)
    m = Basemap(llcrnrlon=120, llcrnrlat=-90, urcrnrlon=360, urcrnrlat=0,resolution='h')
    m.drawparallels(np.arange( -90., 90.,10.),labels=[1,0,0,0],fontsize=8,linewidth=0.2,  dashes=[4, 2], color='gray')
    m.drawmeridians(np.arange(-180.,180.,30.),labels=[0,0,0,1],fontsize=8,linewidth=0.2,  dashes=[4, 2], color='gray')    
    m.drawcountries(linewidth=0.4,color='k')
    m.drawcoastlines(linewidth=0.4,color='k')
            
    u = []   
    for k in range(8):
        if k ==0: gribi = grib0
        if k ==1: gribi = grib1
        if k ==2: gribi = grib2
        if k ==3: gribi = grib3
        if k ==4: gribi = grib4
        if k ==5: gribi = grib5
        if k ==6: gribi = grib6
        if k ==7: gribi = grib7
                
        ui = gribi.GetRasterBand(u250)
        ui = ui.ReadAsArray() 
        u.append(ui)
    u = sum(u)/len(u)     

    x = linspace(min_lon, max_lon, u.shape[1])
    y = linspace(max_lat, min_lat, u.shape[0])
    x, y = m(*np.meshgrid(x, y))   
    

    Ω=7.292e-5
    a=6.37e+6
    rad = np.pi/180
    
    cosy = np.cos(y*rad)

    termo1=(2*Ω*(cosy**2))/a

    termo2=(cosy)/a**2

    termo3=1/cosy

    termo4=u*cosy

    dcoslatj= np.gradient(termo4, axis=0,edge_order=2)      

    dlat= np.gradient(y, axis=0,edge_order=2)*rad  
    
    dcosdlat=(dcoslatj/dlat)

    termo5=termo3*dcosdlat

    termo6= np.gradient(termo5, axis=0,edge_order=2)  
       
    termo7=(termo6/dlat)

    βm=(termo1-(termo2*termo7))*1.0e+11

    vbarra1=u/(a*(cosy))

    ks=(((a*(termo1-(termo2*termo7)))/vbarra1)) **(0.5) 


    if i ==0: 
       data=u
       plt.title('a)',loc='left'); plt.title('Zonal wind',loc='center') 

       levels=np.arange(-20,60,5)
       plot = m.contourf(x, y, data, cmap='jet',levels=levels)         
       levels2=np.arange(55,105,10)
       plot1 = m.contourf(x, y, data, colors='#9A0000',levels=levels2)                 
       plot2 = m.contour(x, y, data, linewidths=.5, linestyles='solid', colors='black',levels=levels)
       labels=plt.clabel(plot2,fontsize=10,inline=True , rightside_up=True,inline_spacing=1,fmt="%i")    
       for zk in labels:
           zk.set_rotation(0)         
       cax = fig.add_axes([0.920, 0.668, 0.012, 0.199])
       fig.colorbar(plot, shrink=.6, cax=cax)   

    if i ==1:     
       plt.title('b)',loc='left'); plt.title('Meridional gradient of absolute vorticity β*',loc='center') 
       data = βm
       levels=np.arange(-9,18,1)
       plot = m.contourf(x, y, data, cmap='jet',levels=levels)  
       levels2=np.arange(17,20000,1000)
       plotx = m.contourf(x, y, data, colors='#9A0000',levels=levels2) 
       levels2=np.arange(-100,-8,1)
       plotx = m.contourf(x, y, data, colors='navy',levels=levels2) 

       cax = fig.add_axes([0.920, 0.395, 0.012, 0.199])
       fig.colorbar(plot, shrink=.6, cax=cax)        
           
    if i ==2: 
       plt.title('c)',loc='left'); plt.title('Stationary Rossby wave number KS',loc='center')         
       data=ks   	    
       levels=np.arange(0,11,1)
       plot = m.contourf(x, y, data, cmap='gist_stern_r',levels=levels)            
       levels=np.arange(10,300000,100000)
       plotB = m.contourf(x, y, data, colors='#7F070E',levels=levels)                     
       cax = fig.add_axes([0.920, 0.124, 0.012, 0.199])
       fig.colorbar(plot, shrink=.6, cax=cax)         
    

    fig.text(0.9,0.91,'✆ (53) 991605100', fontsize=9, fontweight='bold', color='#3EE45C',ha='right', va='center')    
    fig.text(0.9,0.90,'✉ lucasfumagalli@gmail.com', fontsize=9, fontweight='bold', color='#EA4335',ha='right', va='center')    

    fig.text(0.5,.9,'GFS-FV3 250 hPa basic state between '+str(dia0)+'/'+str(mes0)+'/'+str(ano0)+' - '+str(dia1)+'/'+str(mes1)+'/'+str(ano1)+' ',fontweight='bold', ha='center',va='center', fontsize = 13)          


   
    plt.savefig('basicstate_'+str(ano)+'_'+str(mes)+'_'+str(dia)+'.png',bbox_inches='tight', dpi=500, transparent=False)              
  

print('\n\n4. Arquivos salvos\n\n')

from django.shortcuts import render
from django.http import HttpResponse
from . import models
import datetime  


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders




def informes(request):
    tabla = models.TbProduct.objects.select_related().all()
    context = {'tabla' : tabla}   
    return render(request, 'informes/index.html',context)
    
def inicio(request):
    #tabla = models.TbProduct.objects.all()
    #context = {'tabla' : tabla}   
    return render(request, 'informes/inicio.html',{})

def about(request):
    #tabla = models.TbProduct.objects.all()
    #context = {'tabla' : tabla}   
    return render(request, 'informes/about.html',{})

def ventas(request):
    
    total  =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cant   =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    device =    ['1','2','3','4','5','6','7','8','9','10','11','17','18','19','20','21','22','23','24']#id maquinas
    cont   = 0
    gran_total = 0
    placas_total = 0
    
    date_range = request.POST.get('fecha')
    
    start_date = datetime.date.today()
    end_date = datetime.date.today()
    
    if date_range == "hoy":
        start_date = datetime.date.today()
        end_date = datetime.date.today()+datetime.timedelta(days=1)
        #print(start_date)
        #print(end_date)
    if date_range == "ayer":
        start_date = datetime.date.today()-datetime.timedelta(days=1)
        end_date = datetime.date.today()
        #print(start_date)
        #print(end_date)
    if date_range == "semana":
        start_date = datetime.date.today()-datetime.timedelta(days=7)
        end_date = datetime.date.today()
        #print(start_date)
        #print(end_date)
    if date_range == "mes":
        start_date = datetime.date.today()-datetime.timedelta(days=7)
        end_date = datetime.date.today()
        #print(start_date)
        #print(end_date) 
    if date_range == "rango":
        start_date = request.POST.get('fechainicial')
        end_date = request.POST.get('fechafinal')
    
    
    if date_range != "default":
        for dev in device:
            #consulta ventas por id de maquina en un rango de fecha        
            query = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(start_date, end_date)).select_related()
            cant[cont] = query.count() #cantidad de ventas por maquina
            #total venta por id de 
            for query in query:
                total[cont] = query.billingtotal + total[cont]
            
            cont = cont + 1
            
        #total ventas    
        for i in total:
            gran_total = i + gran_total
            
        #total placas vendidas
        for j in cant:
            placas_total = j + placas_total
        
    context = {
        'venta1':cant[0],
        'total1':total[0],

        'venta2':cant[1],
        'total2':total[1],
        
        'venta3':cant[2],
        'total3':total[2],
        
        'venta4':cant[3],
        'total4':total[3],
        
        'venta5':cant[4],
        'total5':total[4],
        
        'venta6':cant[5],
        'total6':total[5],
        
        'venta7':cant[6],
        'total7':total[6],
        
        'venta8':cant[7],
        'total8':total[7],
        
        'venta9':cant[8],
        'total9':total[8],
        
        'venta10':cant[9],
        'total10':total[9],
        
        'venta11':cant[10],
        'total11':total[10],
        
        'venta12':cant[11],
        'total12':total[11],
        
        'venta13':cant[12],
        'total13':total[12],
        
        'venta14':cant[13],
        'total14':total[13],
        
        'venta15':cant[14],
        'total15':total[14],
        
        'venta16':cant[15],
        'total16':total[15],
        
        'venta17':cant[16],
        'total17':total[16],
        
        'venta18':cant[17],
        'total18':total[17],
        
        'venta19':cant[18],
        'total19':total[18],
        
        'Total':gran_total,
        'placas': placas_total,
        
    }
    #return HttpResponse("prueba")
    return render(request, 'informes/ventas.html',context)

def pdf(request):
    template = get_template('informes/ventas.html')
    context = {'title':''}
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_ventas.pdf"'
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    return response

def maquinas(request):
    lista_fechas = []
    total_diario = []
    stop = 0
    cont = 0
    total = 0
    total_ = 0
       
    start_date = request.POST.get('fechainicial')
    end_date = request.POST.get('fechafinal')
    
    zonas = models.TbDevicezone.objects.all() #generar lista de zonas
    select_zona = request.POST.get('zona') #selección del usuario
    id_zona = models.TbDevicezone.objects.filter(devicezonename=select_zona).first() #consultar el id de la zona seleccionada
    id_maquina = models.TbDevice.objects.filter(id_devizezone=(id_zona)).first() #buscar id de la maquina que corresponde
    
    if start_date != None and end_date != None:
        start_date2 = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date2 = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        #busqueda de las ventas que coinciden con el id de la maquina y la fecha establecida
        querys = models.TbBilling.objects.filter(id_device=id_maquina, billingtransaciondate__range=(start_date2, end_date2)).select_related()
        #querys = []
        for query in querys:
            total = query.billingtotal + total
        
    #busqueda de las ventas diarias de la maquina
    ##creacion fechas diarias
    if start_date != None and end_date != None:
        conv_fecha_ini = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        conv_fecha_fin = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        
        while(stop != 1):
            
            lista_fechas.append(conv_fecha_ini) 
            conv_fecha_ini = conv_fecha_ini + datetime.timedelta(days=1)
            
            if conv_fecha_ini == conv_fecha_fin:
                stop = 1
                
        for fechas in lista_fechas: 
            
            total_ = 0
            fecha_end = fechas + datetime.timedelta(days=1)                   
            query2 = models.TbBilling.objects.filter(id_device=id_maquina, billingtransaciondate__range=(fechas, fecha_end)).select_related()
            
            for query in query2:
                total_ = query.billingtotal + total_
                
            total_diario.append(total_)
            
    context ={
        'zonas':zonas,
        'id_maquina':id_maquina,
        'total':total,
        'lista_fechas':lista_fechas,
        'total_diario':total_diario,       
    }
    
    return render(request, 'informes/maquinas.html', context)
    
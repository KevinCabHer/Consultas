from calendar import c
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import datetime  


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
import pdfkit
from jinja2 import Environment, FileSystemLoader 

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


context1 = {}
context2 = {}

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
    global context1   
    context1 = {
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
    return render(request, 'informes/ventas.html',context1)

def pdf(request):
    template = get_template('informes/ventas.html')
    #context = {'title':''}
    html = template.render(context1)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_ventas.pdf"'
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    return response

def maquinas(request):
    lista_fechas = []
    total_diario = []
    contenedor =[]
    stop = 0
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
            
    total1 = sum(total_diario)
    print(total1)
    
    contenedor = {lista_fechas:total_diario for (lista_fechas,total_diario) in zip(lista_fechas,total_diario)}
    
    prueba = []
    for element in lista_fechas:
        prueba.append(str(element))
        
    contenedor2 = {prueba:total for (prueba,total) in zip(prueba,total_diario)}
    
    global context2    
    context2 ={
        'zonas':zonas,
        'id_maquina':id_maquina,
        'total':total,
        'lista_fechas':lista_fechas,
        'total_diario':total_diario, 
        'contenedor': contenedor,
        'contenedor2': contenedor2,
        'total1' : total1     
    }
    
    return render(request, 'informes/maquinas.html', context2)

def pdf2(request):
    template = get_template('informes/maquinas.html')
    #context = {'title':''}
    html = template.render(context2)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_maquinas.pdf"'
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    return response

def comparacion(request):
    total_device = []
    device_ventas = {}
    device_new = []
    device_str = []
    lista_fechas = []
    stop = 0
    
    start_date = request.POST.get('fechainicial')
    end_date = request.POST.get('fechafinal')    
    
    device = [
        request.POST.get('pet01'),
        request.POST.get('pet02'),
        request.POST.get('pet03'),
        request.POST.get('pet04'),
        request.POST.get('pet05'),
        request.POST.get('pet06'),
        request.POST.get('pet07'),
        request.POST.get('pet08'),
        request.POST.get('pet09'),
    ]      
    # Tomar los valores de la lista diferentes de None - generar lista con los nombres de la maquinas
    for dev in device:
        if dev is not None:
            device_new.append(int(dev))
            device_str.append("PET0"+dev)
                     
    if start_date != None and end_date != None: #Siempre y cuando halla valores seleccionados
        
        #conversion fechas para poder trabajar operaciones
        start_date2 = datetime.datetime.strptime(start_date, '%Y-%m-%d') 
        end_date2 = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        
        #Total de ventas por maquina y rango de fecha
        for dev in device_new:
            total_ = 0
            querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(start_date2, end_date2)).select_related()
            for query in querys:
                total_ = query.billingtotal + total_
            total_device.append(total_)
        
        device_ventas = {device_str:total_device for (device_str,total_device) in zip(device_str,total_device)}

        #Total de ventas por maquina y dia
        
        #conv_fecha_ini = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        #conv_fecha_fin = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        
        while(stop != 1):
            
            lista_fechas.append(start_date2) 
            start_date2 = start_date2 + datetime.timedelta(days=1)
            
            if start_date2 == end_date2:
                stop = 1
        
        context={
            'device_ventas':device_ventas, 
            'fecha_ini':start_date,
            'fecha_fin':end_date
        }
    else:
        context = {}
    return render(request, 'informes/comparacion.html', context)
    
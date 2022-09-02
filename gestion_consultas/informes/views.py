from calendar import c, month
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import datetime 
import pandas as pd 
import numpy as np
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
    return render(request, 'informes/inicio.html',{})

def about(request):   
    return render(request, 'informes/about.html',{})

def ventas(request):
    total  =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #esto se puede mejorar
    cant   =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #esto se puede mejorar
    device =    ['1','2','3','4','5','6','7','8','9','10','11','17','18','19','20','21','22','23','24']#id maquinas  #esto se puede mejorar
    cont   = 0
    gran_total = 0
    placas_total = 0
    
    date_range = request.POST.get('fecha')    
    #esto se puede mejorar
    if date_range != None:
        
        start_date = datetime.date.today()
        end_date = datetime.date.today()
        
        if date_range == "hoy":
            start_date = datetime.date.today()
            end_date = datetime.date.today()+datetime.timedelta(days=1)

        if date_range == "ayer":
            start_date = datetime.date.today()-datetime.timedelta(days=1)
            end_date = datetime.date.today()

        if date_range == "semana":
            start_date = datetime.date.today()-datetime.timedelta(days=7)
            end_date = datetime.date.today()
            
        if date_range == "mes":
            start_date = datetime.date.today()-datetime.timedelta(days=7)
            end_date = datetime.date.today()
            
        if date_range == "rango":
            start_date = request.POST.get('fechainicial')
            end_date = request.POST.get('fechafinal')
        
        for dev in device:
            #consulta ventas por id de maquina en un rango de fecha        
            query = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(start_date, end_date)).select_related()
            cant[cont] = query.count() #cantidad de ventas por maquina
            #total venta por id de 
            for query in query:
                total[cont] = query.billingtotal + total[cont]
            
            cont = cont + 1
        # total dinero 
        for i in total:
            gran_total = i + gran_total
            
        #total placas vendidas
        for j in cant:
            placas_total = j + placas_total
            
    global context1  #variable global para generar pdf
      
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
    
    if start_date != None and end_date != None and select_zona != None:
        start_date2 = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date2 = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        #busqueda de las ventas que coinciden con el id de la maquina y la fecha establecida
        querys = models.TbBilling.objects.filter(id_device=id_maquina, billingtransaciondate__range=(start_date2, end_date2)).select_related()
        #querys = []
        for query in querys:
            total = query.billingtotal + total
        
    #busqueda de las ventas diarias de la maquina
    ##creacion fechas diarias
    #if start_date != None and end_date != None:
        
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
    else:
        return render(request, 'informes/maquinas.html', {'zonas':zonas,})

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
    total_int = []
    total_int_ = []
    device_ventas = {}
    device_new = []
    device_str = []
    lista_fechas = []
    total_diario_maquina = []
    total_diario_maquinas = []
    stop = 0
    
    start_date = request.POST.get('fechainicial')
    end_date = request.POST.get('fechafinal')  
    
    check_box = request.POST.get('seleccion_rango')  
    semana = request.POST.get('semana')
    
    mes = request.POST.get('mes')  
    
    #print(check_box)
    #print(semana)
    
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
              
        if check_box == "1": #opcion semanas
            pass
        if check_box == "2": #opcion meses
            control = 0
            mes = mes + "-01" # fecha 01 del mes
            start_date2 = datetime.datetime.strptime(mes, '%Y-%m-%d') #fecha inicial
            mes = start_date2.month #mes en el que estoy
            copia = start_date2 #fecha final inicia en fecha inicial
            mes2 = copia.month #mes 2 inicia en el mes en el que estoy
            
            while(control == 0): #itero el mes hasta el ultimo dia del mismo      
                copia = copia + datetime.timedelta(days=1)
                mes2 = copia.month
                if mes == mes2:
                    end_date2 = copia
                else:
                    control = 1
    
        if check_box == "3": #opcion rango fechas
            start_date2 = datetime.datetime.strptime(start_date, '%Y-%m-%d') 
            end_date2 = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
        fecha_ini = start_date2
        fecha_fin = end_date2    
        #conversion fechas para poder trabajar operaciones
        
        
        #Total de ventas por maquina y rango de fecha
        for dev in device_new:
            total_ = 0
            querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(start_date2, end_date2)).select_related()
            for query in querys:
                total_ = query.billingtotal + total_
            total_device.append(total_)
        
        device_ventas = {device_str:total_device for (device_str,total_device) in zip(device_str,total_device)}

        #Total de ventas por maquina y dia
        
        #generar lista con las fecchas segun rango seleccionado
        while(stop != 1):
            
            lista_fechas.append(start_date2) 
            start_date2 = start_date2 + datetime.timedelta(days=1)
            
            if start_date2 == end_date2:
                stop = 1

        for dev in device_new: #recorro las maquinas
            total_diario_maquina = []
            total_int = []
            #print(dev)
            for fecha_i in lista_fechas:# busqueda diaria por maquina
                fecha_f = fecha_i + datetime.timedelta(days=1)
                querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(fecha_i, fecha_f)).select_related()
                subtotal_device = 0
                #print(fecha_i)
                for query in querys:# sumatoria del total de la venta en ese dia
                    subtotal_device = query.billingtotal + subtotal_device
                total_diario_maquina.append(subtotal_device) #lista con las ventas diarias de la maquina
                total_int.append(int(subtotal_device))
            #print(len(total_diario_maquina))
            #print(sum(total_diario_maquina))
            total_int_.append(total_int)
            total_diario_maquinas.append(total_diario_maquina) #lista de listas con las ventas diarias de todas las maquinas
        #print(total_int_)
        
        total_diario_maquinas = np.array(total_diario_maquinas)
        total_diario_maquinas = total_diario_maquinas.transpose()
        
        total_int_ = np.array(total_int_)
        total_int_ = total_int_.transpose()

        #print(total_int_)
        
        #print(total_diario_maquinas)    
        dic_device_ventas = {lista_fechas:total_diario_maquinas for (lista_fechas,total_diario_maquinas) in zip(lista_fechas,total_diario_maquinas)}     
        #print(dic_device_ventas)
        prueba = []
        
        for element in lista_fechas:
            prueba.append(str(element))
        diccionario2 = {prueba:total for (prueba,total) in zip(prueba,total_int_)}
        
        #print(diccionario2)
        
        context={
            'device_ventas':device_ventas, 
            'fecha_ini':fecha_ini,
            'fecha_fin':fecha_fin,
            'fechas':lista_fechas,
            'diccionario': dic_device_ventas,
            'device': device_str,
            'diccionario2': diccionario2,
            'valor_grafica': total_int_
        }
    else:
        context = {}
    return render(request, 'informes/comparacion.html', context)
    
from calendar import c, month
from decimal import Decimal
from multiprocessing import context
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
from django.db import connection
from django.db.models import Sum
from pytz import timezone

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

context1 = {}
context2 = {}

def inicio(request):
    return render(request, 'informes/inicio.html',{})

def about(request):   
    return render(request, 'informes/about.html',{})

def productos(request):
    tabla = models.TbProduct.objects.all().values_list('id_product', 'productname', 'id_category', 'productprice', named = True)
    context = {'tabla' : tabla}   
    return render(request, 'informes/productos.html',context)

def ventas(request):
    total  =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #esto se puede mejorar
    cant   =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #esto se puede mejorar
    device =    ['1','2','3','4','5','6','7','8','9','10','11','17','18','19','20','21','22','23','24']#id maquinas  #esto se puede mejorar
    cont   = 0
    gran_total = 0
    placas_total = 0
    
    date_range = request.POST.get('fecha')    
    #esto se puede mejorar
    if date_range != "default" and date_range != None:
        
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
            query = models.TbBilling.objects.filter(billingtransaciondate__range=(start_date, end_date)).select_related()
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
            
    #global context1  #variable global para generar pdf

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
            'estado': 1}
    
    else:
        context = {
           'estado': 0, 
        }
    print (date_range)
    return render(request, 'informes/ventas.html',context)

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
    
    # variables del template
    start_date = request.POST.get('fechainicial')
    end_date = request.POST.get('fechafinal')  
    check_box = request.POST.get('seleccion_rango')  
    semana = request.POST.get('semana')
    mes_ini = request.POST.get('mes_ini')  
    mes_fin = request.POST.get('mes_fin')   
        
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
       
    # Tomar los valores validos de device - genera lista con los nombres de la maquinas
    for dev in device:
        if dev is not None:
            device_new.append(int(dev))
            device_str.append("PET0"+dev)
                     
    if start_date != None and end_date != None: #Siempre y cuando halla valores seleccionados
              
        if check_box == "1": #opcion semanas
            pass
        
        if check_box == "2": #opcion meses
            fechas_iniciales = []
            fechas_finales   = []
            rango = "mensual"
            mes_ini = mes_ini + "-01" #fecha del mes inicial
            mes_fin = mes_fin + "-28" #fecha del mes final
            #convetimos a formato de fecha
            start_date2 = datetime.datetime.strptime(mes_ini, '%Y-%m-%d') 
            end_date2 = datetime.datetime.strptime(mes_fin, '%Y-%m-%d') 
            start_date3 = start_date2
            while(start_date2 < end_date2):
                fechas_iniciales.append(start_date2)
                mes = start_date2.month #mes en el que estoy
                mes2 = mes #mes 2 inicia en el mes en el que estoy
                control = 0
                while(control == 0): #itero el mes hasta el ultimo dia del mismo      
                    start_date2 = start_date2 + datetime.timedelta(days=1)
                    mes2 = start_date2.month
                    if mes == mes2:
                        copia = start_date2
                    else:
                        control = 1
                    
                fechas_finales.append(copia) # guardo el ultimo dia del mes
                #start_date2 = start_date2 + datetime.timedelta(days=1) # start date comienza en el siguiente mes
            
            for dev in device_new:
                total_ = 0
                querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(start_date3, end_date2)).select_related()
                for query in querys:
                    total_ = query.billingtotal + total_
                total_device.append(total_)

            device_ventas = {device_str:total_device for (device_str,total_device) in zip(device_str,total_device)}
            
            #Total de ventas por maquina - mes
            #generar lista con las fechas diarias segun rango seleccionado
            
            for dev in device_new: #recorre cada una de las maquinas
                
                total_diario_maquina = []
                total_int = []
                
                for i in range(len(fechas_iniciales)):# recorre fechas diarias 
                    
                    querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(fechas_iniciales[i], fechas_finales[i])).select_related()
                    subtotal_device = 0 #variable que almacena los subtotales
                    
                    for query in querys:# suma la cantidad de ventas del dia
                        subtotal_device = query.billingtotal + subtotal_device
                        
                    total_diario_maquina.append(subtotal_device) #lista con las ventas diarias de la maquina
                    total_int.append(int(subtotal_device))
                
                total_int_.append(total_int)
                total_diario_maquinas.append(total_diario_maquina) #lista de listas con las ventas diarias de todas las maquinas
            
            #creacion diccionario para generar las tablas
            total_diario_maquinas = np.array(total_diario_maquinas)
            total_diario_maquinas = total_diario_maquinas.transpose()
            dic_device_ventas = {fechas_iniciales:total_diario_maquinas for (fechas_iniciales,total_diario_maquinas) in zip(fechas_iniciales,total_diario_maquinas)}     
            
            total_int_ = np.array(total_int_)
            total_int_ = total_int_.transpose()
            fechas_transpuesta = []
            for element in fechas_iniciales:
                fechas_transpuesta.append(str(element))
            diccionario2 = {prueba:total for (prueba,total) in zip(fechas_transpuesta,total_int_)}
            
            context = {
                'device_ventas': device_ventas,
                'fecha_ini':mes_ini,
                'fecha_fin':mes_fin,
                'rango':rango,
                'diccionario': dic_device_ventas,
                'device': device_str,
                'diccionario2': diccionario2,
            }
                      
        if check_box == "3": #opcion rango fechas
            rango = "diario"
            start_date2 = datetime.datetime.strptime(start_date, '%Y-%m-%d') 
            end_date2 = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
            
            # Fechas en formato y - m - d para mostrar en el template
            fecha_ini = start_date2
            fecha_fin = end_date2         
            
            #Total de ventas por maquina y rango de fecha
            for dev in device_new:
                total_ = 0
                querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(start_date2, end_date2)).select_related()
                for query in querys:
                    total_ = query.billingtotal + total_
                total_device.append(total_)
            
            device_ventas = {device_str:total_device for (device_str,total_device) in zip(device_str,total_device)}

            #Total de ventas por maquina y dia
            #generar lista con las fechas diarias segun rango seleccionado
            while(stop != 1):
                
                lista_fechas.append(start_date2) 
                start_date2 = start_date2 + datetime.timedelta(days=1)
                
                if start_date2 == end_date2:
                    stop = 1

            for dev in device_new: #recorre cada una de las maquinas
                
                total_diario_maquina = []
                total_int = []
                
                for fecha_i in lista_fechas:# recorre fechas diarias 
                    fecha_f = fecha_i + datetime.timedelta(days=1)
                    querys = models.TbBilling.objects.filter(id_device=dev, billingtransaciondate__range=(fecha_i, fecha_f)).select_related()
                    subtotal_device = 0 #variable que almacena los subtotales
                    
                    for query in querys:# suma la cantidad de ventas del dia
                        subtotal_device = query.billingtotal + subtotal_device
                        
                    total_diario_maquina.append(subtotal_device) #lista con las ventas diarias de la maquina
                    total_int.append(int(subtotal_device))
                
                total_int_.append(total_int)
                total_diario_maquinas.append(total_diario_maquina) #lista de listas con las ventas diarias de todas las maquinas
            
            #creacion diccionario para generar las tablas
            total_diario_maquinas = np.array(total_diario_maquinas)
            total_diario_maquinas = total_diario_maquinas.transpose()
            dic_device_ventas = {lista_fechas:total_diario_maquinas for (lista_fechas,total_diario_maquinas) in zip(lista_fechas,total_diario_maquinas)}     
            
            #creacion diccionario para generar las graficas
            total_int_ = np.array(total_int_)
            total_int_ = total_int_.transpose()
            fechas_transpuesta = []
            for element in lista_fechas:
                fechas_transpuesta.append(str(element))
            diccionario2 = {prueba:total for (prueba,total) in zip(fechas_transpuesta,total_int_)}
            
            context={
                'device_ventas':device_ventas, 
                'fecha_ini':fecha_ini,
                'fecha_fin':fecha_fin,
                'diccionario': dic_device_ventas,
                'device': device_str,
                'diccionario2': diccionario2,
                'rango': rango
                    }
    else:
        context = {}
        
    return render(request, 'informes/comparacion.html', context)


def horas(request):
    
    #Criterios de busqueda seleccionados en el front
    #fecha seleccionada
    fecha_ini = request.POST.get("fecha_ini")
    #Maquinas seleccionadas
    maquinas = device(request)
    device_new = maquinas[0]
    device_str = maquinas[1]
    
    #Si hay una fecha seleccionada valida
    if fecha_ini != None: 
        #Contenedores
        horas = []
        cont = []
        dic = {}      
        #conversión de fecha
        fecha_ini_ = datetime.datetime.strptime(fecha_ini, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_fin_ = datetime.datetime.strptime(fecha_ini, '%Y-%m-%d').replace(hour=23, minute=59, second=59, microsecond=0)
        
        #Generar lista con los intervalos de tiempo en horas
        copia_fecha_ini_ = fecha_ini_
        while(copia_fecha_ini_<fecha_fin_):
            cont.append(copia_fecha_ini_)
            copia_fecha_ini_ = copia_fecha_ini_ + datetime.timedelta(hours=1)
            cont.append(copia_fecha_ini_)
            horas.append(cont)
            cont = []
    
        querys = models.TbBilling.objects.filter(billingtransaciondate__range=(fecha_ini_,fecha_fin_)).values_list('id_device','billingtotal','billingtransaciondate', named = True)
        
        for hora in horas: #Recorre el intervalo de fechas 
            for dev in device_new: #Recorre el numero de maquinas
                total = 0
                for query in querys: #recorre el query
                    #Siempre y cuando sea la maquina buscada dentro del tiempo establecido
                    if query.id_device == dev and query.billingtransaciondate >= hora[0] and query.billingtransaciondate <= hora [1]: #si 
                        total = total + query.billingtotal  
                cont.append(total) #
            dic[hora[0]] = cont
            cont = []

        context = {
            'querys' : dic,
            'device' : device_str}
        
    else:
        context = {}
        
    return render(request, 'informes/horas.html', context)

def maximos(request): 
    #Valores seleccionados en el front para el filtro
    chk = request.POST.get("seleccion_rango")
    fecha_ini = request.POST.get("fechainicial")
    fecha_fin = request.POST.get("fechafinal")
    dia = request.POST.get("dia")
    
    #función que devuelve los Id de las maquinas seleccionadas como String y Entero 
    maquinas = device(request)
    device_new = maquinas[0]
    device_str = maquinas[1]
    
    #En caso de seleccionar filtro por rango de fecha, siempre y cuando sea una fecha valida
    if chk == "1" and fecha_ini != "" and fecha_fin != "":
        cont = []
        dias = []
        maximos = []
        promedio = []
        totales = []
        dic = {}
        print("prueba2")
        #Rango de fechas para filtrar desde las 00:00:00 del dia inicial al 23:59:59 del dia final
        fecha_ini_ = datetime.datetime.strptime(fecha_ini, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_fin_ = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').replace(hour=23, minute=59, second=59, microsecond=0)
        
        #Generar lista con las fechas en intervalos de un dia entre fecha inicial y fecha final
        copia_fecha_ini_ = fecha_ini_
        while(copia_fecha_ini_ < fecha_fin_):
            cont.append(copia_fecha_ini_)
            copia_fecha_ini_ = copia_fecha_ini_ + datetime.timedelta(days=1)
            cont.append(copia_fecha_ini_)
            dias.append(cont)
            cont = []
        #print(dias)
        #consultar datos en rango de fechas
        querys = models.TbBilling.objects.filter(billingtransaciondate__range=(fecha_ini_,fecha_fin_)).values_list('id_device','billingtotal','billingtransaciondate', named = True)
        
        #filtrar informacion consultada por fecha y maquina
        for dia in dias:              #Recorre el intervalo de horas
            for dev in device_new:      #Recorre el numero de maquinas seleccionadas
                total = 0               #Reinicia el acumulador
                for query in querys:    #recorre el query
                    #Siempre y cuando sea la maquina buscada dentro del tiempo establecido
                    if query.id_device == dev and query.billingtransaciondate >= dia[0] and query.billingtransaciondate <= dia[1]:  
                        total = total + query.billingtotal #acumula las ventas que se encuentren en el rango de fechas y la maquina iterada  
                cont.append(total) #Agrega las ventas totales a un vector con que contiene las ventas de todas las maquinas consultada para un rango de tiempo
            totales.append(cont)
            dic[dia[0]] = cont #se relaciona el vector cont con el intervalo de tiempo correspondiente
            cont = []
        #print(dic)
        num_device = (len(device_new)) #Cantidad de maquinas consultadas
        
        #vectores vacios que contendran las estadisticas
        vector_maximos = [0]*num_device
        vector_fechas = [0]*num_device
        vector_sumatoria = [0]*num_device
        vector_contandor = [0]*num_device
        vector_promedio = [0]*num_device
   
        for x in dic:
            for y in range(num_device):
                #acumulador del total vendido de cada maquina                
                vector_sumatoria[y] = vector_sumatoria[y] + dic[x][y]
                #acumulador de numero de ventas 
                if dic[x][y] != 0:
                    vector_contandor[y] = vector_contandor[y] + 1 
                #acumulador con la mayor venta por maquina en rango de fecha
                if dic[x][y] > vector_maximos[y]:                                                                                                      
                    vector_fechas[y] = x
                    vector_maximos[y] = dic[x][y] 
        #Calcular el promedio de ventas
        for i in range(num_device):
            if vector_contandor[i] != 0:
                vector_promedio[i] = round((vector_sumatoria[i]/vector_contandor[i]),2)
            else: 
                vector_promedio[i] = 0
        
        #lista de listas con datos de ventas maximas y promedio       
        maximos.append(vector_fechas)
        maximos.append(vector_maximos)
        #promedio.append(vector_fechas)
        promedio.append(vector_promedio)
        
        context = {
            'querys'   :  dic,
            'device'   :  device_str,
            'maximos'  :  maximos,
            'promedio' :  promedio,
            'total'    :  vector_sumatoria,
            'condicion':  1,
            'rango'    :  "DIAS" 
        }
        
     
    #En caso de seleccionar filtro por dia, siempre y cuando sea una fecha valida
    elif chk == "2" and dia != "":
        maximos = []
        promedio = []
        horas = []
        dic = {}
        cont = []
        totales = []
        
        #rango de fecha desde las 00:00:00 hasta las 23:59:59
        fecha_ini_ = datetime.datetime.strptime(dia, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_fin_ = datetime.datetime.strptime(dia, '%Y-%m-%d').replace(hour=23, minute=59, second=59, microsecond=0)
        print("hora:")
        print(type(fecha_fin_.hour))
        #Generar lista con los intervalos de tiempo en horas
        copia_fecha_ini_ = fecha_ini_
        while(copia_fecha_ini_<fecha_fin_):
            cont.append(copia_fecha_ini_)
            copia_fecha_ini_ = copia_fecha_ini_ + datetime.timedelta(hours=1)
            cont.append(copia_fecha_ini_)
            horas.append(cont)
            cont = []
        
        #Consulta con los datos de la tabla de ventas en el rango de fecha seleccionado  
        querys = models.TbBilling.objects.filter(billingtransaciondate__range=(fecha_ini_,fecha_fin_)).values_list('id_device','billingtotal','billingtransaciondate', named = True)
        #Filtro de datos en base al query
        for hora in horas:              #Recorre el intervalo de horas
            for dev in device_new:      #Recorre el numero de maquinas seleccionadas
                total = 0               #Reinicia el acumulador
                for query in querys:    #recorre el query
                    #Siempre y cuando sea la maquina buscada dentro del tiempo establecido
                    if query.id_device == dev and query.billingtransaciondate >= hora[0] and query.billingtransaciondate <= hora [1]: #si 
                        total = total + query.billingtotal #acumula las ventas que se encuentren en el rango de fechas y la maquina iterada  
                cont.append(total) #Agrega las ventas totales a un vector con que contiene las ventas de todas las maquinas consultada para un rango de tiempo
            totales.append(cont)
            if hora[1].hour < 10 and hora[1] != 0:
                hour = "0"+str(hora[1].hour)+":0"+str(hora[1].minute)+":0"+str(hora[1].second)
            else:
                hour = str(hora[1].hour)+":0"+str(hora[1].minute)+":0"+str(hora[1].second)
            dic[hour] = cont #se relaciona el vector cont con el intervalo de tiempo correspondiente
            cont = []
        
        num_device = (len(device_new)) #Cantidad de maquinas consultadas
        
        #vectores vacios que contendran las estadisticas
        vector_maximos = [0]*num_device
        vector_fechas = [0]*num_device
        vector_sumatoria = [0]*num_device
        vector_contandor = [0]*num_device
        vector_promedio = [0]*num_device
   
        for x in dic:
            for y in range(num_device):
                #acumulador del total vendido de cada maquina                
                vector_sumatoria[y] = vector_sumatoria[y] + dic[x][y]
                #acumulador de numero de ventas 
                if dic[x][y] != 0:
                    vector_contandor[y] = vector_contandor[y] + 1 
                #acumulador con la mayor venta por maquina en rango de fecha
                if dic[x][y] > vector_maximos[y]:                                                                                                      
                    vector_fechas[y] = x
                    vector_maximos[y] = dic[x][y] 
        #Calcular el promedio de ventas
        for i in range(num_device):
            if vector_contandor[i] != 0:
                vector_promedio[i] = round((vector_sumatoria[i]/vector_contandor[i]),2)
            else: 
                vector_promedio[i] = 0
        
        #lista de listas con datos de ventas maximas y promedio       
        maximos.append(vector_fechas)
        maximos.append(vector_maximos)
        #promedio.append(vector_fechas)
        promedio.append(vector_promedio)
        
        context = {
            'querys'   :  dic,
            'device'   :  device_str,
            'maximos'  :  maximos,
            'promedio' :  promedio,
            'total'    :  vector_sumatoria,
            'condicion':  1,
            'rango'    :  "HORA" 
        }
    #En caso de no seleccionarse una fecha valida  
    else:
        context = {
            'condicion': 0,
        }
    
    return render(request,'informes/maximos.html',context)

#Validación de los checkbox seleccionados 
def device(request):
    #contenedores
    device_new = []
    device_str = []
    device_full = []
    #Consulta el estado de los Check Box
    device = [
        request.POST.get("cbox1"), request.POST.get("cbox2"), request.POST.get("cbox3"),
        request.POST.get("cbox4"), request.POST.get("cbox5"), request.POST.get("cbox6"),
        request.POST.get("cbox7"), request.POST.get("cbox8"), request.POST.get("cbox9"),
        request.POST.get("cbox10"), request.POST.get("cbox11"), request.POST.get("cbox12"),
        request.POST.get("cbox13"), request.POST.get("cbox14"), request.POST.get("cbox15"),
        request.POST.get("cbox16"), request.POST.get("cbox17"), request.POST.get("cbox18"),
        request.POST.get("cbox19"), request.POST.get("cbox20"), request.POST.get("cbox21"),]
    #Filtrar maquinas seleccionadas y convertir a Int y Str
    for dev in device:
        if dev != None:
            device_new.append(int(dev))
            device_str.append("PET0"+dev)
    #Agregar a la informacion de selección a una lsita de lista 
    device_full.append(device_new)
    device_full.append(device_str)
    
    return (device_full)

def pdf(request):
    template = get_template('informes/ventas.html')
    html = template.render(context1)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_ventas.pdf"'
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    return response

def pdf2(request):
    template = get_template('informes/maquinas.html')
    html = template.render(context2)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_maquinas.pdf"'
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    return response
    
    
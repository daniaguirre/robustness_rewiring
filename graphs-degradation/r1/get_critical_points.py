import sys
import csv

def loadData(dFile):
    data=[[],[],[],[],[],[],[],[]]  #Contiene todos los datos menos asortatividad y conectividad
    with open(dFile, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Elimino las etquetas de los datos

        for values in reader:
            data[0].append(int(values[0]))      # Number of nodes
            data[1].append(int(values[1]))      # Number of edges
            data[2].append(float(values[2]))    # Average shortests path length
            data[3].append(int(values[3]))      # Diameter
            data[4].append(float(values[4]))    # Average clustering coefficient      
            data[5].append(int(values[7]))      # Number of components
            data[6].append(int(values[8]))      # Order of largest component
    return data

# Archivo donde se guardaran los datos
output1_csv = "puntos_criticos_r1_fallos.csv"
output2_csv = "puntos_criticos_r1_ataques.csv"

# Preparamos el archivo CSV para escribir los datos de fallos
with open(output1_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Escribir encabezados
    csvwriter.writerow(["enlace","experimento","secuencia","pci", "pcm", "pcf"])
    for enlace in [1,2,4,8,16,32]:
        for experimento in range (1,11):
            for secuencia in range (1,11):
                degData = loadData("enlaceD{}//experimento{}//fallos/{}/degradationData.csv".format(enlace,experimento,secuencia))
                pci = 0     # Punto critico al inicio
                pcm = 0     # Punto critico a la mitad
                pcf = 0     # Punto critico al final

                for i in range(101):
                    #div = float(degData[6][i])/float(degData[0][i])   # Anterior  S_i/(n-i)
                    print("enlaceD{}//experimento{}//fallos/{}/degradationData.csv_{}".format(enlace,experimento,secuencia,i))
                    div = float(degData[6][i])/float(degData[0][0])     # Nuevo S_i/n
    
                    if div<0.90 and pci==0:
                        pci=i
                    if div<0.5 and pcm==0:
                        pcm=i
                    if div<0.1 and pcf==0:
                        pcf=i
                #print (pci," ",pcm," ",pcf)
                # Guardar los valores en el CSV
                csvwriter.writerow([enlace,experimento,secuencia,pci, pcm, pcf])

# Preparamos el archivo CSV para escribir los datos de ataques
with open(output2_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Escribir encabezados
    csvwriter.writerow(["enlace","experimento","secuencia","pci", "pcm", "pcf"])
    for enlace in [1,2,4,8,16,32]:
        for experimento in range (1,11):
            for secuencia in range (1,2):
                degData = loadData("enlaceD{}//experimento{}//ataques/{}/degradationData.csv".format(enlace,experimento,secuencia))
                pci = 0     # Punto critico al inicio
                pcm = 0     # Punto critico a la mitad
                pcf = 0     # Punto critico al final

                for i in range(101):
                    div = float(degData[6][i])/float(degData[0][i])   # Anterior
                    #div = float(degData[6][i])/float(degData[0][0])     # Nuevo S_i/S_0
                        
                    if div<0.90 and pci==0:
                        pci=i
                    if div<0.5 and pcm==0:
                        pcm=i
                    if div<0.1 and pcf==0:
                        pcf=i
                #print (pci," ",pcm," ",pcf)
                # Guardar los valores en el CSV
                csvwriter.writerow([enlace,experimento,secuencia,pci, pcm, pcf])


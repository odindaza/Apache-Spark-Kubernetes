# Proyecto Spark en Kubernetes

Este proyecto implementa un clúster de Apache Spark utilizando Kubernetes y Minikube para la orquestación de los contenedores. Incluye un Spark Master y un Spark Worker, así como un script en Python para realizar procesamiento batch sobre un conjunto de datos.

---

## 🚀 Requisitos previos

Antes de iniciar, asegúrate de contar con lo siguiente instalado en tu entorno:

- [Minikube](https://minikube.sigs.k8s.io/docs/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Docker](https://www.docker.com/)
- [Python 3](https://www.python.org/) - [PySpark](https://spark.apache.org/docs/latest/api/python/) - [Py4j](https://www.py4j.org/)

---

## 📂 Estructura del proyecto

📦 Proyecto 

- spark-setup.yaml
-  script.py
- README.md

---
## ⚙️ Configuración de Kubernetes

### 1. Iniciar Minikube
Ejecuta el siguiente comando para iniciar Minikube con suficiente memoria y CPU:
```bash
minikube start
```

### 2. Aplicar la configuración YAML
Despliega los Pods y el Service para el Spark Master y Worker:
```
kubectl apply -f spark-setup.yaml
```

### 3. Verificar los recursos desplegados
Asegúrate de que los Pods y Services estén en ejecución
```
kubectl get pods
kubectl get services
```

### 4. Port Forwarding para visualizar la interfaz en la web
Realiza el port forwarding desde el Pods master para visualizar la interfaz de manera local.
```
kubectl port-forwarding pod/spark-master 8080:8080
```

## 🐍 Ejecución del script en Python
### Descripción
El script en Python realiza limpieza de datos, transformación y calcula promedios agrupados por género en un conjunto de datos en formato CSV.
#### Comando de ejecución
Conectate primero al spark-master de la siguiente manera:
```
kubectl exec -it spark-master -- sh
```
Instala el paquete Py4j usando pip en el spark-master:
```
pip install py4j
```
Copia el [dataset](https://www.datos.gov.co/Seguridad-y-Defensa/Reporte-Capturas-Polic-a-Nacional-de-Colombia/cukt-wz9m/about_data) y script en el spark-master con el siguiente comando:
```
kubectl cp [NAME DATASET] spark-master:/tmp/[NAME DATASET]
kubectl cp [SCRIPT NAME] spark-master:/tmp/[SCRIPT NAME]
```
Utiliza el siguiente comando para ejecutar el script:
```
python3 script.py [NAME DATASET]
```



### Resultados
El resultado será guardado en un archivo llamado reported.parquet.

## 💡 Observaciones
- Asegúrate de que los Workers estén registrados correctamente en la interfaz web del Spark Master (http://localhost:8080).
- El dataset debe estar en formato CSV y contener las columnas esperadas para el procesamiento.


## 🛠️ Solución de problemas
Advertencia: Initial job has not accepted any resources
- Verifica que los Workers tengan recursos suficientes configurados en el archivo YAML.
- Revisa la conectividad entre el Worker y el Master.

Error: No Workers found in the Spark Master UI
- Asegúrate de que los Pods del Worker estén en ejecución y conectados al Master correctamente.


## 🏗️ Futuras mejoras
- Escalabilidad: Implementar un Deployment en lugar de Pods independientes.
- Optimización de recursos: Ajustar dinámicamente según la carga.
- Ampliación: Añadir más Workers para aumentar la capacidad de procesamiento.


## 👤 Autor
Este proyecto fue creado como parte de una actividad de aprendizaje sobre Kubernetes y Apache Spark. Si tienes preguntas o sugerencias, ¡estaré encantado de recibirlas!

Espero que este archivo cumpla con tus expectativas. Si necesitas que ajuste algo o añada más detalles, ¡solo avísame! 😊✨



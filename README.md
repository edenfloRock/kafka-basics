# kafka-basics
Proyecto simple para implementación de Kafka con el API de confluent_kafka.

---

## Descripción
Este proyecto contiene los ejercicios de un curso de Kafka con Python.

---

## Componentes

### Componente 1: test_topic.py
**Descripción:**  
Script que genera un nuevo Topic.


1. **Ejemplo ejecución**
    ```bash
    python test_topic.py Mundial4 --partitions 3

---

### Componente 2: test_producer.py
**Descripción:**  
Script que genera un Producer especificando el tópico y el mensaje.

1. **Ejemplo ejecución**
    ```bash
    python test_producer.py Mundial4 Mensaje1

---

### Componente 3: test_producer_partition.py
**Descripción:**  
Script que genera un Producer especificando el tópico, mensaje y el número de partición a escribir.

1. **Ejemplo ejecución**
    ```bash
    python test_producer_partition.py Mundial4 Mensaje8 0 

---

### Componente 4: test_producer_partition_key.py
**Descripción:**  
Script que genera un Producer especificando el tópico, mensaje en formato clave:valor y el número de partición a escribir.

1. **Ejemplo ejecución**
    ```bash
    python test_producer_partition_key.py Mundial4 Ciudad CDMX 2 

---
### Componente 5: test_consumer.py
**Descripción:**  
Script que genera un Consumer especficando el tópico y grupo.

1. **Ejemplo ejecución**
    ```bash
    python test_consumer.py Mundial4 mensajes
---
### Componente 6: test_consumer_.py
**Descripción:**  
Script que genera un Consumer especificando el tópico, grupo y el número de Partición a leer.

1. **Ejemplo ejecución**
    ```bash
    python test_consumer_multiple.py Mundial4 mensajes 1  
---
## Ejecución de Comandos
Para ejecutar este proyecto, sigue los comandos en el siguiente orden:

1. **Instalar dependencias:**  
   ```bash
   pip install -r requirements.txt

2. **Preparar inicio de cluster de Kafka:**
    ```bash
    kafka-storage.sh random-uuid

    kafka-storage.sh format -t random-uuid -c ~/kafka_2.12-3.9.0/config/kraft/server.properties

3. **Iniciar cluster**
    ```bash
    kafka-server-start.sh ~/kafka_2.12-3.9.0/config/kraft/server.properties

4. **Ejecutar script para crear el tópico**

5. **Ejecutar script para ejecutar el Productor**

6. **Ejecutar script para ejecutar el Consumidor**

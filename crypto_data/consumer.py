from confluent_kafka import Consumer
import csv
import json
import time

topic_name = 'cryptodata'
group_id = 'grupocrypto'

consumer_conf = {'bootstrap.servers':'localhost:9092', 'group.id': group_id, 'auto.offset.reset': 'earliest'}
consumer = Consumer(consumer_conf)
consumer.subscribe([topic_name])

csv_file_path = 'crypto_precios.csv'

with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['timestamp', 'name', 'symbol', 'price'])
    
    if not csv_file.tell():
        writer.writeheader()
        
    # Consume mensajes de Kafka y escribe el csv
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print('Error: {}'.format(msg.error()))
                continue
            
            row = json.loads(msg.value())
            writer.writerow(row)
            print(f'Datos recibidos y escritos en {csv_file_path}')
            
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        time.sleep(2)
        
    
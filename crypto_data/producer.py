from confluent_kafka import Producer
import requests
import json
import time

# Lista de cryptos a revisar
cryptos_to_track = [
    'bitcoin', 
    'ethereum', 
    'ripple', 
    'litecoind', 
    'cardeno', 
    'polkadot', 
    'stellar', 
    'eos', 
    'tron', 
    'dogecoin'
    ]

api_url = 'https://api.coincap.io/v2/assets'

producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)
topic_name = 'cryptodata'

#Evalua cada una de las monedas
while True:

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
                
        # Verificar la estructura de la respuesta
        if 'data' in data and isinstance(data['data'], list):
            # Se crea una lista de diccionarios        
            rows = [{'timestamp': int(time.time()), 
                    'name': crypto['name'],
                    'symbol': crypto['symbol'],
                    'price': crypto['priceUsd']
                    }
                    for crypto in data['data'] if crypto['id'] in cryptos_to_track
                    ]
            
            # Se manda la info a Kafka
            for row in rows:
                producer.produce(topic_name, value=json.dumps(row))
            
            producer.flush()
            print('Datos enviados exitósamente a Kafka')
        else:
            print('La estructura de la respuesta no es la correcta')
        
    else:
        print(f'Error al realizar la solicitud a la API. Código de estado: {response.status_code}')
        
    time.sleep(30)

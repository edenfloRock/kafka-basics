import argparse
from confluent_kafka import Consumer

def main():

    parser = argparse.ArgumentParser(description='Genera un mensaje en kafka')
    parser.add_argument('nombre_topic', type=str, help='Nombre del tópico')
    parser.add_argument('grupo_consumer', type=str, help='Grupo Consumidor')
        
    args = parser.parse_args()

    c = Consumer ({'bootstrap.servers':'localhost:9092', 'group.id': args.grupo_consumer, 'auto.offset.reset':'earliest'})
    c.subscribe([args.nombre_topic])
    
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                print('No hay mensaje, sigo escuchando...')
                continue
            print(f"Clave Mensaje: {msg.key().decode('utf-8')}")
            print(f"Valor Mensaje: {msg.value().decode('utf-8')}")
            print(f"Partición: {msg.partition()}")
            print(f"Offset: {msg.offset()}")
    except KeyboardInterrupt:
        pass
    finally:
        c.close()

if __name__ == '__main__':
    main()

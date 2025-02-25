import argparse
from confluent_kafka import Consumer, TopicPartition

def main():

    parser = argparse.ArgumentParser(description='Genera un mensaje en kafka')
    parser.add_argument('nombre_topic', type=str, help='Nombre del tópico')
    parser.add_argument('grupo_consumer', type=str, help='Grupo Consumidor')
    parser.add_argument('partition_ID', type=int, help='ID de partición' )
        
    args = parser.parse_args()

    c = Consumer ({'bootstrap.servers':'localhost:9092', 'group.id': args.grupo_consumer, 'auto.offset.reset':'earliest'})
    #c.subscribe([args.nombre_topic])
    c.assign([TopicPartition(args.nombre_topic, args.partition_ID)])
    
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                print('No hay mensaje, sigo escuchando...')
                continue
            print(f"Clave Mensaje: {msg.key()}")
            print(f"Valor Mensaje: {msg.value().decode('utf-8')}")
            print(f"Partición: {msg.partition()}")
            print(f"Offset: {msg.offset()}")
    except KeyboardInterrupt:
        pass
    finally:
        c.close()

if __name__ == '__main__':
    main()

import argparse
from confluent_kafka import Producer

def main():

    parser = argparse.ArgumentParser(description='Genera un mensaje en kafka')
    parser.add_argument('nombre_topic', type=str, help='Nombre del tópico')
    parser.add_argument('mensaje', type=str, help='Mensaje')
    parser.add_argument('particion_ID', type=int, help='Número de Partición en la que escribe')
    
    args = parser.parse_args()

    p = Producer ({'bootstrap.servers':'localhost:9092'})
    p.produce(topic = args.nombre_topic, value= args.mensaje, partition = args.particion_ID)
    p.flush()

if __name__ == '__main__':
    main()

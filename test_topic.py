
import argparse
from confluent_kafka.admin import AdminClient, NewTopic


def createTopic(topic_name, num_partitions):
    print(f"Topic Name: {topic_name}")
    print(f"Partitions: {num_partitions}")
    
    admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

    #Crea Topic con x particiones        
    nuevo_topic = NewTopic(topic=topic_name, num_partitions=num_partitions)

    result = admin_client.create_topics(new_topics=[nuevo_topic])


    #Imprime el resultado
    for topic, future in result.items():
        try:
            future.result() #Esto lanza una excepción si hay un error
            print(f'Se ha creado el topic {topic_name} con {num_partitions} particiones.')
        except Exception as e:
            print(f'No se pudo crear el topic {topic}. Error: {e}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="argparse")

    parser.add_argument("topic_name", help="Topic name")
    parser.add_argument("--partitions", type=int, default=1, help="Number of partitions")

    args = parser.parse_args()

    createTopic(args.topic_name, args.partitions)


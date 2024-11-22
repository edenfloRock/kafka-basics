import argparse
from confluent_kafka import Producer


def createProduce (topic_name, message):
    print(f"Topic Name: {topic_name}")
    print(f"Message: {message}")
    
    p = Producer ({'bootstrap.servers':'localhost:9092'})

    p.produce(topic=topic_name,value=message)
    p.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="argparse")

    parser.add_argument("topic_name", help="Topic name")
    parser.add_argument("message", help="Message")

    args = parser.parse_args()

    createProduce(args.topic_name, args.message)
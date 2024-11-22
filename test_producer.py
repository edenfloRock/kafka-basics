from confluent_kafka import Producer

p = Producer ({'bootstrap.servers':'localhost:9092'})

p.produce('TestTopic2', 'Mensaje de prueba 3')
p.flush()
from kafka import KafkaProducer
kafka_server="localhost:9092"
producer = KafkaProducer(bootstrap_servers=kafka_server)
topic = 'awesomefeeds'
producer.send(topic,b'u r awesome')


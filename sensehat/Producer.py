
from kafka import KafkaConsumer, KafkaProducer

def publish_message(producer_instance, topic_name, key, value):
    print("Publish Message=" + value)
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['192.168.1.19:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

topic = "foobar1"
key = 'sensor2'
value = "Hello From Python on 192.168.1.19"
kafka_producer = connect_kafka_producer()
publish_message(kafka_producer, topic, 'key', value)

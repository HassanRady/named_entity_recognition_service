import sys
from confluent_kafka import Consumer, Producer, KafkaError, KafkaException
from config import settings
from ner_extractor import pipeline
import json
from logger import get_file_logger


logger = get_file_logger(__name__, 'logs')

def value_serializer(value):
    return json.dumps(value).encode('utf-8') 

def value_deserializer(value):
    return json.loads(value.decode('utf-8'))

consumer_conf = {
    'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
    'group.id': settings.KAFKA_NER_CONSUMER_GROUP,
    'auto.offset.reset': settings.KAFKA_AUTO_OFFSET_RESET,
}

producer_conf = {
    'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
}

consumer = Consumer(consumer_conf)
consumer.subscribe([settings.KAFKA_STREAM_TEXT_TOPIC])

producer = Producer(producer_conf)


def process_msg(msg):
    data = value_deserializer(msg.value())
    keywords = pipeline(data['text'])
    if not keywords['output']:
        return
    return value_serializer(keywords)

running = True

def consume_produce_loop(consumer, consume_topics, produce_topic):
    try:
        consumer.subscribe(consume_topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.error('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                value = process_msg(msg)
                if not value:
                    continue
                producer.produce(produce_topic, value)
    finally:
        consumer.close()
        producer.flush()

def shutdown():
    running = False

if __name__ == '__main__':
    consume_produce_loop(consumer, [settings.KAFKA_STREAM_TEXT_TOPIC], settings.KAFKA_NER_TOPIC)
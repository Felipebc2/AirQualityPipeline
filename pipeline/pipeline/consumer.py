import json
from kafka import KafkaConsumer

KAFKA_BROKERS = ['localhost:9092', 'localhost:9093']
TOPIC = 'airquality'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKERS,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

if __name__ == "__main__":
    print("Consumindo mensagens do Kafka...")
    for message in consumer:
        data = message.value
        print(f"Recebido: {data}")
        # Aqui você pode chamar funções para armazenar no Redis, MinIO, etc.

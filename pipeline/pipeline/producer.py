import json
import time
import random
from kafka import KafkaProducer

# Configurações Kafka
KAFKA_BROKERS = ['localhost:9092', 'localhost:9093']
TOPIC = 'airquality'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sensor_ids = [1, 2, 3, 4, 5]

def generate_sensor_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "CO": round(random.uniform(0, 20), 2),
        "NO2": round(random.uniform(0, 300), 2),
        "timestamp": int(time.time())
    }

if __name__ == "__main__":
    while True:
        for sensor_id in sensor_ids:
            data = generate_sensor_data(sensor_id)
            producer.send(TOPIC, value=data)
            print(f"Enviado: {data}")
        producer.flush()
        time.sleep(5)

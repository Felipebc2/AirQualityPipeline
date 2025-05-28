import json
import time

from .storage import store_to_redis, store_to_minio
from .alert_handler import check_alerts

# Simula dados recebidos da fonte (ex: Kafka consumer)
def receive_sensor_data():
    # Normalmente aqui vai o código que consome mensagens Kafka,
    # mas para simplificar vamos gerar dados fictícios:
    sample_data = [
        {"sensor_id": 1, "CO": 8, "NO2": 190, "timestamp": time.time()},
        {"sensor_id": 2, "CO": 12, "NO2": 220, "timestamp": time.time()},
        {"sensor_id": 3, "CO": 5, "NO2": 100, "timestamp": time.time()},
    ]
    for d in sample_data:
        yield d
        time.sleep(1)  # simula intervalo entre dados


def main():
    for data in receive_sensor_data():
        # Salvar dados
        store_to_redis(data)
        store_to_minio(data)

        # Checar alertas
        alerts = check_alerts(data)
        if alerts:
            for alert in alerts:
                print(alert)


if __name__ == "__main__":
    main()

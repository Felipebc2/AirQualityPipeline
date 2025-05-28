def check_alerts(data):
    alerts = []

    # Definir limites críticos para os sensores
    CO_LIMIT = 10
    NO2_LIMIT = 200

    co = data.get('CO', 0)
    no2 = data.get('NO2', 0)

    if co > CO_LIMIT:
        alerts.append(f"⚠️ Alerta Crítico: CO alto ({co})")
    if no2 > NO2_LIMIT:
        alerts.append(f"⚠️ Alerta Crítico: NO2 alto ({no2})")

    return alerts


# Exemplo de uso
if __name__ == "__main__":
    sample_data = {
        'sensor_id': 1,
        'CO': 12,
        'NO2': 180
    }

    alerts = check_alerts(sample_data)
    for alert in alerts:
        print(alert)

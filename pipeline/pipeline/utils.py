from datetime import datetime

def timestamp_to_str(ts):
    """Converte timestamp UNIX para string legível."""
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def validate_sensor_data(data):
    """Valida dados básicos do sensor, retorna True se ok, False caso contrário."""
    required_keys = ['sensor_id', 'CO', 'NO2', 'timestamp']
    for key in required_keys:
        if key not in data:
            return False
    # Pode incluir outras validações, como tipo, faixa de valores, etc.
    if not isinstance(data['sensor_id'], int):
        return False
    if not (0 <= data['CO'] <= 100):
        return False
    if not (0 <= data['NO2'] <= 500):
        return False
    if not isinstance(data['timestamp'], (int, float)):
        return False
    return True

def format_alert_message(data, pollutant, value, threshold):
    """Formata mensagem de alerta para poluente que ultrapassou o limite."""
    ts_str = timestamp_to_str(data['timestamp'])
    return (f"⚠️ Alerta! Sensor {data['sensor_id']} detectou {pollutant} em {value}, "
            f"ultrapassando o limite de {threshold} em {ts_str}.")

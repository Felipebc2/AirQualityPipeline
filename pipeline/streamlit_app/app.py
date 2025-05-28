# import streamlit as st
# import redis
# import json

# st.set_page_config(page_title="Monitor de Qualidade do Ar", layout="wide")
# st.title("🌬️ Monitor de Sensores de Qualidade do Ar")

# # Se rodar local, use localhost
# r = redis.Redis(host='redis', port=6379, db=0)

# sensor_ids = [1, 2, 3, 4, 5]

# cols = st.columns(len(sensor_ids))

# for i, sensor_id in enumerate(sensor_ids):
#     key = f"sensor:{sensor_id}"
#     data_raw = r.get(key)
#     data_raw = r.get("sensor:1")
#     print(json.loads(data_raw))
#     print(f"Raw data for {key}: {data_raw}")
#     if data_raw:
#         print(f"Parsed data for {key}: {data}")
#         data = json.loads(data_raw)
#         with cols[i]:
#             st.metric(label=f"Sensor {sensor_id}", value=f"CO: {data['CO']} | NO2: {data['NO2']}")
#             if data['CO'] > 10 or data['NO2'] > 200:
#                 st.error("⚠️ Alerta Crítico!")
#     else:
#         with cols[i]:
#             st.warning("Sem dados disponíveis")
import streamlit as st
import redis
import json
import os
st.set_page_config(page_title="Monitor de Qualidade do Ar", layout="wide")
st.title("🌬️ Monitor de Sensores de Qualidade do Ar")

# Se rodar local, usar localhost
r = redis.Redis(host=os.getenv('REDIS_HOST'), port=6379, db=0)

sensor_ids = [1, 2, 3, 4, 5]

cols = st.columns(len(sensor_ids))

for i, sensor_id in enumerate(sensor_ids):
    key = f"sensor:{sensor_id}"
    data_raw = r.get(key)
    if data_raw:
        data = json.loads(data_raw)
        with cols[i]:
            st.metric(label=f"Sensor {sensor_id}", value=f"CO: {data['CO']} | NO2: {data['NO2']}")
            if data['CO'] > 10 or data['NO2'] > 200:
                st.error("⚠️ Alerta Crítico!")
    else:
        with cols[i]:
            st.warning("Sem dados disponíveis")

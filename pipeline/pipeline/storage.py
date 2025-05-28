import redis
import json
import os
from minio import Minio
from .config import REDIS_HOST, REDIS_PORT, REDIS_DB
from .config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET

# Conexão Redis
r = redis.Redis(host='redis', port=6379 , db=0)

# Conexão MinIO
minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

BUCKET = MINIO_BUCKET

if not minio_client.bucket_exists(BUCKET):
    minio_client.make_bucket(BUCKET)

def store_to_redis(data):
    key = f"sensor:{data['sensor_id']}"
    r.set(key, json.dumps(data))
    print("✅ Dados armazenados no Redis.")

def store_to_minio(data):
    filename = f"{data['sensor_id']}_{int(data['timestamp'])}.json"
    filepath = f"/tmp/{filename}"
    with open(filepath, 'w') as f:
        json.dump(data, f)

    minio_client.fput_object(BUCKET, filename, filepath)
    os.remove(filepath)
    print("📦 Dados salvos no MinIO.")

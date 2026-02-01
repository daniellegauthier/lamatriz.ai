# backend/api/cache.py
from django.core.cache import cache
import uuid

def store_png(png_bytes: bytes, ttl: int = 300) -> str:
    key = f"gnh_plot_{uuid.uuid4().hex}"
    cache.set(key, png_bytes, timeout=ttl)
    return key

def load_png(key: str) -> bytes | None:
    return cache.get(key)

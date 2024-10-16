"""Get names for methods from Metriq"""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.method_get_names()
assert result is not None

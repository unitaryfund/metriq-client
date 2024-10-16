"""Get task by ID on Metriq."""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.task_get(4)
assert result is not None

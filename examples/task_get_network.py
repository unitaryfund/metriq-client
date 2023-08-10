from metriq import MetriqClient
import os

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.task_get_network()
assert result is not None

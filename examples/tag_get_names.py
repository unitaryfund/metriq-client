from metriq import MetriqClient
import os

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.tag_names_get()
assert result is not None


from metriq import MetriqClient
import os

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.method_get("6101c6ac1134861ba8fbdd9e")
assert result is not None

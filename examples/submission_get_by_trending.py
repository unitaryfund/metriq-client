from metriq import MetriqClient
import os

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_get_by_trending()
assert result is not None

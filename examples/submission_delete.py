"""Delete submission from Metriq."""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_delete("6116cc3b8d4c8079d6b4f618")
assert result.response.ok

"""Get submissions sorted by popularity on Metriq."""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_get_by_popular()
assert result is not None

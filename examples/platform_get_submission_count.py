"""Get submission count for platform from Metriq."""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.platform_get_submission_count()
assert result is not None

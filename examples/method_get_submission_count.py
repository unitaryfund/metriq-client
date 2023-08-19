"""Get submission count from method from Metriq."""
import os
from metriq import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.method_get_submission_count()
assert result is not None

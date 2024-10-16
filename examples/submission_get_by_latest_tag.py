"""Get submission by latest tag on Metriq."""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_get_by_latest_tag("ground state energy")
assert result is not None

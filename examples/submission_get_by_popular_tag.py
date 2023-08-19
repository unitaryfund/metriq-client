"""Get submission by popular tag on Metriq."""
import os
from metriq import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_get_by_popular_tag("ground state energy")
assert result is not None

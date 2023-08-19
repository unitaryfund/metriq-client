"""Upvote submission by ID on Metriq."""
import os
from metriq import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_upvote("6116cc3b8d4c8079d6b4f618")
assert result is not None


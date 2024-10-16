"""Test "hello" route for Metriq API."""
import os
from metriq_client import MetriqClient


client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.metriq_hello()
assert result is not None

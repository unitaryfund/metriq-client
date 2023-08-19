"""Add method to submission on Metriq."""
import os
from metriq import MetriqClient


submission_id = "1234567890"
method_id = "2345678901"
client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_add_method(submission_id=submission_id, method_id=method_id)
assert result is not None

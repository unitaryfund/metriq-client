"""Add task to submission on Metriq."""
import os
from metriq_client import MetriqClient


submission_id = "1234567890"
task_id = "2345678901"
client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_add_task(submission_id=submission_id, task_id=task_id)
assert result is not None

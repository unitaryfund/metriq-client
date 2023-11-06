"""Add result to Metriq."""
import os
from metriq import MetriqClient
from metriq.models.result import ResultCreateRequest


result = ResultCreateRequest()
result.task = "176"
result.method = "84"
result.metricName = "Test Metric"
result.metricValue = "10"
result.evaluatedAt = "2021-07-22"
result.isHigherBetter = "true"
result.qubitCount = "2"

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
submission_id = "1234567890"
result = client.result_add(result, submission_id)
assert result is not None

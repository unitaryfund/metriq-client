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

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.result_add(result)
assert result is not None
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

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.result_add(result))

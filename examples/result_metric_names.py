from metriq import MetriqClient
from metriq.models.result import ResultCreateRequest

# Result Item 1
result1 = ResultCreateRequest()
result1.task = "176"
result1.method = "84"
result1.metricName = "Test Metric 1"
result1.metricValue = "10"
result1.evaluatedAt = "2021-07-22"
result1.isHigherBetter = "true"
result1.qubitCount = "3"

# Result Item 2
result2 = ResultCreateRequest()
result2.task = "177"
result2.method = "84"
result2.metricName = "Test Metric 2"
result2.metricValue = "10"
result2.evaluatedAt = "2021-07-23"
result2.isHigherBetter = "true"
result2.qubitCount = "5"

# Result Item 3
result3 = ResultCreateRequest()
result3.task = "178"
result3.method = "84"
result3.metricName = "Test Metric 3"
result3.metricValue = "10"
result3.evaluatedAt = "2021-07-24"
result3.isHigherBetter = "true"
result3.qubitCount = "2"

# Result Item 4
result4 = ResultCreateRequest()
result4.task = "179"
result4.method = "84"
result4.metricName = "Test Metric 4"
result4.metricValue = "10"
result4.evaluatedAt = "2021-07-25"
result4.isHigherBetter = "true"
result4.qubitCount = "4"

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
client.result_add(result1)
client.result_add(result2)
client.result_add(result3)
client.result_add(result4)
result = client.result_metric_names()
assert result is not None

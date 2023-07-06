from metriq import MetriqClient

submission_id = "1234567890"
method_id = "2345678901"
client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.submission_add_method(submission_id=submission_id, method_id=method_id)
assert result is not None

from metriq import MetriqClient

submission_id = "1234567890"
tag_name = "quantum-computing"
client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.submission_add_tag(submission_id=submission_id, tag_name=tag_name)
assert result is not None
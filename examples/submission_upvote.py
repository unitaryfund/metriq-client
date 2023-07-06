from metriq import MetriqClient

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
# Give a submission ID, as the string below.
result = client.submission_upvote("6116cc3b8d4c8079d6b4f618")
assert result is not None


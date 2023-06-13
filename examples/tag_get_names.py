from metriq import MetriqClient

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.tag_names_get()
assert result is not None


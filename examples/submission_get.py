from metriq import MetriqClient

client = MetriqClient(
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzcsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2NTk3MTA0Mzl9.__seCACSgBAr-6sZ1A1kaS4Y6qyUrbspO0vnFcG-tR8")

print(client.submission_get("1"))

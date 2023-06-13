from metriq import MetriqClient

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTgsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY1NzYzODl9._4CZoykTkKv_OPSWU4jNBgFhJjFH5aVOp0LubuFVA6Y")
result = client.method_get("6101c6ac1134861ba8fbdd9e")
assert result is not None

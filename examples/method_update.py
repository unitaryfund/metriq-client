from metriq import MetriqClient
from metriq.models.method import MethodUpdateRequest


method = MethodUpdateRequest()
method_id = "6101c6ac1134861ba8fbdd9e"
method.name = "Test Method name Updated (Client)"
method.fullName = "Test Method fullName Updated (Client)"
method.description = "Test Method description Updated (Client)"

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTgsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY1NzYzODl9._4CZoykTkKv_OPSWU4jNBgFhJjFH5aVOp0LubuFVA6Y")
result = client.method_update(method_id, method)
assert result is not None

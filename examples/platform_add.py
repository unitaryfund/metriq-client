from msilib.schema import Environment
from metriq import MetriqClient
from metriq.models.platform import EnvironmentCreateRequest

environment = EnvironmentCreateRequest()
environment.userId = "60f06be9f320801f0d2380d4"
environment.name = "Test Submission (Client)"
environment.fullName = "Test Submission Full Name (Client)"
environment.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTgsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY1NzYzODl9._4CZoykTkKv_OPSWU4jNBgFhJjFH5aVOp0LubuFVA6Y")
result = client.platform_add(environment)
assert result is not None

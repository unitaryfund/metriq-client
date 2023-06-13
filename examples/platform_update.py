from metriq import MetriqClient
from metriq.models.platform import PlatformUpdateRequest


environment = PlatformUpdateRequest()
platform_id = "6102f848ff8f28281ae4ea3c"
environment.parentPlatform = "6102f848ff8f28281ae4ea3c"
environment.name = "Environment_1"
environment.fullName = "Test environment Updated(Client)"
environment.description = "Test environment Updated Description (Client)."
client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTgsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY1NzYzODl9._4CZoykTkKv_OPSWU4jNBgFhJjFH5aVOp0LubuFVA6Y")
result = client.platform_update(platform_id, environment)
assert result is not None
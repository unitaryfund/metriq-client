"""Add platform to Metriq."""
import os
from metriq_client import MetriqClient
from metriq_client.models.platform import PlatformCreateRequest


platform = PlatformCreateRequest()
platform.userId = "60f06be9f320801f0d2380d4"
platform.name = "Test Submission (Client)"
platform.fullName = "Test Submission Full Name (Client)"
platform.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.platform_add(platform)
assert result is not None

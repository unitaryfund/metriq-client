from metriq import MetriqClient
from metriq.models.platform import PlatformCreateRequest
import os

environment = PlatformCreateRequest()
environment.userId = "60f06be9f320801f0d2380d4"
environment.name = "Test Submission (Client)"
environment.fullName = "Test Submission Full Name (Client)"
environment.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.platform_add(environment)
assert result is not None

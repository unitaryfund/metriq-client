"""Add method to Metriq."""
import os
from metriq_client import MetriqClient
from metriq_client.models.method import MethodCreateRequest


method = MethodCreateRequest()
method.name = "Test Method Name (Client)"
method.fullName = "Test Method Full Name (Client)"
method.description = "This is the first method to be successfully uploaded with the Python client."
client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))

result = client.method_add(method)
assert result is not None

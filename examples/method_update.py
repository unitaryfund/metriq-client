"""Update method on Metriq."""
import os
from metriq_client import MetriqClient
from metriq_client.models.method import MethodUpdateRequest


method = MethodUpdateRequest()
method_id = "6101c6ac1134861ba8fbdd9e"
method.name = "Test Method name Updated (Client)"
method.fullName = "Test Method fullName Updated (Client)"
method.description = "Test Method description Updated (Client)"

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.method_update(method_id, method)
assert result is not None

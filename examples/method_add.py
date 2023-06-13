from metriq import MetriqClient
from metriq.models.method import MethodCreateRequest

method = MethodCreateRequest()
method.name = "Test Method Name (Client)"
method.fullName = "Test Method Full Name (Client)"
method.description = "This is the first method to be successfully uploaded with the Python client."
client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.method_add(method)
assert result is not None

from metriq import MetriqClient
from metriq.models.method import MethodUpdateRequest


method = MethodUpdateRequest()
method_id = "6101c6ac1134861ba8fbdd9e"
method.name = "Test Method name Updated (Client)"
method.fullName = "Test Method fullName Updated (Client)"
method.description = "Test Method description Updated (Client)"

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.method_update(method_id, method))

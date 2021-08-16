from metriq import MetriqClient
from metriq.models.method import MethodCreateRequest

method = MethodCreateRequest()
method.name = "Test Method Name (Client)"
method.fullNme = "Test Method Full Name (Client)"
method.description = "This is the first method to be successfully uploaded with the Python client."
client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.method_add(method))

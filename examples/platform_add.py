from msilib.schema import Environment
from metriq import MetriqClient
from metriq.models.platform import EnvironmentCreateRequest

environment = EnvironmentCreateRequest()
environment.userId = "60f06be9f320801f0d2380d4"
environment.name = "Test Submission (Client)"
environment.fullName = "Test Submission Full Name (Client)"
environment.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.task_add(environment))

from metriq import MetriqClient
from metriq.models.task import TaskCreateRequest

task = TaskCreateRequest()
task.userId = "60f06be9f320801f0d2380d4"
task.name = "Test Submission (Client)"
task.fullName = "Test Submission Full Name (Client)"
task.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.task_add(task))

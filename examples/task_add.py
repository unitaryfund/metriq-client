from metriq import MetriqClient
from metriq.models.task import TaskCreateRequest

task = TaskCreateRequest()
task.userId = "60f06be9f320801f0d2380d4"
task.name = "Test Submission (Client)"
task.fullName = "Test Submission Full Name (Client)"
task.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.task_add(task)
assert result is not None

from metriq import MetriqClient
from metriq.models.task import TaskCreateRequest

task = TaskCreateRequest()
task.userId = "60f06be9f320801f0d2380d4"
task.name = "Test Submission (Client)"
task.fullName = "Test Submission Full Name (Client)"
task.description = "This is the first submission to be successfully uploaded with the Python client."

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.task_add(task)
assert result is not None

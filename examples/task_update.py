from metriq import MetriqClient
from metriq.models.task import TaskUpdateRequest


task = TaskUpdateRequest()
task_id = "6102f848ff8f28281ae4ea3c"
task.name = "MAXCUT 2"
task.fullName = "Test Task Updated(Client)"
task.description = "Test Task Updated Description (Client)."
client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.task_update(task_id, task)
assert result is not None

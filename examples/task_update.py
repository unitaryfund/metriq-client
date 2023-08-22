"""Update task by ID on Metriq."""
import os
from metriq import MetriqClient
from metriq.models.task import TaskUpdateRequest


task = TaskUpdateRequest()
task_id = "6102f848ff8f28281ae4ea3c"
task.name = "MAXCUT 2"
task.fullName = "Test Task Updated(Client)"
task.description = "Test Task Updated Description (Client)."
client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.task_update(task_id, task)
assert result is not None

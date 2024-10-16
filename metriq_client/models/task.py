from tea_client.models import TeaClientModel
from metriq_client.models.page import Page


class Task(TeaClientModel):
    """Task object representing a task in the Metriq system.

    Attributes:
        id (int): Task ID, typically an integer and required.
        userId (str | None): The ID of the user who created the task.
        name (str | None): The name of the task.
        fullName (str | None): The full name of the task, providing a more detailed description.
        description (str | None): A brief description of the task.
        submittedDate (str | None): The date when the task was submitted.
        deletedDate (str | None): The date when the task was deleted, if applicable.
    """

    id: int  # id is required and should never be None
    userId: str | None = None
    name: str | None = None
    fullName: str | None = None
    description: str | None = None
    submittedDate: str | None = None
    deletedDate: str | None = None

class TaskCreateRequest(TeaClientModel):
    """TaskCreateRequest object.

    Attributes:
        userId (str): The ID of the user submitting the task.
        name (str): Task name.
        fullName (str): Full name of task.
        description (str): Task description.
        parent_task (str, optional): ID of the parent task.
    """

    userId: str | None
    name: str | None
    fullName: str | None
    description: str | None = ""
    parent_task: str | None = None


class TaskUpdateRequest(TeaClientModel):
    """TaskUpdateRequest object.

    Attributes:
        userId (str): The ID of the user submitting the task.
        name (str): Task name.
        fullName (str): Full name of task.
        description (str): Task description.
        parent_task (str, optional): ID of the parent task.
    """

    name: str | None
    fullName: str | None
    description: str | None = ""
    parent_task: str | None = None


class Tasks(Page):
    """Object representing a paginated page of tasks.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Task]): List of tasks on this page.
    """

    results: list[Task]

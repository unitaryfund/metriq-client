from typing import List, Optional

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class Task(TeaClientModel):
    """Task object.

    Attributes:
        id (str): Task ID.
        name (str): Task name.
        fullName (str): Full name of Task.
        description (str): Task description.
        submittedDate (str): Date of Task submission.
        deletedDate (str): Date of Task deletion.
    """

    class Config:
        fields = {'id': '_id'}

    id: str
    userId: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str]
    submittedDate: Optional[str]
    deletedDate: Optional[str]


class TaskCreateRequest(TeaClientModel):
    """TaskCreateRequest object.


    Attributes:
        userId (str): The ID of the user submitting the task.
        name (str): Task name.
        fullName (str): Full name of task.
        description (str): Task description.
        parent_task (str, optional): ID of the parent task.
    """

    userId: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""
    parent_task: Optional[str] = None


class TaskUpdateRequest(TeaClientModel):
    """TaskUpdateRequest object.

    Attributes:
        userId (str): The ID of the user submitting the task.
        name (str): Task name.
        fullName (str): Full name of task.
        description (str): Task description.
        parent_task (str, optional): ID of the parent task.
    """

    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""
    parent_task: Optional[str] = None

class Tasks(Page):
    """Object representing a paginated page of tasks.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Task]): List of tasks on this page.
    """

    results: List[Task]

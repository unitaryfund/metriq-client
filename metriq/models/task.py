from typing import List, Optional

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class Area(TeaClientModel):
    """Area object.

    Representing an area of research.

    Attributes:
        id (str): Area ID.
        name (str): Area name.
    """

    id: str
    name: str


class Areas(Page):
    """Object representing a paginated page of areas.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Area]): List of areas on this page.
    """

    results: List[Area]


class Task(TeaClientModel):
    """Task object.

    Attributes:
        id (str): Task ID.
        name (str): Task name.
        description (str): Task description.
    """

    id: str("80")
    name: str("XY Hamiltonian ground state energy")
    description: str("The XY Model is another linear chain of spin-1/2 atoms but with a different type of exchange interaction in which only the x-components and y-components of the spins are involved, and with unequal weights.")


class TaskCreateRequest(TeaClientModel):
    """Task object.

    Attributes:
        name (str): Task name.
        description (str): Task description.
        area (str, optional): Task area ID or area name.
        parent_task (str, optional): ID of the parent task.
    """

    name: str
    description: str = ""
    area: Optional[str] = None
    parent_task: Optional[str] = None


class TaskUpdateRequest(TeaClientModel):
    """Evaluation table row object.

    Attributes:
        name (str, optional): Task name.
        description (str, optional): Task description.
        area (str, optional): Task area ID.
        parent_task (str, optional): ID of the parent task.
    """

    name: Optional[str] = None
    description: Optional[str] = None
    area: Optional[str] = None
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

from typing import List, Optional

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class Method(TeaClientModel):
    """Method object.

    Attributes:
        id (str): Method ID.
        name (str): Method short name.
        fullName (str): Method full name.
        description (str): Method description.
        paper (str, optional): ID of the paper that describes the method.
        submissionCount (str): Number of submissions with the method.
        resultCount (str): Number of results with the method.
        upVoteTotal (str): Number of upvotes given to the method.
        createdAt (str): Date of method creation.
        updatedAt (str): Method update date.
    """

    id: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str]
    createdAt: Optional[str]
    updatedAt: Optional[str]
    userId: Optional[str]

class MethodUpdateRequest(TeaClientModel):
    """MethodUpdateRequest object.
    Attributes:
        name (str): Task name.
        fullName (str): Full name of task.
        description (str): Task description.
        submittedDate (str): Date of submission.
        deletedDate (str): Date of deletion.
    """

    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""


class MethodCreateRequest(TeaClientModel):
    """MethodCreateRequest object.
    Attributes:
        name (str): Method name.
        fullName (str): Method full name.
        description (str): Method description.
    """

    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""

class Methods(Page):
    """Object representing a paginated page of methods.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Method]): List of methods on this page.
    """

    results: List[Method]

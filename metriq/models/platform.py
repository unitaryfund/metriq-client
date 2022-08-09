from typing import List, Optional

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class Environment(TeaClientModel):
    """Environment object.

    Attributes:
        id (str): Environment ID.
        name (str): Environment name.
        fullName (str): Full name of Environment.
        description (str): Environment description.
        submittedDate (str): Date of Environment submission.
        deletedDate (str): Date of Environment deletion.
    """

    class Config:
        fields = {'id': '_id'}

    id: Optional[str]
    userId: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str]
    submittedDate: Optional[str]
    deletedDate: Optional[str]


class EnvironmentCreateRequest(TeaClientModel):
    """EnvironmentCreateRequest object.


    Attributes:
        userId (str): The ID of the user submitting the Environment.
        name (str): Environment name.
        fullName (str): Full name of Environment.
        description (str): Environment description.
        parentEnvironment (str, optional): ID of the parent Environment.
    """

    userId: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""
    parentEnvironment: Optional[str] = None


class EnvironmentUpdateRequest(TeaClientModel):
    """EnvironmentUpdateRequest object.

    Attributes:
        userId (str): The ID of the user submitting the Environment.
        name (str): Environment name.
        fullName (str): Full name of Environment.
        description (str): Environment description.
        parentEnvironment (str, optional): ID of the parent Environment.
    """

    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""
    parentEnvironment: Optional[str] = None


class Environment(Page):
    """Object representing a paginated page of Environment.

    Attributes:
        count (int): Number of elements matching the query.
        nextPage (int, optional): Number of the next page.
        previousPage (int, optional): Number of the previous page.
        results (List[Environment]): List of Environment on this page.
    """

    results: List[Environment]

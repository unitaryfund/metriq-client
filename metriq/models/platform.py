from typing import List, Optional

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class Platform(TeaClientModel):
    """Platform object.

    Attributes:
        id (str): Platform ID.
        name (str): Platform name.
        fullName (str): Full name of Platform.
        description (str): Platform description.
        submittedDate (str): Date of Platform submission.
        deletedDate (str): Date of Platform deletion.
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


class PlatformCreateRequest(TeaClientModel):
    """PlatformCreateRequest object.


    Attributes:
        userId (str): The ID of the user submitting the Platform.
        name (str): Platform name.
        fullName (str): Full name of Platform.
        description (str): Platform description.
        parentPlatform (str, optional): ID of the parent Platform.
    """

    userId: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""
    parentPlatform: Optional[str] = None


class PlatformUpdateRequest(TeaClientModel):
    """PlatformUpdateRequest object.

    Attributes:
        userId (str): The ID of the user submitting the Platform.
        name (str): Platform name.
        fullName (str): Full name of Platform.
        description (str): Platform description.
        parentPlatform (str, optional): ID of the parent Platform.
    """

    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str] = ""
    parentPlatform: Optional[str] = None


class Platform(Page):
    """Object representing a paginated page of Platform.

    Attributes:
        count (int): Number of elements matching the query.
        nextPage (int, optional): Number of the next page.
        previousPage (int, optional): Number of the previous page.
        results (List[Platform]): List of Platform on this page.
    """

    results: List[Platform]

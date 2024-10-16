from tea_client.models import TeaClientModel
from metriq_client.models.page import Page

class Platform(TeaClientModel):
    """Platform object representing a platform in the Metriq system.

    Attributes:
        id (str): Platform ID.
        userId (str | None): The ID of the user who submitted the platform.
        name (str | None): Platform name.
        fullName (str | None): Full name of the platform.
        description (str | None): Description of the platform.
        submittedDate (str | None): Date when the platform was submitted.
        deletedDate (str | None): Date when the platform was deleted, if applicable.
    """

    id: int  # Required ID
    userId: str | None = None
    name: str | None = None
    fullName: str | None = None
    description: str | None = None
    submittedDate: str | None = None
    deletedDate: str | None = None


class PlatformCreateRequest(TeaClientModel):
    """PlatformCreateRequest object representing a request to create a platform.

    Attributes:
        userId (str | None): The ID of the user submitting the platform.
        name (str | None): Platform name.
        fullName (str | None): Full name of the platform.
        description (str | None): Description of the platform.
        parentPlatform (str | None): ID of the parent platform, if applicable.
    """

    userId: str | None = None
    name: str | None = None
    fullName: str | None = None
    description: str | None = ""
    parentPlatform: str | None = None


class PlatformUpdateRequest(TeaClientModel):
    """PlatformUpdateRequest object representing a request to update a platform.

    Attributes:
        name (str | None): Platform name.
        fullName (str | None): Full name of the platform.
        description (str | None): Description of the platform.
        parentPlatform (str | None): ID of the parent platform, if applicable.
    """

    name: str | None = None
    fullName: str | None = None
    description: str | None = ""
    parentPlatform: str | None = None


class Platforms(Page):
    """Object representing a paginated page of platforms.

    Attributes:
        count (int): Number of elements matching the query.
        nextPage (int | None): Number of the next page, if any.
        previousPage (int | None): Number of the previous page, if any.
        results (list[Platform]): List of platforms on this page.
    """

    results: list[Platform]

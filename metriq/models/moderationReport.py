from typing import List, Optional

from tea_client.models import TeaClientModel

from metriq.models.page import Page


class ModerationReport(TeaClientModel):
    """ModerationReport object.

    Attributes:
        id (str): ModerationReport ID.
        name (str): ModerationReport name.
        fullName (str): Full name of ModerationReport.
        description (str): Task description.
        resolvedAt (str): when ModerationReport was resolved
    """

    class Config:
        fields = {'id': '_id'}

    id: str
    userId: Optional[str]
    name: Optional[str]
    fullName: Optional[str]
    description: Optional[str]
    resolvedAt: Optional[str]



class ModerationReports(Page):
    """Object representing a paginated page of ModerationReport.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[ModerationReport]): List of ModerationReports on this page.
    """

    results: List[ModerationReport]

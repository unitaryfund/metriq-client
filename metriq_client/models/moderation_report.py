from tea_client.models import TeaClientModel
from metriq_client.models.page import Page

class ModerationReport(TeaClientModel):
    """ModerationReport object representing a moderation report.

    Attributes:
        id (str): ModerationReport ID.
        userId (str | None): The ID of the user who submitted the moderation report.
        name (str | None): Name of the moderation report.
        fullName (str | None): Full name of the moderation report.
        description (str | None): Description of the moderation report.
        resolvedAt (str | None): Timestamp indicating when the moderation report was resolved.
    """

    id: int  # Required ID
    userId: str | None = None
    name: str | None = None
    fullName: str | None = None
    description: str | None = None
    resolvedAt: str | None = None

class ModerationReportCreateRequest(TeaClientModel):
    """ModerationReportCreateRequest object representing a request to create a moderation report.

    Attributes:
        userId (str | None): The ID of the user submitting the moderation report.
        name (str | None): Name of the moderation report.
        fullName (str | None): Full name of the moderation report.
        description (str | None): Description of the moderation report.
    """

    userId: str | None = None
    name: str | None = None
    fullName: str | None = None
    description: str | None = ""  # Default empty string for description

class ModerationReports(Page):
    """Object representing a paginated page of moderation reports.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int | None): Number of the next page, if any.
        previous_page (int | None): Number of the previous page, if any.
        results (list[ModerationReport]): List of moderation reports on this page.
    """

    results: list[ModerationReport]

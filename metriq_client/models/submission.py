from tea_client.models import TeaClientModel
from metriq_client.models.page import Page

class Submission(TeaClientModel):
    """Submission object representing a submission in the Metriq system.

    Attributes:
        id (int | None): Submission ID for the database.
        userId (str | None): ID of the user responsible for the submission.
        name (str | None): Name of the submission.
        nameNormal (str | None): Normalized name of the submission.
        description (str | None): Description of the submission.
        contentUrl (str | None): URL for the submission content.
        thumbnailUrl (str | None): URL for the submission's image thumbnail.
        codeUrl (str | None): URL for the submission's code.
        supplementalUrl (str | None): URL for supplemental content for the submission.
        approvedAt (str | None): Date of submission approval.
        publishedAt (str | None): Date of submission publication.
        tags (list | None): List of tags associated with the submission.
        tasks (list | None): List of tasks associated with the submission.
        results (list | None): List of results associated with the submission.
        methods (list | None): List of methods associated with the submission.
    """

    id: int | None = None
    userId: int | None = None
    name: str | None = None
    nameNormal: str | None = None
    description: str | None = None
    contentUrl: str | None = None
    thumbnailUrl: str | None = None
    codeUrl: str | None = None
    supplementalUrl: str | None = None
    approvedAt: str | None = None
    publishedAt: str | None = None
    tags: list | None = None
    tasks: list | None = None
    results: list | None = None
    methods: list | None = None


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object representing a request to create a submission.

    Attributes:
        name (str | None): Name of the submission.
        contentUrl (str | None): URL for the submission content.
        thumbnailUrl (str | None): URL for the submission's image thumbnail.
        codeUrl (str | None): URL for the submission's code.
        description (str | None): Description of the submission.
    """

    name: str | None = None
    contentUrl: str | None = None
    thumbnailUrl: str | None = None
    codeUrl: str | None = None
    description: str | None = ""


class SubmissionUpdateRequest(TeaClientModel):
    """SubmissionUpdateRequest object representing a request to update a submission.

    Attributes:
        name (str | None): Name of the submission.
        codeUrl (str | None): URL for the submission's code.
        description (str | None): Description of the submission.
    """

    name: str | None = None
    codeUrl: str | None = None
    description: str | None = None


class Submissions(Page):
    """Object representing a paginated page of submissions.

    Attributes:
        results (list[Submission]): List of submissions on this page.
    """

    results: list[Submission]

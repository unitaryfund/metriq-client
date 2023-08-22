from tea_client.models import TeaClientModel
from typing import Any, Optional, List
from metriq.models.page import Page


class Submission(TeaClientModel):
    """Submission object.

    Attributes:
        id (str): Submission ID for database.
        userId (str): ID of user responsible for upload.
        name (str): Submission name.
        nameNormal (str): Submission name (normalized).
        description (str): Description of submission.
        contentUrl (str): URL for submission.
        thumbnailUrl (str): URL for submission image thumbnail.
        supplementalURL (str): URL for supplemental content for submission.
        approvedDate (str): Date of approval of submission.
        publishedAt (str): Date of publication of submission.
        tags (list): List of tags of submission.
        tasks (list): List of tasks of submission.
        results (list): List of results of submission.
        methods (list): List of methods of submission.
    """

    class Config:
        fields = {'id': '_id'}

    id: Optional[str]
    userId: Optional[str]
    name: Optional[str]
    nameNormal: Optional[str]
    description: Optional[str]
    contentUrl: Optional[str]
    thumbnailUrl: Optional[str]
    codeUrl: Optional[str]
    supplementalUrl: Optional[str]
    approvedAt: Optional[str]
    publishedAt: Optional[str] 
    tags: Optional[List[Any]]
    tasks: Optional[List[Any]]
    results: Optional[List[Any]]
    methods: Optional[List[Any]]


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object.

    Attributes:
        submissionName (str): Submission name.
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        description (str): Description of submission.
    """

    name: Optional[str]
    contentUrl: Optional[str]
    thumbnailUrl: Optional[str]
    description: Optional[str] = ""


class SubmissionUpdateRequest(TeaClientModel):
    """SubmissionUpdateRequest object.

    Attributes:
        submissionName (str): Submission name.
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        description (str): Description of submission.
    """

    name: Optional[str]
    description: Optional[str]

class Submissions(Page):
    """Object representing a paginated page of submissions.

    Attributes:
        count (int): Number of elements matching the query.
        next_page (int, optional): Number of the next page.
        previous_page (int, optional): Number of the previous page.
        results (List[Task]): List of tasks on this page.
    """

    results: List[Submission]
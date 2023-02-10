from tea_client.models import TeaClientModel
from typing import Optional, List


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
    tags: Optional[List]
    tasks: Optional[List]
    results: Optional[List]
    methods: Optional[List]


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
    description: Optional[str]


class SubmissionUpdateRequest(TeaClientModel):
    """SubmissionUpdateRequest object.

    Attributes:
        submissionName (str): Submission name.
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        description (str): Description of submission.
    """

    name: Optional[str]
    description: Optional[str]

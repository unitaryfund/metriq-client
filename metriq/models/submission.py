from tea_client.models import TeaClientModel
from typing import Optional, List


class Submission(TeaClientModel):
    """Submission object.

    Attributes:
        id (str): Submission ID for database.
        userId (str): ID of user responsible for upload.
        submissionName (str): Submission name.
        submissionNameNormal (str): Submission name (normalized).
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        submittedDate (str): Date of submission.
        upvotes (list): List of userIds of upvoters.
        tags (list): List of tags.
        deletedDate (str): Date of submission.
    """

    class Config:
        fields = {'id': '_id'}

    id: str
    userId: Optional[str]
    submissionName: Optional[str]
    submissionNameNormal: Optional[str]
    submissionThumbnailUrl: Optional[str]
    submittedDate: Optional[str]
    description: Optional[str]
    upvotes: List[str]


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object.

    Attributes:
        submissionName (str): Submission name.
    """

    submissionName: Optional[str]
    submissionThumbnailUrl: Optional[str]
    description: Optional[str]

from tea_client.models import TeaClientModel
from typing import Optional, List


class Submission(TeaClientModel):
    """Submission object.

    Attributes:
        id (str): Submission ID for database.
        userId (str): ID of user responsible for upload.
        submissionName (str): Submission name.
        submissionNameNormal (str): Submission name (normalized).
        description (str): Description of submission.
        submittedDate (str): Date of submission.
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        approvedDate (str): Date of approval of submission.
        deletedDate (str): Date of submission.
        upvotes (list): List of userIds of upvoters.
    """

    class Config:
        fields = {'id': '_id'}

    id:Optional[str]
    userId: Optional[str]
    submissionName: Optional[str]
    submissionNameNormal: Optional[str]
    description: Optional[str]
    submittedDate: Optional[str]
    submissionContentUrl: Optional[str]
    submissionThumbnailUrl: Optional[str]
    approvedDate: Optional[str]
    deletedDate: Optional[str]
    upvotes:Optional[str]


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object.

    Attributes:
        submissionName (str): Submission name.
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        description (str): Description of submission.
    """

    submissionName: Optional[str]
    submissionContentUrl: Optional[str]
    submissionThumbnailUrl: Optional[str]
    description: Optional[str]


class SubmissionUpdateRequest(TeaClientModel):
    """SubmissionUpdateRequest object.

    Attributes:
        submissionName (str): Submission name.
        submissionThumbnailUrl (str): URL for submission image thumbnail.
        description (str): Description of submission.
    """

    submissionName: Optional[str]
    description: Optional[str]

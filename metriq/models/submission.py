from tea_client.models import TeaClientModel
from typing import Optional, List


class Submission(TeaClientModel):
    """Submission object.

    Attributes:
        id (str): Submission ID for database.
        userId (str): ID of user responsible for upload.
        submissionName (str): Submission name.
        submissionNameNormal (str): Submission name (normalized).
        upvotes (list): List of userIds of upvoters.
        deletedDate (str): Date of submission.
    """

    class Config:
        fields = {'id': '_id'}

    id: str
    userId: Optional[str]
    submissionName: Optional[str]
    submissionNameNormal: Optional[str]
    submittedDate: Optional[str]
    upvotes: List[str]
    deletedDate: Optional[str]


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object.

    Attributes:
        userId (str): Submission ID.
        submissionName (str): Submission name.
    """

    userId: Optional[str]
    submissionName: Optional[str]

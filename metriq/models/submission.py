from tea_client.models import TeaClientModel
from typing import Optional, List


class Submission(TeaClientModel):
    """Submission object.

    Attributes:
        userId (str): Submission ID.
        submissionName (str): Submission name.
        submissionNameNormal (str): Submission name (normalized).
        upvotes (list): List of userIds of upvoters.
    """

    userId: Optional[str]
    submissionName: Optional[str]
    submissionNameNormal: Optional[str]
    upvotes: List[str]


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object.

    Attributes:
        userId (str): Submission ID.
        submissionName (str): Submission name.
    """

    userId: Optional[str]
    submissionName: Optional[str]

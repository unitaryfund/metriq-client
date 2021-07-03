from tea_client.models import TeaClientModel
from typing import Optional, List


class Submission(TeaClientModel):
    """Submission object.

    Attributes:
        userId (str): Submission ID.
        submissionName (str): Submission name.
    """

    userId: Optional[str]
    submissionName: Optional[str]


class SubmissionCreateRequest(TeaClientModel):
    """SubmissionCreateRequest object.

    Attributes:
        userId (str): Submission ID.
        submissionName (str): Submission name.
    """

    userId: Optional[str]
    submissionName: Optional[str]

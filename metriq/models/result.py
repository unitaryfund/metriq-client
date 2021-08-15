from tea_client.models import TeaClientModel
from typing import Optional, List


class Result(TeaClientModel):
    """Submission object.

    Attributes:
        id (str): Result ID for database.
        userId (str): ID of user responsible for upload.
        submissionId (str): ID of associated submission.
        taskId (str):
        methodId (str):
        isHigherBetter (str):
        metricName (str):
        evaluatedDate (str): Date of evaluation.
        submittedDate (str): Date of submission.
        deletedDate (str): Date of submission.
    """

    class Config:
        fields = {'id': '_id'}

    id: str
    # userId: Optional[str]
    # submissionId: Optional[str]
    # taskId: Optional[str]
    # methodId: Optional[str]
    # isHigherBetter: Optional[str]
    # metricName: Optional[str]
    # metricValue: Optional[str]
    # evaluatedDate: Optional[str]
    # submittedDate: Optional[str]
    # deletedDate: Optional[str]


class ResultCreateRequest(TeaClientModel):
    """ResultCreateRequest object.

    Attributes:
        submissionName (str): Submission name.
    """

    submissionName: Optional[str]
    submissionThumbnailUrl: Optional[str]
    description: Optional[str]

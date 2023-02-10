from tea_client.models import TeaClientModel
from typing import Optional, List


class Result(TeaClientModel):
    """Result object.

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

    userId: Optional[str]
    task: Optional[str]
    method: Optional[str]
    metricName: Optional[str]
    metricValue: Optional[str]
    evaluatedAt: Optional[str]
    notes: Optional[str]
    standardError: Optional[str]
    sampleSize: Optional[str]
    submittedDate: Optional[str]
    deletedDate: Optional[str]


class ResultCreateRequest(TeaClientModel):
    """ResultCreateRequest object.

    Attributes:
        X
    """
    task: Optional[str]
    method: Optional[str]
    platform: Optional[str]
    isHigherBetter: Optional[str]
    metricName: Optional[str]
    metricValue: Optional[str]
    evaluatedAt: Optional[str]
    qubitCount: Optional[str]
    circuitDepth: Optional[str]
    notes: Optional[str]

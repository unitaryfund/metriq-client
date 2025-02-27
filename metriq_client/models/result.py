from tea_client.models import TeaClientModel
from metriq_client.models.page import Page

class Result(TeaClientModel):
    """Result object representing an evaluation result in the Metriq system.

    Attributes:
        id (int): Result ID for the database.
        userId (str | None): ID of the user responsible for the upload.
        task (str | None): ID of the associated task.
        method (str | None): ID of the associated method.
        metricName (str | None): Name of the metric used in the evaluation.
        metricValue (str | None): Value of the metric.
        evaluatedAt (str | None): Date when the evaluation was conducted.
        notes (str | None): Additional notes for the result.
        sampleSize (str | None): Sample size of the result.
        standardError (str | None): Standard error for the result.
        submittedDate (str | None): Date when the result was submitted.
        deletedDate (str | None): Date when the result was deleted, if applicable.
    """

    id: int  # Required ID
    userId: str | None = None
    task: str | None = None
    method: str | None = None
    metricName: str | None = None
    metricValue: str | None = None
    evaluatedAt: str | None = None
    notes: str | None = None
    sampleSize: str | None = None
    standardError: str | None = None
    shots: str | None = None
    submittedDate: str | None = None
    deletedDate: str | None = None

class ResultCreateRequest(TeaClientModel):
    """ResultCreateRequest object representing a request to create a result.

    Attributes:
        task (str | None): ID of the associated task.
        method (str | None): ID of the associated method.
        platform (str | None): ID of the associated platform.
        isHigherBetter (str | None): Indicator if a higher metric value is better.
        metricName (str | None): Name of the metric used in the evaluation.
        metricValue (str | None): Value of the metric.
        evaluatedAt (str | None): Date when the evaluation was conducted.
        qubitCount (str | None): Number of qubits used in the evaluation.
        circuitDepth (str | None): Depth of the quantum circuit used.
        notes (str | None): Additional notes for the result.
        sampleSize (str | None): Sample size of the result.
        standardError (str | None): Standard error for the result.
    """

    task: str | None = None
    method: str | None = None
    platform: str | None = None
    isHigherBetter: str | None = None
    metricName: str | None = None
    metricValue: str | None = None
    evaluatedAt: str | None = None
    qubitCount: str | None = None
    circuitDepth: str | None = None
    notes: str | None = None
    sampleSize: str | None = None
    standardError: str | None = None
    shots: str | None = None


class Results(Page):
    """Object representing a paginated page of results.

    Attributes:
        results (list[Result]): List of result objects on this page.
    """

    results: list[Result]

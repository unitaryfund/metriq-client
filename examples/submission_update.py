"""Update submission on Metriq."""
import os
from metriq import MetriqClient
from metriq.models.submission import SubmissionUpdateRequest


submission = SubmissionUpdateRequest()
submission_id = "60f9d9dbded46f23670f724f"
submission.submissionName = "Test Submission Name Updated (Client)"
submission.description = "Test Submission Updated Description (Client)."

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.submission_update(submission_id, submission)
assert result is not None

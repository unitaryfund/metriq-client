from metriq import MetriqClient
from metriq.models.submission import SubmissionUpdateRequest


submission = SubmissionUpdateRequest()
submission_id = "60f9d9dbded46f23670f724f"
submission.submissionName = "Test Submission Name Updated (Client)"
submission.description = "Test Submission Updated Description (Client)."

client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTksInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY2NjQxODd9.VWT8b4peYwebm9-Ul4-6xkMMajATIiqUXO_dE4lxigk")
result = client.submission_update(submission_id, submission)
assert result is not None

from metriq import MetriqClient
from metriq.models.submission import SubmissionUpdateRequest


submission = SubmissionUpdateRequest()
submission_id = "60f9d9dbded46f23670f724f"
submission.submissionName = "Test Submission Name Updated (Client)"
submission.submissionThumbnailUrl = "Test Submission Updated submissionThumbnailURL"
submission.description = "Test Submission Updated Description (Client)."

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.submission_update(submission_id, submission))

from metriq import MetriqClient
from metriq.models.submission import SubmissionCreateRequest

submission = SubmissionCreateRequest()
submission.submissionName = "Test Submission (Client)"
submission.submissionContentUrl = "https://arxiv.org"
submission.description = "This is the first submission to be successfully uploaded with the Python client."
client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.submission_add(submission))


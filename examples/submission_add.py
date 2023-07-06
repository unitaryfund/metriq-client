from metriq import MetriqClient
from metriq.models.submission import SubmissionCreateRequest

submission = SubmissionCreateRequest()
submission.name = "Test Submission (Client)"
submission.contentUrl = "https://arxiv.org"
submission.description = "This is the first submission to be successfully uploaded with the Python client."
client = MetriqClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTgsInJvbGUiOiJjbGllbnQiLCJpYXQiOjE2ODY1NzYzODl9._4CZoykTkKv_OPSWU4jNBgFhJjFH5aVOp0LubuFVA6Y")
result = client.submission_add(submission)
assert result is not None

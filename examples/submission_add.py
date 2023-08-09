from metriq import MetriqClient
from metriq.models.submission import SubmissionCreateRequest

submission = SubmissionCreateRequest()
submission.name = "Test Submission (Client)"
submission.contentUrl = "https://arxiv.org"
submission.description = "This is the first submission to be successfully uploaded with the Python client."
client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.submission_add(submission)
assert result is not None

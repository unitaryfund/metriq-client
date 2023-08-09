from metriq import MetriqClient

submission_id = "1234567890"
task_id = "2345678901"
client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.submission_add_task(submission_id=submission_id, task_id=task_id)
assert result is not None

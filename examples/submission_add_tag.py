from metriq import MetriqClient

submission_id = "1234567890"
tag_name = "quantum-computing"
client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.submission_add_tag(submission_id=submission_id, tag_name=tag_name)
assert result is not None

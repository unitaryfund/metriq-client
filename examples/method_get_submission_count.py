from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.method_get_submission_count()
assert result is not None

from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.submission_get_by_popular()
assert result is not None

from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.task_get_names()
assert result is not None

from metriq import MetriqClient

client = MetriqClient(token=os.environ(["METRIQ_CLIENT_API_KEY"])
result = client.task_get_network()
assert result is not None

from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.metriq_hello()
assert result is not None

from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
result = client.platform_get("6101c6ac1134861ba8fbdd9e")
assert result is not None

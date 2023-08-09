from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
# Give a submission ID, as the string below.
result = client.submission_delete("6116cc3b8d4c8079d6b4f618")
assert result.response.ok

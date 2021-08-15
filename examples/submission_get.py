from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.submission_get("60f5ce7bc3519e62a97feb54"))

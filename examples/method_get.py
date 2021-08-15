from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.method_get("6101c6ac1134861ba8fbdd9e"))

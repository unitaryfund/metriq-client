from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.task_get("6102f848ff8f28281ae4ea4f"))

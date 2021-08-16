from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
# Give a task ID, as the string below.
print(client.task_delete("6102f848ff8f28281ae4ea4f"))


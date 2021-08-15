from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.method_submission_count_get())

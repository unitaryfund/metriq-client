from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
# Give a submission ID, as the string below.
print(client.submission_delete("6116cc3b8d4c8079d6b4f618"))


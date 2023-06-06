from metriq import MetriqClient

submission_id = "1234567890"
method_id = "2345678901"
client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.submission_add_method(submission_id=submission_id, method_id=method_id))

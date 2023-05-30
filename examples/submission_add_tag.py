from metriq import MetriqClient

submission_id = "1234567890"
tag_name = "quantum-computing"
client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.submission_add_tag(submission_id=submission_id, tag_name=tag_name))

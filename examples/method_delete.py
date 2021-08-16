from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
# Give a method ID, as the string below.
print(client.method_delete("6101c6ac1134861ba8fbdd9e"))


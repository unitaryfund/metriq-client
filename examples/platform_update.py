from metriq import MetriqClient
from metriq.models.platform import EnvironmentUpdateRequest


environment = EnvironmentUpdateRequest()
environment_id = "6102f848ff8f28281ae4ea3c"
environment.name = "Environment_1"
environment.fullName = "Test environment Updated(Client)"
environment.description = "Test environment Updated Description (Client)."
client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.platform_update(environment_id, environment))

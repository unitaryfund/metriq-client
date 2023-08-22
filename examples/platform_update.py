"""Update platform on Metriq."""
import os
from metriq import MetriqClient
from metriq.models.platform import PlatformUpdateRequest


platform = PlatformUpdateRequest()
platform_id = 5
platform.parentPlatform = "6102f848ff8f28281ae4ea3c"
platform.name = "Environment_1"
platform.fullName = "Test environment Updated(Client)"
platform.description = "Test environment Updated Description (Client)."

client = MetriqClient(token=str(os.environ["METRIQ_CLIENT_API_KEY"]))
result = client.platform_update(platform_id, platform)
assert result is not None

# Quickstart

The `metriq-client` is designed to work with python objects. To use the library you only need to import 
and instantiate the client and start calling methods on it:

```python
from metriq_client import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.hello())
>>> {'status': 'API is working', 'message': 'This is the Metriq public REST API.'}
```

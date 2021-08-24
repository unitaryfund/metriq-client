# metriq API client

This is a client for [Metriq](https://metriq.com/api/v1/docs/)
read/write API.

The API is completely covered by the client and it wraps all the API models
into python objects and communicates with the API by getting and passing those
objects from and to the api client.

Documentation can be found on the
[ReadTheDocs](https://metriq-client.readthedocs.io/en/latest/) website.

It is published to the
[Python Package Index](https://pypi.org/project/metriq-client/) and
can be installed by simply calling `pip install metriq-client`.

## Quick usage example

You will require the [`pipenv` package](https://pipenv.pypa.io/en/latest/) on your machine in order to instantiate a 
virtual environment. This can be done with `pip install --user pipenv`.

You will then need to install and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

Once the virtual environment has been activated, to check that the `metriq-client` API is working as expected, run the 
following example script from `metriq-client/examples/metriq_hello.py`:

```python
from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.hello())
>>> {'status': 'API is working', 'message': 'This is the Metriq public REST API.'}
```

For further examples of usage, consult `metriq-client/examples`. For full docs please see our 
[ReadTheDocs](https://metriq-client.readthedocs.io/en/latest/) page.

# Metriq API client

This is a client for [Metriq](https://metriq.info) read/write API.

It is adapted from the [PapersWithCode client](https://github.com/paperswithcode/paperswithcode-client), with thanks!

The API is completely covered by the client and it wraps all the API models
into python objects and communicates with the API by getting and passing those
objects from and to the api client.

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

#in your CLI, run the command: export METRIQ_CLIENT_API_KEY=<the key you get from the website>
#On a UNIX or LINUX system, you can put this inside a .bashrc or .env. For windows, put it into your enviornment variables
client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
print(client.hello())
>>> {'status': 'API is working', 'message': 'This is the Metriq public REST API.'}
```

For further examples of usage, consult `metriq-client/examples`.

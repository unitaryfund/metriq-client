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

You will need to create an environment variable `METRIQ_CLIENT_API_KEY` to store the Metriq API key. On Linux/Unix operating systems, you can run
```
export METRIQ_CLIENT_API_KEY=<the key you get from the website>
```
in your terminal. On Windows, you can similarly add this variable as an environment variable. Once you have created the environment variable, you can verify that the client works as follows:

```python
from metriq import MetriqClient

client = MetriqClient(token=os.environ["METRIQ_CLIENT_API_KEY"])
print(client.hello())
>>> {'status': 'API is working', 'message': 'This is the Metriq public REST API.'}
```

For further examples of usage, consult `metriq-client/examples`.

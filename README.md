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

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.hello())
>>> {'status': 'API is working', 'message': 'This is the Metriq public REST API.'}
```

## Further usage (DRAFT)
### Submissions
Many details of submissions can be managed using the client. For example, the following functionalities can be invoked:
- Adding a submission or any part of one (method, tag, task, etc.)
- Deleting a submission
- Sorting submissions (by latest, popular, or trending_
- Upvoting a submission

### Tags
Similarly, with the client, it is possible to (((what are these funcions doing)))
- tag_get.py
- tag_get_names.py

### Tasks
Users can also add or update tasks that exist within Metriq, or (((get functions)))
- task_add.py
- task_get.py
- task_get_names.py
- task_get_submission_count.py
- task_update.py
  
### Platform
- platform_add.py
- platform_get.py
- platform_update.py

For even more examples of usage, consult `metriq-client/examples`.

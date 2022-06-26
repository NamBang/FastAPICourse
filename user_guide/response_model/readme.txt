FastAPI will use this response_model to:

- Convert the output data to its type declaration
- validate the data
- Add a JSON Schema for the response, in the OpenAPI path operation
- will be used by the automatic documentation system

Most importantly: will limit the output data to that of the model.

Note: never store the plain password of a user or sent it in a response
- FastAPI wil take care of filtering out all the data that is not declared in the output model

Recap:
- use the path operation decorator's parameter response_model to
define response models and especially to ensure private data is filtered out.

- Use response_model_exclude_unset to return only the values explicity set.
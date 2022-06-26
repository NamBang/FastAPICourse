------------------request body---------------------------------
Request body is data sent by the client to your API.
A response body is the data your API sends to the client.

Note:
- API always send respone body, but client don't necessarily need to send requests body.
- Send data should use one of : Post, Put delete, or patch


Result: with just that python type decration(pydantic)
- Read the body of the requests as JSON
- Convert the corresponding types
- Validate the data:
    + if data is invalid, it will return a nice and clear error,
      indicating exactly where and what was the incorrect data.
- Give you the received data in the parameter item: As you declared it in the funciton to be of type item,
you will also have all editor support for all of the atrributes and their types.
- Generate Json schema.

Note:
The function parameters will be recognized as follows:
- if the parameter is also declared in the path, it will be used as a path parameter.
- if the parameter is of a sigular type( like int, float, str, bool, etc) it will be interpereted as a query parameter parameter
- If the parameter is declared to be of the type of a pydantic model. It will be interpreted as a request body.

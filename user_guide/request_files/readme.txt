File is a class that inherit directly from Form.

Use the Uploadfile has several advantages over bytes
- work well for larger files without consuming all the memory
- get metatdata from the uploaded files

Uploadfile has the following async methods:
- write(data): write data to the file
-read(size): read size(int) bytes/characters of the file
- seeK(offset): goes to the byte position offset (int) in the file.
- close(): closes the file
all these methods are async methods, you need to "await" them.
in async methods: ex: contents = await myfile.read()

Note: Whey you use the async methods, FastAPI runs the file methods in a threadpool and awaits for them.
- FastAPI's UploadFile inherits directly from Starlette's UploadFile.

Recap: Use File, bytes, and UploadFile to declare files to be uploaded in the request, sent as form data.
- Use File and Form together when you need to receive data and files in the same request.
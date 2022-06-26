The same way declare additional validation adn metadata in path operation functions parameters with Query, Path and Body.
We can declare validation and metadata inside of Pydantic models using Pydantic's Field


Query, Path and others create objecss of subclasses of a common Parsm class,
which is itself a subclass of Pydantic's FieldInfo class. Pydantic's FieldInfo returns an instance of FiledInfo as well.

Each model's atributes with a type, default value and Field has the same structure as a path operation function's parameter,
with Filed instead of Path, Query and Body.


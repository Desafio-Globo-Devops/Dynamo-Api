from mypy_extensions import TypedDict


class DynamoInterface(TypedDict, total=False):
    id: str

from typing import TypedDict


class SupportState(TypedDict):
    query : str
    intent : str
    response : str

    
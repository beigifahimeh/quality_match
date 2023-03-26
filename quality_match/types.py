from enum import Enum
from typing import Any


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class Answer(Enum):
    EMPTY = ""
    NO = "no"
    YES = "yes"


class TaskOutput:
    answer: Answer
    cant_solve: bool
    corrupt_data: bool
    duration_ms: int

    def __init__(self, answer: Answer, cant_solve: bool, corrupt_data: bool, duration_ms: int) -> None:
        self.answer = answer
        self.cant_solve = cant_solve
        self.corrupt_data = corrupt_data
        self.duration_ms = duration_ms

    @staticmethod
    def from_dict(obj: Any) -> "TaskOutput":
        assert isinstance(obj, dict)
        answer = Answer(obj.get("answer"))
        cant_solve = from_bool(obj.get("cant_solve"))
        corrupt_data = from_bool(obj.get("corrupt_data"))
        duration_ms = from_int(obj.get("duration_ms"))
        return TaskOutput(answer, cant_solve, corrupt_data, duration_ms)


class TaskInput:
    image_url: str

    def __init__(self, image_url: str) -> None:
        self.image_url = image_url

    @staticmethod
    def from_dict(obj: Any) -> "TaskInput":
        assert isinstance(obj, dict)
        image_url = from_str(obj.get("image_url"))
        return TaskInput(image_url)

from typing import Any
from collections.abc import Iterable

class Queue:
    def __init__(self):...
    def enqueue(self, item: Any) -> None:...
    def dequeue(self) -> Any:...
    def extend(self, items: Iterable[Any]) -> None:...
    def __len__(self) -> int:...
    def is_empty(self) -> bool:...

class QueueC:
    def __init__(self):...
    def enqueue(self, item: Any) -> None:...
    def dequeue(self) -> Any:...
    def extend(self, items: Iterable[Any]) -> None:...
    def __len__(self) -> int:...
    def is_empty(self) -> bool:...

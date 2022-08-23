# Create a strongly typed queue data structure.
#
from typing import Any, List, Optional, TypeVar, Generic, Sequence, Iterator
TYPE = TypeVar('TYPE')

class Queue(Generic[TYPE], Sequence[TYPE]):
    def __init__(self) -> None:
        self.items: List[TYPE] = []

    def enqueue(self, item: TYPE) -> None:
        self.items.append(item)

    def dequeue(self) -> TYPE:
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def __len__(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        return f'{self.items}'
    
    def __repr__(self) -> str:
        return f'{self.items}'
    
    def __iter__(self) -> Iterator[TYPE]:
        return iter(self.items)
    
    def __contains__(self, item: TYPE) -> bool:
        return item in self.items
    
    def __getitem__(self, index: int) -> TYPE:
        return self.items[index]
    
    def __setitem__(self, index: int, item: TYPE) -> None:
        self.items[index] = item
    
    def __delitem__(self, index: int) -> None:
        del self.items[index]
    
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        return self.items(*args, **kwargs)
    
    def __next__(self) -> TYPE:
        return self.items.next()
    
    def __iter__(self) -> Iterator[TYPE]:
        return iter(self.items)
    
    def __reversed__(self) -> Iterator[TYPE]:
        return reversed(self.items)

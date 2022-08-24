from typing import Any, Collection, List, Optional, TypeVar, Generic, Sequence, Iterator, Union

TYPE = TypeVar('TYPE')

class Queue(Generic[TYPE], Collection[TYPE]):
    def __init__(self) -> None:
        self.items: List[TYPE] = []

    def enqueue(self, item: TYPE) -> None:
        self.items.append(item)

    def dequeue(self) -> Union[TYPE,None]:
        return  None if self.is_empty() else self.items.pop(0)

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
    
    def __next__(self) -> TYPE:
        return self.items.next()
    
    def __iter__(self) -> Iterator[TYPE]:
        return iter(self.items)
    
    def __reversed__(self) -> Iterator[TYPE]:
        return reversed(self.items)

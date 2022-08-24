from typing import NewType, Tuple
from py_core_ds.ds.Queue import Queue

class TestQueue:
    def test_int_queue(self):
        q = Queue[int]()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        assert q.__contains__(5) == False
        assert q.__contains__(1) == True
        
        assert q.__iter__().__next__() == 1
        assert q.__reversed__().__next__() == 3
        assert q.__repr__() == '[1, 2, 3]'
        assert q.__str__() == '[1, 2, 3]'
        
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3
        assert q.dequeue() == None
        
        assert q.is_empty() == True
        assert q.__len__() == 0
    
    def test_str_queue(self):
        q = Queue[str]()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')

        assert q.__contains__('d') == False
        assert q.__contains__('a') == True
        
        assert q.__iter__().__next__() == 'a'
        assert q.__reversed__().__next__() == 'c'
        assert q.__repr__() == "['a', 'b', 'c']"
        assert q.__str__() == "['a', 'b', 'c']"
        
        assert q.dequeue() == 'a'
        assert q.dequeue() == 'b'
        assert q.dequeue() == 'c'
        assert q.dequeue() == None
        
        assert q.is_empty() == True
        assert q.__len__() == 0
    
    def test_typed_ds_queue(self):
        Coordinate = NewType('Coordinate', Tuple[int, int])
        q = Queue[Coordinate]()
        q.enqueue(Coordinate((1, 2)))
        q.enqueue(Coordinate((3, 4)))
        q.enqueue(Coordinate((5, 6)))

        assert q.__contains__(Coordinate((7, 8))) == False
        assert q.__contains__(Coordinate((1, 2))) == True

        assert q.__iter__().__next__() == Coordinate((1, 2))
        assert q.__reversed__().__next__() == Coordinate((5, 6))
        
        assert q.dequeue() == Coordinate((1, 2))
        assert q.dequeue() == Coordinate((3, 4))
        assert q.dequeue() == Coordinate((5, 6))
        assert q.dequeue() == None
        assert q.is_empty() == True
        assert q.__len__() == 0
    
    def test_alias_ds_queue(self):
        Coordinate = Tuple[int, int]
        q = Queue[Coordinate]()
        q.enqueue((1, 2))
        q.enqueue((3, 4))
        q.enqueue((5, 6))

        assert q.__contains__((7, 8)) == False
        assert q.__contains__((1, 2)) == True

        assert q.__iter__().__next__() == (1, 2)
        assert q.__reversed__().__next__() == (5, 6)
        
        assert q.dequeue() == (1, 2)
        assert q.dequeue() == (3, 4)
        assert q.dequeue() == (5, 6)
        assert q.dequeue() == None
        assert q.is_empty() == True
        assert q.__len__() == 0
        
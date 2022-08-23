
## Create a Testsuite with pytest and test stack class
from typing import NewType, Tuple
from py_core_ds.Stack import Stack
from pytest import raises

class TestStack:
    def test_stack_is_empty(self) -> None:
        stack = Stack[str]()
        assert stack.is_empty() == True
    
    def test_stack_push(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        assert stack.is_empty() == False
        assert stack.peek() == 1
        assert stack.__len__() == 1
    
    def test_stack_pop(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        assert stack.pop() == 1
        assert stack.is_empty() == True
    
    def test_stack_peek(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        assert stack.peek() == 1
        assert stack.is_empty() == False
    
    def test_stack_len(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2
    
    def test_stack_str(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert str(stack) == '[1, 2]'
    
    def test_stack_repr(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert repr(stack) == '[1, 2]'
    
    def test_stack_iter(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert list(stack) == [1, 2]
    
    def test_stack_contains(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert 1 in stack
        assert 3 not in stack
    
    def test_stack_getitem(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert stack[0] == 1
        assert stack[1] == 2
    
    def test_stack_setitem(self) -> None:
        stack = Stack[str]()
        stack.push('a')
        stack.push('2')
        assert stack.__len__() == 2
        assert stack.__repr__() == '[\'a\', \'2\']'
        assert stack.__str__() == '[\'a\', \'2\']'
    
    def test_stack_with_dict(self) -> None:
        stack = Stack[dict]()
        stack.push({'a': 1})
        stack.push({'b': 2})
        assert stack.__len__() == 2
        assert stack.__repr__() == '[{\'a\': 1}, {\'b\': 2}]'
        assert stack.pop() == {'b': 2}
        assert stack.pop() == {'a': 1}
        assert stack.is_empty() == True
    
    def test_stack_with_User_defined_types(self) -> None:
        stack = Stack[Tuple[int, str]]()
        stack.push((1, 'a'))
        stack.push((2, 'b'))
        assert stack.__len__() == 2
        assert stack.__repr__() == '[(1, \'a\'), (2, \'b\')]'
        assert stack.pop() == (2, 'b')
        assert stack.pop() == (1, 'a')
        assert stack.is_empty() == True
    
    def test_stack_with_User_defined_types_with_dict(self) -> None:
        stack = Stack[Tuple[int, dict]]()
        stack.push((1, {'a': 1}))
        stack.push((2, {'b': 2}))
        assert stack.__len__() == 2
        assert stack.__repr__() == '[(1, {\'a\': 1}), (2, {\'b\': 2})]'
        assert stack.pop() == (2, {'b': 2})
        assert stack.pop() == (1, {'a': 1})
        assert stack.is_empty() == True
    
    def test_stack_with_User_defined_types_with_list(self) -> None:
        stack = Stack[Tuple[int, list]]()
        stack.push((1, [1, 2, 3]))
        stack.push((2, [4, 5, 6]))
        assert stack.__len__() == 2
        assert stack.__repr__() == '[(1, [1, 2, 3]), (2, [4, 5, 6])]'
        assert stack.pop() == (2, [4, 5, 6])
        assert stack.pop() == (1, [1, 2, 3])
        assert stack.is_empty() == True
    
    def test_stack_with_Defined_ds_alias(self) -> None:
        Board = Tuple[int, int]
        stack = Stack[Board]()
        stack.push((1, 2))
        stack.push((2, 3))
        assert stack.__len__() == 2
        assert stack.__repr__() == '[(1, 2), (2, 3)]'
        assert stack.pop() == (2, 3)
        assert stack.pop() == (1, 2)
        assert stack.is_empty() == True
    
    def test_stack_with_Defined_ds_type(self) -> None:
        Board = NewType('Board',Tuple[int, int])
        stack = Stack[Board]()
        stack.push(Board((1,2)))
        stack.push(Board((2,3)))
        assert stack.__len__() == 2
        assert stack.__iter__().__next__() == Board((1,2))
        assert stack.pop() == Board((2,3))
        assert stack.pop() == Board((1,2))
        assert stack.is_empty() == True

    
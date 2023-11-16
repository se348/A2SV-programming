# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        self.next_val = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self) -> int:
        return self.next_val

    def next(self) -> int:
        next = self.next_val
        self.next_val = self.iterator.next() if self.iterator.hasNext() else None
        return next

    def hasNext(self) -> bool:
        return self.next_val is not None

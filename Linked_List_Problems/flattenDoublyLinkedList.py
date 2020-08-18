"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from typing import Union
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        def descend(node) -> Union['Node','Node']:
            #base case: reached end of level, return head and tail of this level
            levelHead = node
            if not node.next:
                levelTail = node
                return levelHead, levelTail
            #recursive case: keep going through current level until reach a node with child
            else:
                while node.next:
                    if node.child:
                        #descend into next level and bring back head and tail to current level
                        nextLevelHead, nextLevelTail = descend(node.child)
                        nextLevelHead.prev = node
                        nextLevelTail.next = node.next
                        node.next.prev = nextLevelTail
                        node.next = nextLevelHead
                        node.child = None
                        node = nextLevelTail.next
                    else:
                        node = node.next
                levelTail = node
                return levelHead,levelTail
        if head:    
            levelHead,_ = descend(head)
        return levelHead if head else None

import heapq
from typing import List, Optional
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        heap = []
        counter = 0  

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1
        dummy = ListNode(0)
        current = dummy
        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                counter += 1
                heapq.heappush(heap, (node.next.val, counter, node.next))
        return dummy.next
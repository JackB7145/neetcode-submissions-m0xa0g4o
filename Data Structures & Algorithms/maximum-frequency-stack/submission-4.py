class Node:
    def __init__(self, freq):
        self.freq = freq
        self.vals = set()          # values currently at this frequency
        self.prev = None
        self.next = None


class FreqStack:
    def __init__(self):
        self.stack = []            # global stack of every value pushed (None = popped out)
        self.map = {}              # val -> [list of indices into self.stack, Node pointer]
        self.head = Node(0)        # sentinel, freq 0
        self.tail = self.head      # highest-frequency node

    # ---- linked list helpers ----
    def _insert_after(self, node, freq):
        new = Node(freq)
        new.prev, new.next = node, node.next
        if node.next:
            node.next.prev = new
        node.next = new
        if self.tail is node:
            self.tail = new
        return new

    def _unlink(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.tail is node:
            self.tail = node.prev

    # ---- API ----
    def push(self, val: int) -> None:
        idx = len(self.stack)
        self.stack.append(val)

        if val not in self.map:
            self.map[val] = [[], self.head]
        idxs, cur = self.map[val]

        # node for freq + 1
        if cur.next and cur.next.freq == cur.freq + 1:
            nxt = cur.next
        else:
            nxt = self._insert_after(cur, cur.freq + 1)

        # move val from cur to nxt
        if cur is not self.head:
            cur.vals.discard(val)
            if not cur.vals:
                self._unlink(cur)
        nxt.vals.add(val)

        idxs.append(idx)
        self.map[val][1] = nxt

    def pop(self) -> int:
        top = self.tail
        # among max-frequency values, pick the one pushed most recently
        val = max(top.vals, key=lambda v: self.map[v][0][-1])
        idxs, _ = self.map[val]

        # remove from global stack
        i = idxs.pop()
        self.stack[i] = None
        while self.stack and self.stack[-1] is None:
            self.stack.pop()

        # move val down to freq - 1
        top.vals.discard(val)
        if top.freq - 1 == 0:
            del self.map[val]
        else:
            prev = top.prev
            if prev.freq != top.freq - 1:
                prev = self._insert_after(prev, top.freq - 1)
            prev.vals.add(val)
            self.map[val][1] = prev

        if not top.vals:
            self._unlink(top)

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
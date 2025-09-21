from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.queue = deque()
        self.packet_set = set()
        self.memoryLimit = memoryLimit
        self.dest_map = defaultdict(list)  # destination -> sorted timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False

        # Evict if full
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_ts = self.queue.popleft()
            self.packet_set.remove((old_src, old_dst, old_ts))
            # remove from dest_map
            idx = bisect.bisect_left(self.dest_map[old_dst], old_ts)
            if idx < len(self.dest_map[old_dst]) and self.dest_map[old_dst][idx] == old_ts:
                self.dest_map[old_dst].pop(idx)

        # Add new
        self.queue.append(key)
        self.packet_set.add(key)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        self.packet_set.remove((src, dst, ts))
        # remove from dest_map
        idx = bisect.bisect_left(self.dest_map[dst], ts)
        if idx < len(self.dest_map[dst]) and self.dest_map[dst][idx] == ts:
            self.dest_map[dst].pop(idx)
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left

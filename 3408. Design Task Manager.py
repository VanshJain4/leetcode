import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        # taskId -> (userId, priority)
        self.tasks = {}
        # heap of tuples: (-priority, -taskId, taskId, userId)
        self.heap = []

        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.tasks:
            userId, _ = self.tasks[taskId]
            self.tasks[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.tasks:
            del self.tasks[taskId]   # lazy delete; heap entry remains stale

    def execTop(self) -> int:
        # pop until we find a heap entry that matches the current tasks mapping exactly
        while self.heap:
            negPriority, negTaskId, taskId, userId = heapq.heappop(self.heap)
            if taskId in self.tasks:
                curUser, curPriority = self.tasks[taskId]
                # both priority and userId must match the current mapping
                if curPriority == -negPriority and curUser == userId:
                    del self.tasks[taskId]  # execute -> remove from system
                    return userId
            # otherwise stale entry: continue
        return -1

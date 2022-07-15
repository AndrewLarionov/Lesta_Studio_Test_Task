from collections import deque


class BufferFIFO(list):

    def put(self, element) -> None:
        self.append(element)

    def get(self) -> None:
        self.pop(0)


class AnotherBufferFIFO(deque):

    def put(self, element):
        self.append(element)

    def get(self):
        self.popleft()


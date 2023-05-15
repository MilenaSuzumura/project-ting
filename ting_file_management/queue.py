from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.__len__() != 0:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        if index >= 0 and index < self.__len__():
            return self._data[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")

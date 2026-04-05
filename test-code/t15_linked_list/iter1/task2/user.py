
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self._head: Node  = None
        self._current: Node = None

    def empty(self) -> bool:
        return self._head is None

    def reset(self):
        self._current = self._head

    def next(self):

        if self.empty() or self._current.next is None:
            raise StopIteration

        self._current = self._current.next

    def current(self):
        return self._current.item

    def insert_after(self,item):

        node = Node(item)

        if self.empty():
            self._head = self._current = node
            return

        node.next = self._current.next
        self._current.next = node

    def insert_before(self,item):

        self.insert_after(item)
        if self._current.next is not None:
            self._current.item, self._current.next.item = self._current.next.item, self._current.item
            self._current = self._current.next

    def delete(self):
        if self.empty():
            return
        if self._head is self._current:
            self._head = self._current = self._head.next
            return

        prev = self._head
        while prev.next is not self._current:
            prev = prev.next

        prev.next = self._current.next
        if self._current.next is None:
            self._current = prev
        else:
            self._current = self._current.next


    def damp(self):

        container = []
        pointer = self._head
        while pointer is not None:
            container.append(pointer.item)

            pointer = pointer.next

        return container


lst: LinkedList


def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = LinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return lst.empty()


def reset():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.reset()

def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    lst.next()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return lst.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    lst.insert_after(item)





def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    lst.insert_before(item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.delete()


def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return lst.damp()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Node:

    def __init__(self,item):
        self.item = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self._front: Node | None = None
        self._last: Node | None = None
        self._curr: Node | None = None

    def empty(self):
        return self._front is None

    def set_first(self):
        self._curr = self._front

    def set_last(self):
        self._curr = self._last

    def next(self):
        if self.empty() or self._curr.next is None:
             raise StopIteration
        self._curr = self._curr.next

    def prev(self):
        if self.empty() or self._curr.prev is None:
            raise StopIteration
        self._curr = self._curr.prev

    def current(self):
        return self._curr.item


    def insert_after(self,item):

        node = Node(item)
        if self.empty():
            self._curr = self._front = self._last = node
            return


        node.next = self._curr.next
        node.prev = self._curr

        if self._curr.next is None:
            self._last = node
        else:
            self._curr.next.prev = node

        self._curr.next = node

    def insert_before(self,item):

        node = Node(item)
        if self.empty():
            self._curr = self._front = self._last = node
            return

        node.next = self._curr
        node.prev = self._curr.prev

        if self._curr.prev is None:
            self._front = node
        else:
            self._curr.prev.next = node

        self._curr.prev = node


    def delete(self):
        if self.empty():
            return

        if self._front is self._last:
            self._front = self._curr = self._last = self._front.next
            return

        if self._curr is self._front:
            self._front = self._curr.next
        else:
            self._curr.prev.next = self._curr.next

        if self._curr is self._last:
            self._last = self._curr.prev
        else:
            self._curr.next.prev = self._curr.prev

        if self._curr.next is None:
            self._curr = self._curr.prev
        else:
            self._curr = self._curr.next


lst: DoublyLinkedList

def init():
    """ Викликається один раз на початку виконання програми. """
    global lst
    lst = DoublyLinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return lst.empty()


def set_first():
    """ Робить перший елемент списку, поточним.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_first()


def set_last():
    """ Робить останній елемент списку, поточним

    Переставляє поточний елемент на останній елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    lst.set_last()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    lst.next()


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    lst.prev()


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

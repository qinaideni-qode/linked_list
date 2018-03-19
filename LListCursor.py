#!/usr/bin/env python

#----------------------------------------------------------------------
# LListCursor.py
# Adam Myers
# 02/16/2016
#----------------------------------------------------------------------

import sys

from ListNode import ListNode

#----------------------------------------------------------------------

class LListCursor:
    
    '''LListCursor is a linked list where you can add/remove/access
    items at beginning, end, and a cursor position in the list

    class invariant:

        1. if the list is empty, self.head, self.cursor, self.tail are
        all None
        
        2. if the list is not empty, self.head, self.cursor, and
        self.tail alll point to an appropriate ListNode; self.head
        points to the first ListNode; self.tail points to the last
        ListNode; self.cursor points to a ListNode in the list

        3. inserting an item should not change self.cursor unless the
        list was empty, in which case self.cursor points to the one
        item in the list

        4. when deleting at the head or tail, self.cursor stays where
        it is unless it was at the head or tail; if cursor was at the
        head and the head was deleted, self.cursor now refers to the
        ListNode after it. if self.cursor was at the tail and the tail
        is deleted, self.cursor now refers to the ListNode before it

        5. when deleting the item at the cursor, self.cursor now
        refers to the ListNode after it, unless there is no ListNode
        after it in which case it refers to the ListNode before it.

        6. self.length indicates the number of items in the LListCursor
        '''
        
    #------------------------------------------------------------------
    
    def __init__(self, seq=None):

        '''initializes empty list or list with items in seq if it is
        not None'''

        self.head = None
        self.cursor = None
        self.tail = None
        self.length = 0
        if seq is not None:
            for x in seq:
                self.insertAtTail(x)
            
    #------------------------------------------------------------------

    def size(self):

        'returns number of items in the list'

        return self.length

    #------------------------------------------------------------------

    def __len__(self):

        'returns number of items in the list'

        return self.length

    #------------------------------------------------------------------

    def insertAtHead(self, item):

        '''post: item is inserted at beginning of the list (before the
        current head)'''

        newNode = ListNode(item)
        if self.head is None:
            self.head = newNode
            self.cursor = newNode
            self.tail = newNode
            self.length = 1
        else:
            newNode.link = self.head
            self.head = newNode
            self.length += 1
            

    
    #------------------------------------------------------------------

    def insertAfterCursor(self, item):

        'post: item is inserted after the cursor position'

        newNode = ListNode(item)
        if self.cursor is None:
            self.head = newNode
            self.cursor = newNode
            self.tail = newNode
        elif self.cursor is self.tail:
            self.cursor.link = newNode
            self.tail = newNode
        else:
            newNode.link = self.cursor.link
            self.cursor.link = newNode
        self.length += 1
    
    #------------------------------------------------------------------

    def insertAtTail(self, item):

        'post: item is inserted at end of list'

        newNode = ListNode(item)
        if self.tail is None:
            self.head = newNode
            self.cursor = newNode
            self.tail = newNode
        else:
            self.tail.link = newNode
            self.tail = newNode
        self.length += 1
    
    #------------------------------------------------------------------

    def removeItemAtHead(self):

        '''removes item at head of list

        pre: list is not empty

        post: first item is removed from the list; IndexError raised
        if list empty otherwise the item that was removed is returned'''

        if self.length == 0:
            # raise IndexError if list is empty
            raise IndexError('removeItemAtHead called on empty LListCursor')
        else:
            self.length -= 1
            # get item so can return it later
            item = self.head.item
            # if list is empty after the deletion
            if self.length == 0:
                # make all ListNode instance vars None
                self.head = self.cursor = self.tail = None
            else:
                # if cursor was at head
                if self.cursor is self.head:
                    # move cursor forward to new first item
                    self.cursor = self.cursor.link
                # move head forward to new first item
                self.head = self.head.link

        return item

    #------------------------------------------------------------------

    def removeItemAtCursor(self):

        '''removes item at cursor position

        pre: list is not empty

        post: item at cursor position is removed from the list;
        IndexError raised if list empty otherwise the item that was
        removed is returned; the cursor now points to the newNode after
        the original cursor unless the cursor was the last item in
        which case the cursor is now the new last item'''


        if self.length == 0:
            raise IndexError('removeItemAtCursor called on empty LListCursor')
        else:
            self.length -= 1
            item = self.cursor.item
            if self.length == 0:
                self.head = self.cursor = self.tail = None
            else:
                if self.cursor is self.tail:
                    currentnewNode = self.head
                    while not currentnewNode.link is self.tail:
                        currentnewNode = currentnewNode.link
                    self.cursor = currentnewNode
                    self.tail = currentnewNode
                    currentnewNode.link = None
                elif self.cursor is self.head:
                    self.cursor = self.cursor.link
                    self.head = self.head.link
                else:
                    currentnewNode = self.head
                    while not currentnewNode.link is self.cursor:
                        currentnewNode = currentnewNode.link
                    self.cursor = self.cursor.link
                    currentnewNode.link = self.cursor
        
        return item
    
    #------------------------------------------------------------------

    def removeItemAtTail(self):

        '''removes item at end of list

        pre: list is not empty

        post: last item is removed from the list; IndexError raised if
        list empty otherwise the item that was removed item is
        returned'''

        if self.length == 0:
            raise IndexError('removeItemAtCursor called on empty LListCursor')
        else:
            self.length -= 1
            item = self.tail.item
            if self.length == 0:
                self.head = self.cursor = self.tail = None
            else:
                currentnewNode = self.head
                while not currentnewNode.link is self.tail:
                    currentnewNode = currentnewNode.link
                if self.cursor is self.tail:
                    self.cursor = currentnewNode
                self.tail = currentnewNode

        return item

    #------------------------------------------------------------------

    def itemAtHead(self):

        '''returns item at head of list

        pre: list is not empty

        post: first item in list is returned; IndexError raised if
        list empty'''

        if self.length == 0:
            raise IndexError('removeItemAtCursor called on empty LListCursor')
        else:
            item = self.head.item

        return item
    
    #------------------------------------------------------------------

    def itemAtCursor(self):

        '''returns item at cursor position

        pre: list is not empty

        post: item at cursor position in list is returned; IndexError
        raised if list empty'''

        if self.length == 0:
            raise IndexError('removeItemAtCursor called on empty LListCursor')
        else:
            item = self.cursor.item

        return item
    
    #------------------------------------------------------------------

    def itemAtTail(self):

        '''returns item at end of list

        pre: list is not empty

        post: last item in list is returned; IndexError raised if
        list empty otherwise the item that was removed is returned'''

        if self.length == 0:
            raise IndexError('removeItemAtCursor called on empty LListCursor')
        else:
            item = self.tail.item

        return item
    
    #------------------------------------------------------------------

    def cursorToStart(self):

        'move cursor to start of list'
        
        self.cursor = self.head
    
    #------------------------------------------------------------------

    def cursorForward(self):

        '''move cursor forward one item

        post: returns True if cursor was moved forward or False if
        list empty or cursor already at end of list'''

        #use what wrote in removeAtCursor to find what was before cursor
        if self.length == 0:
            return False
        elif self.cursor is self.tail:
            return False
        else:
            self.cursor = self.cursor.link
            return True
    
    #------------------------------------------------------------------

    def __iter__(self):

        'iterators over items in list yielding one item at a time'

        # start at beginning of list
        newNode = self.head
        # while newNodes left
        while newNode is not None:
            # yield item
            yield newNode.item
            # and move newNode forward
            newNode = newNode.link

    #------------------------------------------------------------------

    def __add__(self, other):

        '''retuns a new LListCursor that is the catenation of self and other

        pre: other is a LListCursor object

        post: retuns a new LListCursor that is the catenation of self
        and other with the cursor of the result at the head'''

#for loop using __iter__ method

        newList = LListCursor()
        for item in self:
            newList.insertAtTail(item)
        for item in other:
            newList.insertAtTail(item)
        return newList
    
    #------------------------------------------------------------------

#----------------------------------------------------------------------

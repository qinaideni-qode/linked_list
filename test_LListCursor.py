#!/usr/bin/env python3

#----------------------------------------------------------------------
# test_LListCursor.py
# Adam Myers
# 02/16/2016
#----------------------------------------------------------------------

import unittest
import sys
sys.path.insert(0, '..')

from LListCursor import LListCursor

#----------------------------------------------------------------------

class LListTest(unittest.TestCase):

    #------------------------------------------------------------------


#check all special cases in LListCursor.py

    def checkList(self, linked, lst, cursor):
        self.assertEqual(len(linked), len(lst))
        self.assertEqual(linked.size(), len(lst))
        items = []
        for x in linked:
            items.append(x)
        self.assertEqual(items, lst)
        if len(lst) > 0:
            self.assertEqual(linked.itemAtHead(), lst[0], 'head wrong')
            self.assertEqual(linked.itemAtTail(), lst[-1], 'tail wrong')
            self.assertEqual(linked.itemAtCursor(), cursor, 'cursor wrong')
            
    #------------------------------------------------------------------

    def testInit(self):

        items = LListCursor()
        self.assertEqual(items.size(), 0)
    
    #------------------------------------------------------------------

    def testInitInstanceVars(self):

        items = LListCursor()
        self.assertEqual(items.length, 0)
        self.assertEqual(items.head, None)
        self.assertEqual(items.cursor, None)
        self.assertEqual(items.tail, None)
    
    #------------------------------------------------------------------

    def testAtHeadRaisesIndexError(self):

        items = LListCursor()
        self.assertRaises(IndexError, items.itemAtHead)

    #------------------------------------------------------------------

    def testInsertAtHead(self):

        items = LListCursor()
        for i in range(3, -1, -1):
            items.insertAtHead(i)
        self.checkList(items, list(range(4)), 3)
    
    #------------------------------------------------------------------
        
    #------------------------------------------------------------------

#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)

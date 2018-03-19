#!/usr/bin/env python

#----------------------------------------------------------------------
# ListNode.py
# Adam Myers
# 02/16/2016
#----------------------------------------------------------------------

import sys

#----------------------------------------------------------------------

class ListNode:

    '''A single-linked structure'''
    
    #----------------------------------------------------------------------
    
    def __init__(self, item = None, link = None):

        '''creates a linked with the specified data value and link
        pre: None
        post: creates a linked with the specified data value and link'''
        
        self.item = item
        self.link = link
        
#----------------------------------------------------------------------

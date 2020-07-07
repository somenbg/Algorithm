#!/bin/python3

import math
import os
import random
import re
import sys


class Node():

    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_complete_ind = False
        self.counter = 1


class Contact():

    def __init__(self, root):
        self.root = Node(root)

    def add_name(self, name):

        node = self.root

        for char in name:
            found_in_child = False

            for child in node.children:

                if child.char == char:
                    found_in_child = True
                    child.counter += 1
                    node = child
                    break

            if not found_in_child:
                new_node = Node(char)
                node.children.append(new_node)
                node = new_node
        
        node.word_complete_ind = True
        print('"{}" added to the contact list'.format(name))
    
    def find_name(self, name):

        node = self.root

        if not node.children:
            return print(0)

        for char in name:

            name_not_found = True

            for child in node.children:

                if child.char == char:
                    name_not_found = False
                    node = child

            if name_not_found:
                return print(0)

        return print(node.counter)




if __name__ == '__main__':
    # n = int(input())
    input_list = ['add hack', 'add hackerrank', 'find hac', 'find hak']

    node = Contact('*')

    # for n_itr in range(n):
    for input in input_list:
        opContact = input.split()

        op = opContact[0]

        contact = opContact[1]

        if op == 'add':
            node.add_name(contact)
        elif op == 'find':
            node.find_name(contact)
        else:
            print('Function {} not defined'.format(op))

        

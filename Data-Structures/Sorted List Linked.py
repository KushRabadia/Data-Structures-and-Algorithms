#imports
from copy import deepcopy

class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_ListNode)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        return self._front==None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        if self._front is None:
            # Priority queue is empty
            node = _SL_Node(value, None)
            self._front = node
            self._rear = node
        elif value < self._front._value:
            # New value has highest priority
            node = _SL_Node(value, self._front)
            self._front = node
        elif value >= self._rear._value:
            # New values has lowest priority
            node = _SL_Node(value, None)
            self._rear._next = node
            self._rear = node
        else:
            # Find the proper position for value.
            prev = None
            curr = self._front

            while value >= curr._value:
                prev = curr
                curr = curr._next

            # Create the new node and link it to curr.
            node = _SL_Node(value, curr)
            # The previous node is linked to the new node.
            prev._next = node
        # Increment the priority queue size.
        self._count += 1
        return


    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        previous = None
        current = self._front
        index= 0
       
        while current is not None and current._value !=key:
            previous = current
            current = current._next
            index += 1
       
        if current is None:
            index = -1
       
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        previous, current, index = self._linear_search(key)
        if index == -1:
            value = None
        else:
            value = current._value
            self._count -= 1
            if index == 0:
                self._front = self._front._next
                if self._front is None:
                    self._rear = None
            else:
                previous._next = current._next
                if previous._next is None:
                    self._rear = previous
       
        return value

        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        
        value = self._front._value
        self._count -= 1
        self._front = self._front._next
        if self._front is None:
            self._rear = None
        return value

        return

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """

        prev = None
        current = self._front
        
        while current is not None:
            if self._front._value == key:
                self._front = self._front._next
                if self._front is None:
                    self._rear = None
                self._count-=1
            elif current._value == key:
                prev._next = current._next
                if prev._next is None:
                    self._rear = prev
                self._count-=1
            prev = current
            current = current._next
            
            
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        _, current, _ = self._linear_search(key)
       
       
        if current is not None:
            value = deepcopy(current._value)
        else:
            value = None
           
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = self._front._value
        return deepcopy(value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """

        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front
        if i < 0:
            i = self._count + i
        j = 0
        
        while j<i:
            current = current._next
            j+=1
        value = deepcopy(current._value)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """

        is_containing = False
        _, _, i = self._linear_search(key)
        if i != -1:
            is_containing = True
        return is_containing

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        value = self._rear._value
        
        return deepcopy(value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        value =  self._front._value
        
        return  deepcopy(value)

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """

        number = 0
        current = self._front

        while current is not None:
            if key == current._value:
                number += 1
            current = current._next
        return number
    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        temp = []
        previous = None
        current = self._front
        
        while current is not None:
            if current._value not in temp:
                temp.append(current._value)
                previous = current
            else:
                previous._next = current._next
                self._count-=1
            
            current = current._next
            
            if current is None:
                self._rear = previous
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                args[0] = self._count + args[0]
            j = 0

            while j < args[0]:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1


        return value


    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    
                    node = _SL_Node(value, None)

                    if self._front is None:
                        self._front = node
                    else:
                        self._rear._next = node
                    self._rear = node
                    self._count += 1
                

            source1_node = source1_node._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                node = _SL_Node(value, None)

                if self._front is None:
                    self._front = node
                else:
                    self._rear._next = node
                self._rear = node
                self._count += 1
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                node = _SL_Node(value, None)

                if self._front is None:
                    self._front = node
                else:
                    self._rear._next = node
                self._rear = node
                self._count += 1

            source2_node = source2_node._next
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        # your code here

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """

        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            target_node = other._front
            
            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next
                
            identical = source_node is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        new_list = deepcopy(self)

        return new_list

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._front is not None and source2._front is not None:
            self.insert(source1.pop(0))
            self.insert(source2.pop(0))
        while source1._front is not None:
            self.insert(source1.pop(0))
        while source2._front is not None:
            self.insert(source2.pop(0))
        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

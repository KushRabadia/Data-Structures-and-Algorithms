from copy import deepcopy

class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []
        

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """
        if len(self._values) == 0:
            result = True
        else:
            result = False
        
        return result       
        
    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        
    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        value = self._values[len(self._values)-1]
        del(self._values[len(self._values) - 1])
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        value = self._values[len(self._values)-1]
        return deepcopy(value)


    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
        
    def split_alt(self):
        """
        ------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -----------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        
        v = 0
                
        while len(self._values) != 0:
            value = self._values[len(self._values)-1]
            self._values.pop(len(self._values) - 1)
            if v%2 == 0:
                target1._values.append(deepcopy(value))
            else:
                target2._values.append(deepcopy(value))
            v+=1     
           
        return(target1,target2)

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        v = 0
        while len(source1._values)>0 or len(source2._values)>0:
            if len(source1._values)>0 and len(source2._values)>0:
                if v%2==0:
                    value = source1._values[len(source1._values)-1]
                    source1._values.pop(len(source1._values) - 1)
                else:
                    value = source2._values[len(source2._values)-1]
                    source2._values.pop(len(source2._values) - 1)
            elif len(source1._values)==0:
                value = source2._values[len(source2._values)-1]
                source2._values.pop(len(source2._values) - 1)
            else:
                value = source1._values[len(source1._values)-1]
                source1._values.pop(len(source1._values) - 1)
            self._values.append(deepcopy(value))
            v+=1

class MinStack(object):

    def __init__(self):
        # Initialize two stacks: one for regular values and one for tracking the minimum values
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # If the min_stack is empty or the current value is smaller than or equal to the current minimum,
        # push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            popped_val = self.stack.pop()
            # If the popped value is the current minimum, pop from the min_stack as well
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]

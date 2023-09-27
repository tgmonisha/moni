class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.head.data
        self.head = self.head.next
        return data

def evaluate_postfix(expression):
    stack = LinkedList()
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.push(result)

    if not stack.is_empty():
        return stack.pop()
    else:
        raise Exception("Invalid postfix expression")

def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise Exception("Division by zero")
        return operand1 / operand2

if __name__ == "__main__":
    postfix_expression = "(55)*5+2-"
    result = evaluate_postfix(postfix_expression)
    print(f"Result of {postfix_expression} is {result}")


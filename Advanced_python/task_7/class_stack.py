
class Stack:

    def __init__(self):

        self.stack = self.create_list()

    @staticmethod
    def create_list():

        return []

    def is_empty(self):

        flag = not bool(self.stack)

        return flag

    def push(self, new_element):

        self.stack.append(new_element)

    def pop(self):

        last_element = self.stack.pop()

        return last_element

    def peek(self):

        last_element = self.stack[-1]

        return last_element

    def size(self):

        length = len(self.stack)

        return length

    def clear(self):

        count = self.size()
        for i in range(count):
            self.pop()

    @staticmethod
    def is_balance(item: str) -> bool:

        while any(i in item for i in ("()", "[]", "{}")):
            if "()" in item:
                item = item.replace("()", "")
            if "[]" in item:
                item = item.replace("[]", "")
            if "{}" in item:
                item = item.replace("{}", "")

        return True if len(item) == 0 else False

from class_stack import Stack
# from mail import Email


if __name__ == '__main__':

    # Задание 1
    stack = Stack()
    print("Is empty", stack.is_empty())
    stack.push(1)
    print("Is empty", stack.is_empty())
    el = stack.pop()
    print("Last", el)
    print("Is empty", stack.is_empty())
    stack.push(999)
    new_el = stack.peek()
    print("Last", new_el)
    print("Is empty", stack.is_empty())
    stack.push(1_000_000)
    print("Size", stack.size())
    stack.pop()
    stack.pop()
    print("Size", stack.size())

    # Задание 2
    balance = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}"]
    not_balance = ["}{}", "{{[(])}}", "[[{())}]"]

    for b in balance:
        b = list(b)
        count = len(b)
        for i in range(count):
            if b[0] in ('(', '[', '{'):
                stack.push(new_element=b[0])
                del b[0]
            elif stack.size() > 0 and (stack.peek() + b[0] in ('()', '[]', '{}')):
                stack.pop()
                del b[0]
            else:
                stack.push(new_element=b[0])
                del b[0]
        print(True if not stack.size() else False)
        stack.clear()
    print()

    for b in not_balance:
        b = list(b)
        count = len(b)
        for i in range(count):
            if b[0] in ('(', '[', '{'):
                stack.push(new_element=b[0])
                del b[0]
            elif stack.size() > 0 and (stack.peek() + b[0] in ('()', '[]', '{}')):
                stack.pop()
                del b[0]
            else:
                stack.push(new_element=b[0])
                del b[0]
        print(True if not stack.size() else False)
        stack.clear()

    # # Задание 3
    # GMAIL_SMTP = "smtp.gmail.com"
    # GMAIL_IMAP = "imap.gmail.com"
    #
    # l = 'login@gmail.com'
    # password = 'qwerty'
    # subject = 'Subject'
    # recipients = ['vasya@email.com', 'petya@email.com']
    # message = 'Message'
    # header = None
    #
    # mail = Email(login=l, password=password, GMAIL_IMAP=GMAIL_IMAP, GMAIL_SMTP=GMAIL_SMTP)
    # mail.send_message(subject=subject, recipients=recipients, message=message)
    # recieve_message = mail.recieve_message()
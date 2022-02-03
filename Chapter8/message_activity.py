def show_messages(msg_list):
    """Display messages from a stored list"""
    for msg in msg_list:
        print(msg)

def send_messages(msg_list,sent_list):
    """Send a list of pending messages, clearing them out as they're sent, and store them in a new list of sent messages"""
    while msg_list:
        currentText = msg_list.pop()
        print(currentText)
        sent_list.append(currentText)
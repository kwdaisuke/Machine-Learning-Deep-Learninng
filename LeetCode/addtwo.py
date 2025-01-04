class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    """
    Add two numbers represented by linked lists.

    :param l1: First linked list.
    :param l2: Second linked list.
    :return: Linked list representing the sum of the two numbers.
    """

    # Dummy node to start the result linked list
    dummy = ListNode()
    current = dummy

    carry = 0

    # Traverse both lists
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        sum_val = total % 10

        # Add the sum to the linked list
        current.next = ListNode(sum_val)
        current = current.next

        # Move to the next nodes
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to list
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Test the function with the provided examples
l1_example1 = create_linked_list([2, 4, 3])
l2_example1 = create_linked_list([5, 6, 4])
result_example1 = add_two_numbers(l1_example1, l2_example1)

l1_example2 = create_linked_list([0])
l2_example2 = create_linked_list([0])
result_example2 = add_two_numbers(l1_example2, l2_example2)

l1_example3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2_example3 = create_linked_list([9, 9, 9, 9])
result_example3 = add_two_numbers(l1_example3, l2_example3)

linked_list_to_list(result_example1), linked_list_to_list(result_example2), linked_list_to_list(result_example3)

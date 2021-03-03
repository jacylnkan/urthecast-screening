def merge_list(orig, to_add, to_del):
    """
    Merges orig and to_add such that all elements are unique and do not appear in to_del.
    Sorts resulting list by number of character count (decreasing). In case of a tie, orders
    in reverse alphabetical order.

    Args:
        orig (list): Original list
        to_add (list): List to add to original list
        to_del (list): List of elements to remove from resulting list

    Returns:
        list: List sorted according to problem description.
    """
    unsorted = list(set([item for item in orig + to_add if item not in to_del]))
    merged = sorted(sorted(unsorted, reverse=True), key=len, reverse=True)
    return merged

orig_list = ['one', 'two', 'three']
add_list = ['one', 'two', 'five', 'six']
del_list = ['two', 'five']
print(merge_list(orig_list, add_list, del_list))
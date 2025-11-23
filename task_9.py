# Find Common Elements Between Two Lists

def common_elements(list1, list2):
    return list(set(list1) & set(list2))


# Example usage
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Should return [3, 4]
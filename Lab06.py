"""
Lab 06: Implementation and Analysis of Searching, Sorting, and Recursive Algorithms
PART A: Searching Algorithms
"""

# ============================================================================
# TASK 1: LINEAR SEARCH
# ============================================================================

def linear_search(lst, element):
    """
    Performs linear search on a list to find an element.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        lst: List to search in
        element: Element to find
    
    Returns:
        Position of element (1-indexed) if found, otherwise -1
    """
    for i in range(len(lst)):
        if lst[i] == element:
            return i + 1  # Return 1-indexed position
    return -1


def test_linear_search():
    """Test case for linear search"""
    print("=" * 60)
    print("TASK 1: LINEAR SEARCH")
    print("=" * 60)
    
    lst = [10, 20, 30, 40, 50]
    print(f"List: {lst}")
    
    element = int(input("Enter element to search: "))
    position = linear_search(lst, element)
    
    if position != -1:
        print(f"Element found at position {position}")
    else:
        print(f"Element not found in the list")
    print()


# ============================================================================
# TASK 2: INDEXED SEARCH (BLOCK SEARCH)
# ============================================================================

import math

def indexed_search(lst, element, block_size=None):
    """
    Performs indexed (block) search on a sorted list.
    Assumes the list is sorted.
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    Args:
        lst: Sorted list to search in
        element: Element to find
        block_size: Size of each block (default: √n)
    
    Returns:
        True if found, False otherwise
    """
    n = len(lst)
    
    # If block_size is not provided, calculate it as sqrt(n)
    if block_size is None:
        block_size = int(math.sqrt(n))
    
    # Find the block where element is likely to be
    prev = 0
    while lst[min(block_size, n) - 1] < element:
        prev = block_size
        block_size += int(math.sqrt(n))
        if prev >= n:
            return False
    
    # Linear search within the block
    while lst[prev] < element:
        prev += 1
        if prev == min(block_size, n):
            return False
    
    # Check if element is found
    if lst[prev] == element:
        return True
    
    return False


def test_indexed_search():
    """Test case for indexed search"""
    print("=" * 60)
    print("TASK 2: INDEXED SEARCH (BLOCK SEARCH)")
    print("=" * 60)
    
    lst = [5, 10, 15, 20, 25, 30]
    print(f"List: {lst}")
    
    element = int(input("Enter element: "))
    
    if indexed_search(lst, element):
        print("Element found")
    else:
        print("Element not found")
    print()


# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main menu for the searching algorithms"""
    while True:
        print("=" * 60)
        print("SEARCHING ALGORITHMS - PART A")
        print("=" * 60)
        print("1. Linear Search")
        print("2. Indexed Search")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            test_linear_search()
        elif choice == '2':
            test_indexed_search()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()

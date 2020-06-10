### To create the Union and Intersection functions, I used a set to find all the values in the linked lists - without repeating them - and a dictionary to discover the common elements, respectively. The union process takes O(n), the highest linked list size, and the intersection takes O(n + m), the size of both linked lists, that is a time complexity of O(n) in total. The space complexity is also O(n), the size of the set, the dictionary, and the new linked list.
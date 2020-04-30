import sys

class Node(object):

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
    
    def get_left_child(self):
        return self.left
    
    def set_left_child(self, node):
        self.left = node
    
    def get_right_child(self):
        return self.right
    
    def set_right_child(self, node):
        self.right = node
        
    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None

def huffman_encoding(data):
    if len(data) <= 1:
        return None, None

    frequencies_array = find_frequencies(data)

    tree = make_tree(frequencies_array)

    return encode_message(data, tree), tree

def huffman_decoding(data,tree):
    if len(data) == 0 and tree == None:
        return None

    return decode_message(data, tree)

def find_frequencies(data):
    aux_dict = {}

    for i in range(len(data)):
        if not data[i] in aux_dict:
            aux_dict[data[i]] = 1
        else:
            aux_dict[data[i]] += 1
    
    frequencies_array = []

    for key, value in aux_dict.items():
        frequencies_array.append((value, key))

    return sorted(frequencies_array)

def make_tree(frequencies_array):
    if len(frequencies_array) == 1:
        return frequencies_array[0]

    first_smaller = frequencies_array.pop(0)
    second_smaller = frequencies_array.pop(0)
    
    node = Node()

    if not is_tuple(first_smaller):
        node.set_value(first_smaller.get_value())
        node.set_left_child(first_smaller)
    else:
        node.set_value(first_smaller[0])
        node.set_left_child(first_smaller[1])
    
    if not is_tuple(second_smaller):
        node.set_value(node.get_value() + second_smaller.get_value())
        node.set_right_child(second_smaller)
    else:
        node.set_value(node.get_value() + second_smaller[0])
        node.set_right_child(second_smaller[1])

    index_to_insert_node = 0

    while True:
        if len(frequencies_array) == index_to_insert_node or len(frequencies_array) == 0:
            break

        if is_tuple(frequencies_array[index_to_insert_node]):
            if node.get_value() > frequencies_array[index_to_insert_node][0]:
                index_to_insert_node += 1
            else:
                break
        else:
            if node.get_value() > frequencies_array[index_to_insert_node].get_value():
                index_to_insert_node += 1
            else:
                break

    frequencies_array.insert(index_to_insert_node, node)

    return make_tree(frequencies_array)

def is_tuple(data):
    if type(data) is tuple:
        return True
    return False

def is_string(data):
    if type(data) is str:
        return True
    return False

def traverse(node, message, aux_dict, method):
    if is_string(node):
        if method == 0:
            aux_dict[node] = message
        else:
            aux_dict[message] = node

    if node:
        if not is_string(node):
            message += "0"
            traverse(node.get_left_child(), message, aux_dict, method)
            message = message[0:-1]
            message += "1"
            traverse(node.get_right_child(), message, aux_dict, method)

def encode_message(data, tree):
    message = ""
    aux_dict = {}
    
    traverse(tree, message, aux_dict, 0)

    for i in range(len(data)):
        message += aux_dict[data[i]]

    return message

def decode_message(data, tree):
    message = ""
    aux_dict = {}
    
    traverse(tree, message, aux_dict, 1)

    code = ""
    for i in range(len(data) - 1):
        if code not in aux_dict or code + data[i + 1] in aux_dict:
            code += data[i]
        else:
            message += aux_dict[code]
            code = data[i]

        if i == len(data) - 2:
            code += data[i + 1]
            message += aux_dict[code]
    
    return message

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence))) # returns 69 because is the original string size
    print ("The content of the data is: {}\n".format(a_great_sentence)) # returns the original string

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data and tree:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # returns 36 because is the encoded string size
        print ("The content of the encoded data is: {}\n".format(encoded_data)) # returns the string content

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # returns 69 because is the decoded string size
        print ("The content of the encoded data is: {}\n".format(decoded_data)) # returns the string content


    edge_sentence_1 = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(edge_sentence_1))) # returns 49 because is the memory size of an empty string
    print ("The content of the data is: {}\n".format(edge_sentence_1)) # returns the empty string

    print(huffman_encoding(edge_sentence_1), "\n") # returns (None, None) because it's not possible to encode an empty string

    edge_sentence_2 = "a"

    print ("The size of the data is: {}\n".format(sys.getsizeof(edge_sentence_2))) # returns 50 because is the memory size of a string with only one character
    print ("The content of the data is: {}\n".format(edge_sentence_2)) # returns the string

    print(huffman_encoding(edge_sentence_2), "\n") # returns (None, None) because it's not possible to encode a string with only one character

    edge_sentence_3 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

    print ("The size of the data is: {}\n".format(sys.getsizeof(edge_sentence_3))) # returns 623 because is the original string size
    print ("The content of the data is: {}\n".format(edge_sentence_3)) # returns the original string

    encoded_data, tree = huffman_encoding(edge_sentence_3)

    if encoded_data and tree:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # returns 364 because is the encoded string size
        print ("The content of the encoded data is: {}\n".format(encoded_data)) # returns the string content

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # returns 623 because is the decoded string size
        print ("The content of the encoded data is: {}\n".format(decoded_data)) # returns the string content

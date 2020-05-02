import hashlib
import datetime

class Block:

      def __init__(self, timestamp, data, previous_hash):
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.calc_hash()

      def calc_hash(self):
            sha = hashlib.sha256()

            hash_str = '{}:{}:{}'.format(
                  self.timestamp, self.data, self.previous_hash
            ).encode('utf-8')

            while not sha.hexdigest().startswith('0000'):
                  sha.update(hash_str)

            return sha.hexdigest()

class Node:

      def __init__(self, block):
            self.value = block
            self.next = None

class Blockchain:

      def __init__(self):
            self.head = None
            self.tail = None

      def add_block(self, data):
            if data == "" or data is None:
                  return None
            
            def new_block(data, previous_hash):
                  return Node(Block(get_time_now(), data, previous_hash))

            if not self.head:
                  self.head = new_block(data, 0)
                  self.tail = self.head
            else:
                  self.tail.next = new_block(data, self.tail.value.hash)
                  self.tail = self.tail.next
            
      def print_blockchain(self):
            if self.head is None:
                  return None

            current_node = self.head
            while current_node:
                  print("Timestamp: {}\nData: {}\nHash: {}\nPrevious hash: {}\n".format(
                        current_node.value.timestamp,
                        current_node.value.data,
                        current_node.value.hash,
                        current_node.value.previous_hash
                  ))
                  current_node = current_node.next

def get_time_now():
      return datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %m/%d/%Y")

# Test case 1

blockchain = Blockchain()

blockchain.add_block("Some information")
blockchain.add_block("Some information")
blockchain.add_block("Some information")

blockchain.print_blockchain() # returns the blocks information  

# Test case 2

blockchain_2 = Blockchain()

blockchain_2.add_block("") # the block won't be addded

blockchain_2.print_blockchain() # returns nothing because the block wasn't added

# Test case 3

blockchain_3 = Blockchain()

blockchain_3.add_block(None) # the block won't be addded

blockchain_3.print_blockchain() # returns nothing because the block wasn't added

# Test case 4

blockchain_4 = Blockchain()

blockchain_4.add_block("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur at ante sit amet dolor elementum aliquet. Curabitur id lectus faucibus, ultricies arcu eu, porta justo. Nullam eget ligula et arcu ultricies sodales. Donec gravida ipsum vitae arcu blandit vestibulum. Sed sed ex purus. Morbi semper sollicitudin ornare. Sed est urna, porttitor vitae porttitor ut, rhoncus eget ante. Fusce vestibulum, metus mattis vehicula varius, dui magna interdum tortor, semper tempor nunc libero ultrices ligula. Curabitur suscipit est eget velit ultricies ultrices. Maecenas pretium mauris quis maximus hendrerit. Sed sodales mi eget nibh varius feugiat. Integer vitae tempor justo. Sed ut erat a arcu ullamcorper porta.")
blockchain_4.add_block("Sed consectetur, tellus eu varius lacinia, urna diam pulvinar elit, sit amet scelerisque metus odio efficitur ante. Donec at leo eget ex venenatis venenatis. Phasellus iaculis sem eget sodales ornare. Donec commodo nec massa quis mattis. Maecenas ultrices ornare condimentum. Praesent scelerisque orci id ornare interdum. Vestibulum fermentum metus non consectetur viverra. Vestibulum tristique sem vel fringilla pretium.")
blockchain_4.add_block("Quisque in justo et augue aliquam cursus non ac nunc. Vivamus elementum metus in ultrices congue. Nam lacinia ante dolor, at feugiat tortor ullamcorper at. Proin quis ante ultrices tortor elementum viverra. Duis venenatis est non consectetur pellentesque. Mauris sit amet odio varius, ultrices ante id, vehicula nisl. Fusce nec pharetra neque. Aliquam suscipit erat mauris, commodo posuere magna egestas sed. Maecenas tincidunt a enim eget tincidunt. Sed auctor posuere urna. Mauris vel enim commodo, eleifend magna eget, aliquet eros. Ut pulvinar leo in arcu vehicula interdum. Curabitur sed elit et orci faucibus iaculis sit amet et ipsum.")
blockchain_4.add_block("Nunc maximus cursus odio sit amet tempor. Aliquam pellentesque mauris eu vehicula aliquet. Nullam auctor porttitor urna. Nullam feugiat iaculis neque, sit amet ullamcorper sem pretium eu. Praesent vehicula eget dolor at ullamcorper. Quisque nisl turpis, semper non enim sed, sagittis auctor elit. Fusce hendrerit lobortis erat id lacinia. Maecenas facilisis elementum aliquam.")
blockchain_4.add_block("Nam rutrum pharetra mauris. Mauris quam massa, pretium sit amet posuere id, cursus vitae ligula. Etiam eu laoreet sapien, ut porttitor velit. Mauris malesuada egestas dui quis venenatis. Quisque ullamcorper pharetra orci, vitae pulvinar felis dignissim ut. Curabitur fringilla dignissim vulputate. Curabitur sagittis varius nulla. Proin aliquam, enim ut elementum venenatis, dui odio pellentesque nisi, eget posuere massa elit in dolor. Curabitur porta turpis vel justo laoreet, vel scelerisque ex faucibus. Fusce a cursus velit.")

blockchain_4.print_blockchain() # returns the blocks information 

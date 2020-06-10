# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, route, handler, handler_not_found, root = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if root is None:
            root = self.root

        aux_route = route.pop(0)

        if len(route) == 0:
            root.insert(aux_route, handler)
        else:
            if aux_route not in root.children:
                root.insert(aux_route, handler_not_found)

            self.insert(route, handler, handler_not_found, root.children[aux_route])

    def find(self, route):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match 
        current = self.root

        for current_route in route:
            if current_route not in current.children:
                return None
            current = current.children[current_route]
        
        return current

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, route, handler):
        # Insert the node as before
        if route not in self.children:
            self.children[route] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, handler_not_found):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.handler_not_found = handler_not_found
        self.routes = RouteTrie(handler)

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routes.insert(list(filter(lambda x: x != "", self.split_path(route))), handler, self.handler_not_found)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        result = self.routes.find(list(filter(lambda x: x != "", self.split_path(route))))

        if result is None:
            return self.handler_not_found
        
        return result.handler

    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return route.split('/')

# Test case 1

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'

# Test case 2

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home", "home handler")  # add a route
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/signin/", "signin handler")  # add a route
router.add_handler("/signout/", "signout handler")  # add a route
router.add_handler("/home/profile", "profile handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'home handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("signin")) # should print 'signin handler'
print(router.lookup("signout/")) # should print 'signout handler'
print(router.lookup("profile")) # should print 'not found handler'
print(router.lookup("home/profile")) # should print 'profile handler'

# Test case 3 - edge cases

try:
    router = Router("", "")
    router.add_handler("", "")
    print(router.lookup(""))

    router = Router(None, None)
    router.add_handler(None, None)
    print(router.lookup(None))

except IndexError: print('Invalid Arguments')
except AttributeError: print('Invalid Arguments')
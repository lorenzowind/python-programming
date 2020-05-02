class Group(object):

    def __init__(self, _name):
        if _name == "" or _name == None:
            return None

        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        if user == "" or user == None:
            return None

        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return find_group(user, group)
    
def find_group(user, group):
    if len(group.users) != 0:
        if find_user(user, group, 0):
            return True

    if len(group.groups) != 0:
        for index in range(len(group.groups)):
            if find_group(user, group.groups[index]):
                return True

    return False

def find_user(user, group, index):
    if index == len(group.users):
        return False

    elif group.users[index] == user:
        return True

    return find_user(user, group, index + 1)

# Test case 1

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent)) # returns True

# Test case 2

group_01 = Group("group 01")
group_01.add_user("user 01")
group_01.add_user("user 02")
group_01.add_user("user 03")
group_01.add_user("user 04")
group_01.add_user("user 05")

group_02 = Group("group 02")
group_02.add_user("user 06")
group_02.add_user("user 07")
group_02.add_user("user 08")

group_03 = Group("group 03")
group_03.add_user("user 15")

group_04 = Group("group 04")
group_04.add_user("user 16")
group_04.add_user("user 17")

group_05 = Group("group 05")
group_05.add_user("user 09")

group_06 = Group("group 06")
group_06.add_user("user 10")
group_06.add_user("user 11")
group_06.add_user("user 12")
group_06.add_user("user 13")

group_07 = Group("group 07")
group_07.add_user("user 14")

group_01.add_group(group_02)
group_01.add_group(group_05)
group_01.add_group(group_06)

group_02.add_group(group_03)
group_02.add_group(group_04)

group_06.add_group(group_07)

# group 01 - ["user 01", "user 02", "user 03", "user 04", "user 05"]
#   group 02 - ["user 06", "user 07", "user 08"]
#     group 03 - ["user 15"]
#     group 04 - ["user 16", "user 17"]
#   group 05 - ["user 09"]
#   group 06 - ["user 10", "user 11", "user 12", "user 13"]
#     group 07 - ["user 14"]

print(is_user_in_group("user 15", group_02)) # returns True
print(is_user_in_group("user 03", group_02)) # returns False
print(is_user_in_group("user 16", group_02)) # returns True

print(is_user_in_group("user 11", group_05)) # returns False
print(is_user_in_group("user 09", group_05)) # returns True

print(is_user_in_group("user 05", group_06)) # returns False
print(is_user_in_group("user 14", group_06)) # returns True

# Test case 3 - edge case

try:
    group = Group("")
    group.add_user("")
    print(is_user_in_group("", group))

except AttributeError: print("Invalid arguments")

try:
    group = Group(None)
    group.add_user(None)
    print(is_user_in_group(None, group))
    
except AttributeError: print("Invalid arguments")

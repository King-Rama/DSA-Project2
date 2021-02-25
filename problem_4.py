class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
"""

Define  a look up function

"""

def is_user_in_group(user, group):

    """

    Itarate incomung user through existing users and return true if user match.

    """
    if user in group.get_users():
        return True

    """

   Loop through the existing group to check which exactly group the user belongs.

    """     
    for group in group.get_groups():
        while is_user_in_group(user, group):
            return True
    return False

    """
    Declare variabes to hold users who will be used for Three different Testing

    """
user1 =  "Teacher"
user2 =  ""
user3 =  "sub_child_user"
user4 = None

# Tests
"""
Print Test result for User 1
"""
print(is_user_in_group("%s"%(user1), child))  
# False

"""
Print test result for user 2
"""
print(is_user_in_group("%s"%(user2), sub_child)) 
# False
"""
Print test result for user 3
"""
print(is_user_in_group("%s"%(user3), parent))
# True
"""
Print test result for user 4
"""
print(is_user_in_group("%s"%(user4), parent))
# False

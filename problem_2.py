import os


def find_files(suffix, path):
    my_list = []
    """
    suffix: the end character we are filtering for
    path: the parent directory link to be checked
    finding files in a directory with a possibility of other directory inside
    """
    if os.path.exists(path) and suffix != '':
        for x in os.listdir(path):
            # making the current path an iterable
            dir_path = os.path.join(path, x)
            # using join to make the current element of a list a full path
            if os.path.isfile(dir_path) and x.endswith(suffix):
                # checking if the joined path is a file and ends with suffix we want
                my_list.append(dir_path)
                # if it is append in my_list
            if os.path.isdir(dir_path):
                # if the path is directory recall the function to repeat above steps
                # and append current list
                my_list = my_list + find_files(suffix, dir_path)
        return my_list
    elif suffix == '':
        return 'No suffix provided'
    else:
        return 'Path does not exist'


# tests
print(find_files("c", 'testdir'))
# ['testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c', 'testdir/t1.c']

print("""\n
    end of test 1
    \n
""")
print(find_files("", 'testdir'))
# No suffix provided

print("""\n
    end of test 2
    \n
""")
print(find_files('c', ''))
# Path does not exist
print("""\n
    end of test 3
    \n
""")
import os

def find_files_recursive(suffix, path, index, paths):
    if index >= len(path):
        return None 

    if path[index].endswith(suffix):
        paths.append(os.path.join(os.getcwd(),path[index]))

    elif os.path.isdir(path[index]):
        os.chdir(os.getcwd() + '/' + path[index])

        find_files_recursive(suffix, os.listdir(), 0, paths)
        
        os.chdir('..')
        
    find_files_recursive(suffix, path, index + 1, paths)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    if suffix == '' or suffix is None:
        return "Invalid arguments"

    paths = []

    find_files_recursive(suffix, path, 0, paths)

    return paths

os.chdir(os.path.join(os.path.dirname(__file__), 'testdir'))

# Test case 1

print(find_files('.c', os.listdir()), '\n') # returns all file paths ending with '.c' in the testdir folder

# Test case 2

print(find_files('.h', os.listdir()), '\n') # returns all file paths ending with '.h' in the testdir folder

# Test case 3

print(find_files('.gitkeep', os.listdir()), '\n') # returns all file paths ending with '.gitkeep' in the testdir folder

# Test case 4 - edge cases

print(find_files('', os.listdir()), '\n') # returns a message of invalid arguments
print(find_files(None, os.listdir()), '\n') # returns a message of invalid arguments

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
    paths = []

    find_files_recursive(suffix, path, 0, paths)

    return paths

os.chdir(os.path.join(os.path.dirname(__file__), 'testdir'))

print(find_files('.c', os.listdir())) # returns all file paths ending with '.c' in the testdir folder

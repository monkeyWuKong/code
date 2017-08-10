import os


def check_file(filename):
    if not os.path.exists(filename):
        error = 'File(%s) does not exist.' % filename
        return False, error
    
    if not os.path.isfile(filename):
        error = '%s is not a file.' % filename
        return False, error
    
    return True, None


def get_file_content(filename):
    state, info = check_file(filename)
    if False == state:
        return False, info
    
    try:
        with open(filename, 'r') as fp:
            content = fp.read()
    except IOError as e:
        return False, str(e)
    
    return True, content


def delete_specified_line(filename, keywords):
    """
    state, file_content = get_file_content(filename)
    if False == state:
        return False, file_content
    """
    state, info = check_file(filename)
    if False == state:
        return False, info
    
    try:
        with open(filename, 'r') as fp:
            lines = fp.readlines()
    except IOError as e:
        return Fasle, str(e)
    
    try:
        with open(filename, 'w') as fp:
            for line in lines:
                if keywords in line:
                    continue
                fp.write(line)
    except IOError as e:
        return False, str(e)
    
    return True, None


def append_new_line(filename, line):
    state, content = get_file_content(filename)
    if False == state:
        return False, content
    
    if content[-1] != '\n':
        content = content + '\n'
    
    if line[-1] != '\n':
        line = line + '\n'
    
    try:
        with open(filename, 'w') as fp:
            fp.write(content)
            fp.write(line)
    except IOError as e:
        return False, str(e)
    
    return True, None


        

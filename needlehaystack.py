import io

def count(needle, haystack):
    """
    :param needle: (String) The text to search for
    :param haystack: (StringIO) An in-memory stream for text I/O
    :returns: (int) The number of lines that contain the needle
    """
    found_lines = []
    for line in stream:
        if needle in line:
            found_lines.append(line.strip())
    return len(found_lines)

if __name__ == "__main__":
    stream = io.StringIO("Hello, there!\nHow are you today?\nYes, you over there.")
    print(count('there', stream))
    stream.close()



    import io

def count(needle, haystack):
    """
    :param needle: (String) The text to search for
    :param haystack: (StringIO) An in-memory stream for text I/O
    :returns: (int) The number of lines that contain the needle
    """
    counter=0
    for line in haystack:
        if needle in line:
            counter=counter+1
    return counter

stream = io.StringIO("Hello, there!\nHow are you today?\nYes, you over there.")
print(count('there', stream))
stream.close()
import textwrap

def wrap(string, max_width):
    currindex= 0
    res = ""
    while currindex < len(string):
        if currindex+ max_width< len(string):
            res += (string[currindex: currindex+ max_width] + "\n")
        else:
            res += (string[currindex:] + "\n")
        currindex += max_width    
    return res
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
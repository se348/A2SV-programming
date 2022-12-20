def swap_case(s):
    ans=""
    for charac in s:
        if charac.isalpha():
            if ord(charac)>=97:
                ans+= chr(ord(charac) -32)
            else:
                ans+= chr(ord(charac) +32)
        else:
            ans+= charac        
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
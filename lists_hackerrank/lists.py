if __name__ == '__main__':
    N = int(input())
    llist= []
    
    for _ in range(N):
        raw = input().split()
        checked = raw[0]
        
        if checked == "insert":
            llist.insert(int(raw[1]), int(raw[2]))
        
        elif checked == "print":
            print(llist)
        
        elif checked == "remove":
            llist.remove(int(raw[1]))
        
        elif checked == "append":
            llist.append(int(raw[1]))
        
        elif checked == "sort":
            llist.sort()
        
        elif checked == "pop":
            llist.pop()
            
        elif checked=="reverse":
            llist.reverse()
            
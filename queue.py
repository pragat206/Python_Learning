que = []
def enq():
    ele = input('enter ele: ')
    que.append(ele)
    print(que)
    
def deq():
    if len(que) == 0:
        print('its empty')
    else:
        e = que.pop(0)
        print('removed',e)
def disp():
    print(que)

while True:
    print('1 for enque 2 for deque 3 for disp 4 to qut')
    choice = int(input())
    if choice == 1:
        enq()
    elif choice == 2:
        deq()
    elif choice == 3:
        disp()
    elif choice == 4:
        break
    else:
        print('choose correct option')
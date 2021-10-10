'''
Polycarp is a big lover of killing time in social networks.
A page with a chatlist in his favourite network is made so that when a message is sent to some friend, 
his friend's chat rises to the very top of the page.
The relative order of the other chats doesn't change.
If there was no chat with this friend before, then a new chat is simply inserted to the top of the list.

Assuming that the chat list is initially empty,
given the sequence of Polycaprus' messages make a list of chats after all of his messages are processed.
Assume that no friend wrote any message to Polycarpus.

Input
The first line contains integer n (1 ≤ n ≤ 200 000) — the number of Polycarpus' messages. 
Next n lines enlist the message recipients in the order in which the messages were sent.
The name of each participant is a non-empty sequence of lowercase English letters of length at most 10.

Output
Print all the recipients to who Polycarp talked to in the order of chats with them, from top to bottom.

Examples

input:
    4
    alex
    ivan
    roman
    ivan

output:
    ivan
    roman
    alex
 

#inputs
x = int(input())
my_list=[]

# to add the inputs in a list
for i in range(x):
    y = str(input())
    my_list.append(y)

# to reverse the list 
my_list.reverse()

# make another list with out duplications 
res = []
for i in my_list:
    if i not in res:
        res.append(i)

#print values witheoyt list
for name in res:    
    print(name)  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # another solution but smaller (not formal code) # # # # # # # #    

#inputs
x = int(input())
my_list=[]

# to add the inputs in a list
for i in range(x):
    y = str(input())
    my_list.append(y)

# to reverse the list
my_list.reverse()

# make another list with out duplications ( in one line )
res = []
[res.append(x) for x in my_list if x not in res]

#print values witheoyt list
for name in res:    
    print(name) 

    

'''

x = int(input())
 
setter = set()
output = list()
for i in range(x):
    y = str(input())
    output.append(y)
 
 
for i in range(x, 0 , -1):
    val = output[i- 1]
    if val not in setter:
        print(val)
        setter.add(val)
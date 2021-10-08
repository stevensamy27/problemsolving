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
'''

# x = int(input())
# my_list=[]
# for i in range(x):
#     y = str(input())

#     if y in my_list:
#         my_list.insert(0,y) 

#     my_list.append(y)


# my_new_list = list(dict.fromkeys(my_list))

# # print(my_new_list)
# # print(my_list)        
# for name in my_new_list:    
#     print(name)   


x = int(input())
my_list=[]
for i in range(x):
    y = str(input())
    my_list.append(y)
my_list.reverse()

res = []
[res.append(x) for x in my_list if x not in res]

for name in res:    
    print(name)  



# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# print ("The original list is : " +  str(test_list))
  

# res = []
# for i in test_list:
#     if i not in res:
#         res.append(i)
  
# # printing list after removal 
# print ("The list after removing duplicates : " + str(res))
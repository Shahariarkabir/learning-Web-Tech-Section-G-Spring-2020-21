table = {'clean': 'move', 'dirty':'suck'}
def lookup(percept):
    for i in table :
        if i == percept[1]:
             return table[i]
def move (location):
    if location == 'A':
        return 'Right'
    elif location =='B':
        return 'Left'


 
def table_agent(percept):
    action=  lookup (percept)
    if action == 'move':
        action = move(percept[0])
    print (action)
 
    Choice ='yes'
    while Choice != 'No':
 
        room_status = input ("Enter Status(Clean/Dirty)")
        room_name = input ("Enter Room Name(A/B)")
        percept =[room_name,room_status]
        table_agent(percept)
        c =input("Continue!!!?? (Yes/No)")
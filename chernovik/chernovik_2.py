import json
d = []
with open('dz.json','r') as file:
    content = file.read()
    dz = json.loads(content)
    average_height = 0
    for d_col in dz:
        average_height += d_col['height'] / 4
    print('Average height: ',average_height)
    
    for d_col in dz:
        if len(d_col['languages']) >= 3:
            print(d_col['name'],'knows', len(d_col['languages']),'languages')

    
            
    
        


    
    
        
        
            
        

    
    

    
        
            
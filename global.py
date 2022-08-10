gx = "global"

def function():
    global gx
    ly = "local"
    gx = gx * 3
    print(ly)
    print(gx)
function()    
   

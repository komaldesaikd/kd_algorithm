def solution(inputvalue):
    import json  
    dict_op={}    
    dict_op_LRUL={}

    for item,value in inputvalue.items():#To check each rectangle minimun and maximum X & Y Coordinates
        minx = 100000000000
        miny = 100000000000
        maxx = -100000000000
        maxy = -100000000000
        for x,y in value:        
            if(x<minx):
                minx=x
            if(y<miny):
                miny=y
            if(x>maxx): 
                maxx=x
            if(y>maxy):
                maxy=y            
        dict_op[item]={"min":(minx,miny),"max":(maxx,maxy)}
    for key, value in dict_op.items():
        for subkey, subvalue in value.items():
            if(key=='A'):
                if(subkey=='min'):            
                    Asubvaluex = subvalue[0]
                    Asubvaluey = subvalue[1]
            elif(key=='B'):
                if(subkey=='min'):            
                    Bsubvaluex = subvalue[0]
                    Bsubvaluey = subvalue[1]
    if(min(Asubvaluex,Bsubvaluex)==Asubvaluex):# To check left rectangle and lower rectangle on the plane
        LR = "A"
        RR = "B"
    else:
        LR = "B"
        RR = "A"
    if(min(Asubvaluey,Bsubvaluey)==Asubvaluey):
        LLR = "A"
        UR = "B"
    else:
        LLR = "B"
        UR  = "A"   
    for key,value in dict_op.items():
        if(key==LR):
            for subkey,subvalue in value.items():
                if(subkey=='max'):
                    maxx = subvalue[0]                    
        if(key==RR):
            for subkey,subvalue in value.items():
                if(subkey=='min'):
                    minx = subvalue[0]                    #
        if(key==LLR):
            for subkey,subvalue in value.items():
                if(subkey=='max'):
                    maxy = subvalue[1]                    
        if(key==UR):
            for subkey,subvalue in value.items():
                if(subkey=='min'):
                    miny = subvalue[1]                              
        diffx = (maxx-minx)#Find difference between X- cordinates of left maximum  & right minimum rectangle
        diffy = (maxy-miny)#Find difference between Y- cordinates of lower maximum  & upper minimum rectangle 
        if(diffx<0 or diffy<0):
            return (False)#if rectangles do not overlaps then return False
        else:
            return (True) #if rectangles overlaps then return True
    

    

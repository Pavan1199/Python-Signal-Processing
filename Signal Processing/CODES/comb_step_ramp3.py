def comb_step_ramp3(t,x):
    
    for i in t:
        if i <=-4:
            k=2
            step(-4,i,k,x)
        elif (i>-4) & (i<=-2) :
            ramp(-2,i,-2,-1,x)
        elif (i>-2) & (i<-1) :
            step(-1,i,0,x)
        elif (i>=-1) & (i<=1) :
            ramp(1,i,1,1,x)
        elif (i>1) & (i<=3) :
            step(3,i,2,x)
        elif (i>3) & (i<=4) :
            step(4,i,-2,x)
        elif (i>=4) & (i<=6) :
            ramp(6,i,-6,1,x)
        else:
            x.append(0)

def step(j,i,k,x):
    if j >=i:
        x.append(k)
    else:
        x.append(0)
    
def ramp(j,i,k,l,x):
    if j >=i:
        x.append(l*i+k)

    else:
        x.append(0)



def stat_dyn_fun(a,x):
    m=0
    for i in range(len(x)):
        if (x[i] == a[i]):
            m=1
        else:
            m=0
            print("the function is dynamic")
            break
    if(m==1):
        print("the given function is static")


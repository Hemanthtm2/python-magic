def myfuncs(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[1],kwargs['food']))

myfuncs(10,20,30,fruit='orange',food='Eggs',animal='Egg')

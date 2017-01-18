from rx import Observable

def handler(event, context):
    #
    print "Last: %s" % event['last_name']
    print "First: %s" % event['first_name']

    #
    xs = Observable.from_([1, 2, 3, 4, 5, 6])
    ys = xs.to_blocking()
    zs = (x*x for x in ys if x > 3)
    for x in zs:
        print x
    return 'foobar'

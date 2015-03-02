import json


def search(args):
    x = args['x']
    y = args['y']
    assert isinstance(x, basestring)
    assert isinstance(y, int)
    print json.dumps('x = {}'.format(x))
    print '---'
    print json.dumps('y = {}'.format(y))


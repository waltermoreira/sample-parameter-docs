import json
from collections import Sequence


def search(args):
    x = args['x']
    y = args['y']
    z = args['z']
    w = args['w']
    assert isinstance(x, basestring)
    assert isinstance(y, int)
    assert isinstance(z, Sequence)
    assert w in ('Foo', 'Bar')
    print json.dumps(args)
    print '---'
    print json.dumps('x = {}'.format(x))
    print '---'
    print json.dumps('y = {}'.format(y))
    print '---'
    print json.dumps('z = {}'.format(z))
    print '---'
    print json.dumps('w = {}'.format(w))


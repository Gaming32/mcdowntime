import sys
sys.path.insert(1, 'Minecraft-Protocol')

from mcproto.server import Connection, Handshake, Server


def log(event, *args):
    print(event)
    for arg in args:
        print('  ', repr(arg))


def info(conn: Connection, handshake: Handshake):
    return {
        'version': {
            'name': 'Downtime Manager',
            'protocol': handshake.protocol_version
        },
        'players': {
            'max': 1,
            'online': 0,
            'sample': []
        },
        'description': {
            'text': 'This server is down for maintainence'
        }
    }


myserv = Server()
# myserv.on('all', log)
myserv.on('status', info)
myserv.on('disallowed', log)


myserv.listen()

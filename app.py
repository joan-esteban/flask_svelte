import logging
from types import SimpleNamespace




def split_url(url: str, default_port: int) -> {}:
    a = url.split(':')
    if (len(a) == 0):
        return (url,  default_port)
    elif (len(a) == 2):
        return ( a[0],  int(a[1]))
    else:
        raise ValueError(url)

def parse_arguments() -> SimpleNamespace:
    import argparse
    parser = argparse.ArgumentParser(description='''My app''')
    parser.add_argument("-b", "--bind", action='store', default="0.0.0.0:8080",
                        help='binding address')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose')

    args = parser.parse_args()
    ip, port =  split_url(args.bind, default_port=8080)
    return SimpleNamespace( 
        bind_ip= ip, 
        bind_port = port, 
        verbose = args.verbose
    )


if __name__ == '__main__':
    args = parse_arguments()
    if args.verbose: logging.basicConfig(level=logging.DEBUG)
    from backend import app, socketio
    socketio.run(app, host=args.bind_ip, port=args.bind_port, use_reloader=True, debug=True)
"""
This module creates a server that repeatedly echoes messages
received from a client. It reads the incoming data from the client
in 16 byte chunks and immediately sends the chunk of data back.
"""

import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    """
    Creates a server socket that repeatedly echoes
    messages received from a client.
    """
    # Create a server socket
    address = ('127.0.0.1', 50001)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

    # TODO: You may find that if you repeatedly run the server script it fails,
    #       claiming that the port is already used.  You can set an option on
    #       your socket that will fix this problem. We DID NOT talk about this
    #       in class. Find the correct option by reading the very end of the
    #       socket library documentation:
    #       http://docs.python.org/3/library/socket.html#example

    # Log that a server is being made
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # Bind socket to address and listen
    sock.bind(address)
    sock.listen(1)
    try:
        # Outer loop -> Handles incoming client connections -> Creates new sockets
        while True:
            print('waiting for a connection', file=log_buffer)

            # New socket 'conn' with client address 'addr'
            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # Inner loop -> Handles sending/receiving data from each client
                while True:
                    # Receive the data from the client
                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf-8')))

                    # Send the data back to the client
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf-8')))
                    if len(data) < 16:
                        break
            except Exception as exc:
                traceback.print_exc()
                sys.exit(1)
            finally:
                conn.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )
    except KeyboardInterrupt:
        conn.close()
        sock.close()
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)

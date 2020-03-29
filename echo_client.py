"""
This module creates a client that sends a message to a server.
It reads the return data from the server in 16 byte chunks
and prints the return data to a log file.
"""

import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    """
    Creates a client socket that repeatedly sends data to a
    server and reads the data returning from the server.
    """
    # Instantiate/connect to a TCP socket with IPv4 Addressing
    server_address = ('127.0.0.1', 50001)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)

    # Variable to append message chunks received back from the server to
    received_message = ''

    # Try/finally block exists to allow socket closure when finished
    try:
        # Sends message to the server
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf-8'))

        # Accumulates chunks received back from the server
        while True:
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf-8')), file=log_buffer)
            received_message += chunk.decode('utf-8')
            if len(chunk) < 16:
                break
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print('closing socket', file=log_buffer)
        sock.close()
    return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)

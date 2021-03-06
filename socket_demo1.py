#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : linsheng
import socket

def handle_request(client):

    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("uff-8"))
    client.send("<h1 style = 'color:red'>Hello ,Welcome</h1>".encode("utf-8"))


def main():

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("localhost",8001))
    sock.listen(5)

    while True:
        connection , address =sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':

    main()

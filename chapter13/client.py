# coding: utf-8
# client.py

import json
import time
import struct
import socket


def rpc(sock, in_, params):
    request = json.dumps({"in": in_, "params": params})  # 请求消息体
    length_prefix = struct.pack("I", len(request))  # 请求长度前缀
    sock.sendall(length_prefix)
    sock.sendall(request)
    length_prefix = sock.recv(4)  # 响应长度前缀
    length, = struct.unpack("I", length_prefix)
    body = sock.recv(length)  # 响应消息体
    response = json.loads(body)
    return response["out"], response["result"]  # 返回响应类型和结果

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    for i in range(10):  # 连续发送10个rpc请求
        out, result = rpc(s, "ping", "ireader %d" % i)
        print out, result
        time.sleep(1)  # 休眠1s，便于观察
    s.close()  # 关闭连接

import sys
sys.path.append("gen-py")

from thrift.transport import TSocket, TTransport
from thrift.protocol import TCompactProtocol

from pi.PiService import Client
from pi.ttypes import PiRequest, IllegalArgument

if __name__ == '__main__':
    sock = TSocket.TSocket("127.0.0.1", 8888)
    transport = TTransport.TBufferedTransport(sock)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = Client(protocol)

    transport.open()
    for i in range(10):
        try:
            res = client.calc(PiRequest(n=i))
            print "pi(%d) =" % i, res.value
        except IllegalArgument as ia:
            print "pi(%d)" % i, ia.message
    transport.close()

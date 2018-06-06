import grpc

import pi_pb2
import pi_pb2_grpc

from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel

chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.gzip),
            ('grpc.grpc.default_compression_level', CompressionLevel.high)]


def main():
    channel = grpc.insecure_channel('localhost:8080', chan_ops)
    client = pi_pb2_grpc.PiCalculatorStub(channel)
    for i in range(10):
        try:
            res = client.Calc(pi_pb2.PiRequest(n=i))
            print "pi(%d) =" % i, res.value
        except grpc.RpcError as e:
            print e.code(), e.details()


if __name__ == '__main__':
    main()

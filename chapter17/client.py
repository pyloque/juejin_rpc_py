import grpc

import pi_pb2
import pi_pb2_grpc


def main():
    channel = grpc.insecure_channel('localhost:8080')
    client = pi_pb2_grpc.PiCalculatorStub(channel)
    for i in range(1, 1000):
        client.Calc(pi_pb2.PiRequest(n=i)).value


if __name__ == '__main__':
    main()

import grpc

import pi_pb2
import pi_pb2_grpc


def generate_request():
    for i in range(1, 2):
        yield pi_pb2.PiRequest(n=i)


def main():
    channel = grpc.insecure_channel('localhost:8080')
    client = pi_pb2_grpc.PiCalculatorStub(channel)
    response_iterator = client.Calc(generate_request())
    for response in response_iterator:
        print "pi(%d) =" % response.n, response.value


if __name__ == '__main__':
    main()

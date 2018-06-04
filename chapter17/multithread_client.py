import grpc

import pi_pb2
import pi_pb2_grpc

from concurrent import futures


def pi(client, k):
    return client.Calc(pi_pb2.PiRequest(n=k)).value

def main():
    channel = grpc.insecure_channel('localhost:8080')
    client = pi_pb2_grpc.PiCalculatorStub(channel)
    pool = futures.ThreadPoolExecutor(max_workers=10)
    results = []
    for i in range(1, 1000):
        results.append((i, pool.submit(pi, client, i)))
    pool.shutdown()

if __name__ == '__main__':
    main()

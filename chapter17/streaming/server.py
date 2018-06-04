import math
import grpc
import time
import random
from concurrent import futures

import pi_pb2
import pi_pb2_grpc


class PiCalculatorServicer(pi_pb2_grpc.PiCalculatorServicer):

    def Calc(self, request_iterator, ctx):
        for request in request_iterator:
            if random.randint(0, 1) == 1:
                continue
            s = 0.0
            for i in range(request.n):
                s += 1.0/(2*i+1)/(2*i+1)
            yield pi_pb2.PiResponse(n=i, value=math.sqrt(8*s))


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = PiCalculatorServicer()
    pi_pb2_grpc.add_PiCalculatorServicer_to_server(servicer, server)
    server.add_insecure_port('localhost:8080')
    server.start()
    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()

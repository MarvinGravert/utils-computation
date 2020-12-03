from decouple import config
from config.api_types import Example

GRPC_PORT = config("GRPC_PORT", cast=int, default=50051)
RUNTIME_HOST = config("RUNTIME_HOST", cast=str, default="[::]")


TEST = config("TEST", cast=int, default=10)
DAY = config("DAY", cast=Example, default=Example.DAY_7)

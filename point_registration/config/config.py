from decouple import config
from config.api_types import Example

GRPC_PORT = config("GRPC_PORT", cast=int, default=50051)
RUNTIME_HOST = config("RUNTIME_HOST", cast=str, default="[::]")

"""
OPENCV AFFINE TRANSFORMATION
"""
RANSAC_THRESHOLD = config("RANSAC_THRESHOLD", cast=float, default=3)
RANSAC_CONFIDENCE = config("RANSAC_CONFIDENCE", cast=float, default=0.99)


TEST = config("TEST", cast=int, default=10)
DAY = config("DAY", cast=Example, default=Example.DAY_7)

from PIL import Image
from minio import Minio
from matplotlib import pyplot as plt
import subprocess

access_key = "minioadmin"
secret_key = "minioadmin"

client = Minio("localhost:9000",
      access_key=access_key,
      secret_key=secret_key, secure=False
      )

my_buckets = []

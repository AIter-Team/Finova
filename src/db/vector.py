from qdrant_client import QdrantClient, models

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="memory",
    vectors_config=models.VectorParams(size=4, distance=models.Distance.COSINE),
)

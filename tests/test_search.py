from app.search import Searcher


class CountingEmbedder:
    def __init__(self) -> None:
        self.calls = 0

    def embed(self, texts):
        self.calls += 1
        yield [1.0, 2.0, 3.0]


def test_repeated_query_embedding_is_cached():
    searcher = Searcher()
    embedder = CountingEmbedder()
    searcher.embedder = embedder

    first = searcher._embed_query("same query")
    second = searcher._embed_query("same query")

    assert first == second == (1.0, 2.0, 3.0)
    assert embedder.calls == 1


def test_query_embedding_cache_is_keyed_by_query():
    searcher = Searcher()
    embedder = CountingEmbedder()
    searcher.embedder = embedder

    searcher._embed_query("first query")
    searcher._embed_query("second query")
    assert embedder.calls == 2


def test_semantic_search_passes_a_list_vector_to_qdrant():
    class RecordingClient:
        def __init__(self) -> None:
            self.query = None

        def query_points(self, *, collection_name, query, limit):
            self.query = query
            return type("Result", (), {"points": []})()

    searcher = Searcher()
    searcher.embedder = CountingEmbedder()
    client = RecordingClient()
    searcher.client = client

    assert searcher._search_semantic("query", top_k=10) == []

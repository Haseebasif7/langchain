"""Test octoai embeddings."""

from langchain.embeddings.octoai_embeddings import (
    OctoAIEmbeddings,
)


def test_octoai_embedding_documents() -> None:
    """Test octoai embeddings."""
    documents = ["foo bar"]
    embedding = OctoAIEmbeddings()
    output = embedding.embed_documents(documents)
    assert len(output) == 1
    assert len(output[0]) == 768


def test_octoai_embedding_query() -> None:
    """Test octoai embeddings."""
    document = "foo bar"
    embedding = OctoAIEmbeddings()
    output = embedding.embed_query(document)
    assert len(output) == 1
    assert len(output[0]) == 768
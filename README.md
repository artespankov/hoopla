### RAG search engine
Full-text search amplified with real-time results with RAG tools

### Run
uv run cli/keyword_search_cli.py search "your search query"


### Stage 1 - Text Preprocessing
1. Make the text **case-insensitive** "The Man and the Ordinarily Obscure RAG." -> "the man and the ordinarily obscure rag."
2. Drop **punctuation** "the man and the ordinarily obscure rag"
3. Text **tokenization** ["the", "man", "and", "the", "ordinarily", "obscure", "rag"]
4. Remove **stopwords** ["man", "ordinarily", "obscure", "rag"]
5. Words **stemming** ["man", "ordinary", "obscure", "rag"]

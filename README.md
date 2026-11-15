# LangChain Models

A hands-on collection of experiments and implementations exploring **Large Language Models (LLMs), Chat Models, Embedding Models, and semantic search** using the LangChain ecosystem.

This repository demonstrates how to interact with different LLM providers, work with locally hosted models, generate text embeddings, and measure document similarity.

## 📌 Project Overview

The repository explores the following areas:

- **Chat Models:** Integrating LangChain with different AI model providers, including OpenAI, Anthropic, Google, Hugging Face, and Ollama.
- **LLMs:** Understanding and experimenting with Large Language Models through LangChain.
- **Embedding Models:** Converting text into numerical vector representations using local and API-based embedding models.
- **Document Similarity:** Comparing documents using vector embeddings and cosine similarity.
- **Semantic Search:** Retrieving relevant documents based on the meaning of a user's query rather than exact keyword matching.
- **Local LLMs:** Running language models locally using Ollama.
- **Hugging Face Integration:** Exploring hosted API and local model integrations.

## 📂 Repository Structure

```text
Langchain_Models/
│
├── ChatModels/
│   ├── chatmodel_anthropic.py
│   ├── chatmodel_google.py
│   ├── chatmodel_openai.py
│   ├── hf_api
│   ├── hf_local_api
│   └── ollama.py
│
├── Embedded_models/
│   ├── document_similarity
│   ├── embedded_local_model
│   ├── openai_docs
│   └── openai_query
│
├── LLMs/
│   └── llm_demo.py
│
└── README.md
```

*Note: This structure reflects the files and folders identified so far. Additional repository files may be added as the project evolves.*

## 1. Chat Models

This section explores how to connect LangChain with different chat model providers.

| File | Description |
|---|---|
| `chatmodel_anthropic.py` | Integration with Anthropic chat models |
| `chatmodel_google.py` | Integration with Google chat models |
| `chatmodel_openai.py` | Integration with OpenAI chat models |
| `hf_api` | Hugging Face API-based model integration |
| `hf_local_api` | Hugging Face local model integration |
| `ollama.py` | Running chat models locally using Ollama |

**Key concepts:**
- Chat model initialization
- Sending prompts to language models
- Receiving and processing model responses
- Working with different LLM providers
- Local versus hosted model inference

## 2. Embedding Models

Embedding models convert text into numerical vectors that capture semantic information.

This section explores local and API-based embeddings and their applications.

| File | Description |
|---|---|
| `document_similarity` | Exploring similarity between documents using embeddings |
| `embedded_local_model` | Generating embeddings using locally available Hugging Face models |
| `openai_docs` | Exploring document embeddings using OpenAI |
| `openai_query` | Working with embeddings for query-based retrieval |

### Local Embeddings with Hugging Face

The repository includes experimentation with:

**Model:** `sentence-transformers/all-MiniLM-L6-v2`

This model generates 384-dimensional embeddings and can be used for semantic similarity and retrieval tasks.

### Document Similarity

Document similarity involves comparing vector representations of text to identify semantically related content.

A typical workflow:

1. Convert documents into embeddings.
2. Convert the user query into an embedding.
3. Calculate cosine similarity between the vectors.
4. Identify the document with the highest similarity score.

**Cosine similarity:**

\[
\text{Similarity}(A,B)=\frac{A\cdot B}{\|A\|\|B\|}
\]

A higher cosine similarity generally indicates greater directional similarity between two embedding vectors.

## 3. Large Language Models (LLMs)

The `LLMs` directory contains experiments with Large Language Models.

| File | Description |
|---|---|
| `llm_demo.py` | Demonstration of LLM functionality using LangChain |

This section focuses on understanding how language models process prompts and generate natural-language responses.

## 4. Technologies and Tools

- Python
- LangChain
- LangChain Community
- LangChain Hugging Face
- LangChain Ollama
- OpenAI
- Anthropic
- Google AI
- Hugging Face
- Ollama
- Sentence Transformers
- Scikit-learn
- NumPy
- Streamlit

## 5. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- A code editor such as Visual Studio Code

For local model execution, install [Ollama](https://ollama.com/).

### Clone the repository

```bash
git clone https://github.com/keshkong/Langchain_Models.git
```

```bash
cd Langchain_Models
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Install dependencies

Install the packages required by the scripts you want to run:

```bash
pip install langchain langchain-openai langchain-anthropic langchain-google-genai langchain-huggingface langchain-ollama sentence-transformers scikit-learn numpy streamlit python-dotenv
```

Some integrations require provider-specific API keys. Configure them through environment variables rather than hardcoding secrets in Python files.

## 6. Running Local Models with Ollama

Install Ollama and download a model:

```bash
ollama pull llama3.2:1b
```

Start the model:

```bash
ollama run llama3.2:1b
```

LangChain can connect to the local Ollama model through `ChatOllama`.

## 7. Learning Objectives

Through this repository, the key learning objectives include:

- Understanding the LangChain ecosystem.
- Exploring different chat model providers.
- Working with hosted and locally running LLMs.
- Understanding text embeddings and vector representations.
- Implementing document similarity using cosine similarity.
- Exploring semantic search and query embeddings.
- Building foundations for retrieval-augmented generation (RAG) applications.

## 8. Future Improvements

- Implement end-to-end Retrieval-Augmented Generation (RAG).
- Explore vector databases such as FAISS and Chroma.
- Build document question-answering applications.
- Experiment with LangChain chains and LangGraph workflows.
- Add interactive Streamlit applications.
- Compare embedding models based on retrieval quality.

## Author

**Keshkong**

GitHub: [@keshkong](https://github.com/keshkong)

---

*This repository is a practical learning journey through LangChain, LLM integrations, embeddings, and semantic search.*

# 🍽️ Food Search & RAG Chatbot System

A comprehensive food recommendation system demonstrating similarity search, metadata filtering, and retrieval-augmented generation (RAG) with AI-powered responses.

## Features

### 1. **Interactive CLI Search** (`interactive_search.py`)
Real-time food search with semantic understanding
- Natural language queries
- Instant recommendations with match scores
- Contextual suggestions for related searches

### 2. **Advanced Search** (`advanced_search.py`)
Smart filtering with multiple options
- Basic similarity search
- Cuisine-filtered search
- Calorie-restricted search
- Combined multi-filter search
- Built-in demonstrations

### 3. **RAG Chatbot** (coming soon)
AI-powered conversational recommendations
- Combines vector search with LLM responses
- Contextual food recommendations
- Natural language explanations

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Running the Systems

```bash
# Interactive Search
python interactive_search.py

# Advanced Search
python advanced_search.py

# RAG Chatbot (requires IBM WatsonX credentials)
python enhanced_rag_chatbot.py
```

## Architecture

```
Food Dataset (JSON)
    ↓
Load & Normalize Data
    ↓
Generate Embeddings (Sentence-Transformers)
    ↓
Store in Vector Database (Chroma DB)
    ↓
Similarity Search / Filtered Search / RAG
    ↓
Display Results / AI Responses
```

## Dataset

- **Format**: JSON
- **Items**: 15+ food items
- **Fields**: name, description, ingredients, calories, cuisine, cooking method, health benefits, taste profile

## Technology Stack

- **Vector Database**: Chroma DB
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **LLM** (optional): IBM Granite via WatsonX
- **Language**: Python 3.8+

## Shared Functions

The `shared_functions.py` module provides reusable utilities:

```python
load_food_data()                    # Load and normalize food data
create_similarity_search_collection() # Create Chroma collection
populate_similarity_collection()    # Add foods + embeddings
perform_similarity_search()         # Find similar foods
perform_filtered_similarity_search() # Search with filters
```

## Example Usage

### Interactive Search
```
🔍 Search for food: chocolate dessert
✅ Found 5 recommendations:
1. 🍽️  Chocolate Cake
   📊 Match Score: 95.2%
   🏷️  Cuisine: American
   🔥 Calories: 380 per serving
   📝 Rich chocolate cake with vanilla frosting...
```

### Advanced Search
```
Option 2: Cuisine-filtered search
Query: "creamy pasta"
Cuisine: Italian
→ Returns only Italian dishes matching "creamy pasta"
```

## Learning Outcomes

- Understanding vector databases and semantic search
- Metadata filtering and complex queries
- RAG architecture and LLM integration
- Building conversational AI systems
- CLI interface design and user interaction

## Notes

- All systems run locally (no cloud dependencies for basic usage)
- Embeddings are cached after first generation
- Vector similarity scores range from 0 to 1 (higher = more similar)
- Perfect for learning similarity search, RAG, and vector databases

## Next Steps

1. Run `python interactive_search.py` to test semantic search
2. Try `python advanced_search.py` to explore filtering
3. (Coming soon) Set up IBM WatsonX credentials for RAG chatbot

---

**Project**: Food Search & RAG Chatbot System  
**Stack**: Python 3.8+, Chroma DB, Sentence-Transformers  
**Status**: Learning/Demonstration
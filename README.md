# 🍽️ Food Search & RAG Chatbot System

A comprehensive learning project demonstrating **vector embeddings**, **semantic similarity search**, **metadata filtering**, and **retrieval-augmented generation (RAG)** using modern AI/ML techniques.

## What This Project Teaches

### Core Concepts
- **Vector Embeddings**: Convert text (food descriptions) into numerical representations using sentence-transformers
- **Semantic Similarity**: Find foods that are conceptually similar, even with different wording
- **Vector Databases**: Store and query embeddings efficiently using Chroma DB
- **Metadata Filtering**: Combine similarity search with exact constraints (cuisine, calories)
- **RAG Architecture**: Combine retrieval systems with LLMs for conversational AI

### Real-World Applications
- Food recommendation systems
- Dietary constraint filtering
- Restaurant discovery
- Nutritional guidance chatbots
- E-commerce product search

## Features

### 🎯 Interactive CLI Search (`interactive_search.py`)
Natural language food search with instant semantic understanding
```
🔍 Search for food: chocolate dessert
✅ Found 5 recommendations:

1. 🍽️ Chocolate Lava Cake
   📊 Match Score: 62.6%
   🏷️ Cuisine: International
   🔥 Calories: 400 per serving
   📝 A decadent dessert with a gooey chocolate center...
```

**Features:**
- Real-time natural language queries
- Similarity scores (0-100%)
- Full food metadata (cuisine, calories, description)
- Related search suggestions
- Simple command interface (`help`, `quit`)

### 🔬 Advanced Search (`advanced_search.py`)
Powerful menu-driven system with filtering options
```
🔧 ADVANCED SEARCH OPTIONS
1. Basic similarity search
2. Cuisine-filtered search
3. Calorie-filtered search
4. Combined filters search
5. Demonstration mode
6. Help
7. Exit
```

**Filtering Options:**
- Cuisine types: Italian, Thai, Mexican, Indian, Japanese, French, Mediterranean, American, Asian, Dessert
- Calorie constraints: Search foods under a maximum calorie limit
- Combined filters: Apply multiple constraints simultaneously
- Demo mode: Three pre-built example searches

### 🤖 RAG Chatbot (Coming Soon)
Will combine vector search with IBM Granite LLM for conversational recommendations:
```
User: "I'm looking for something healthy and Italian"
Bot: "Based on your request, I'd recommend Minestrone Soup 
(180 cal, veggie-based) or Grilled Fish with Vegetables 
(250 cal, light and nutritious). Both are authentic Italian 
dishes that fit your dietary preferences..."
```

## How It Works

### Architecture Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     USER QUERY                              │
│            "chocolate dessert under 400 cal"                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            CONVERT TO EMBEDDING (Vector)                    │
│      Using: sentence-transformers (all-MiniLM-L6-v2)       │
│      Output: 384-dimensional numerical vector              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         SEARCH VECTOR DATABASE (Chroma DB)                  │
│   Find foods with similar embedding vectors (cosine         │
│   distance). Apply metadata filters (cuisine, calories).    │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            RETRIEVE TOP MATCHES (5 results)                 │
│  Ranked by similarity score + metadata constraints          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│     FORMAT & DISPLAY RESULTS                                │
│  Show: Name, Match%, Cuisine, Calories, Description        │
└─────────────────────────────────────────────────────────────┘
```

### Key Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Embeddings** | Sentence-Transformers (all-MiniLM-L6-v2) | Convert text to 384-dim vectors |
| **Vector DB** | Chroma DB | Store & query food embeddings |
| **Similarity** | Cosine Distance | Measure semantic similarity |
| **Metadata** | JSON documents | Store cuisine, calories, etc. |
| **LLM** (future) | IBM Granite via WatsonX | Generate conversational responses |

## Installation & Setup

### Requirements
- Python 3.8+
- pip (Python package manager)

### Step 1: Navigate to Project
```bash
cd "C:\Ai Projects\food-search-rag-chatbot"
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- **chromadb** - Vector database
- **sentence-transformers** - Embedding model
- **numpy** - Numerical operations
- **scipy** - Scientific computing

### Step 3: Verify Installation
```bash
python -c "import chromadb; print('✓ ChromaDB ready')"
python -c "from sentence_transformers import SentenceTransformer; print('✓ Transformers ready')"
```

## Running the Systems

### Interactive Search
```bash
python interactive_search.py
```

Then type searches like:
- `chocolate dessert`
- `italian food`
- `healthy meal`
- `sweet treats`
- `low calorie`

### Advanced Search with Filters
```bash
python advanced_search.py
```

Select from the menu:
1. **Basic Search** - Standard similarity search
2. **Cuisine Filter** - Search within specific cuisine types
3. **Calorie Filter** - Find foods under a calorie limit
4. **Combined Filters** - Use multiple constraints
5. **Demo Mode** - See three example searches
6. **Help** - Learn more
7. **Exit**

## Dataset

**FoodDataSet.json** contains 185 food items with fields:
- `name` - Food name
- `description` - Full description
- `ingredients` - List of ingredients
- `calories` - Per serving
- `cuisine` - Cuisine type
- `cooking_method` - How it's prepared
- `health_benefits` - Nutritional info
- `taste_profile` - Flavor characteristics

## Understanding Vector Embeddings

### What is an Embedding?
Text → Mathematical Vector (384 numbers)

```
"Chocolate cake with vanilla frosting"
              ↓ (embedding model)
[0.12, -0.45, 0.89, ... 0.34]  (384 dimensions)

"Rich cocoa cake with cream icing"
              ↓ (embedding model)
[0.11, -0.48, 0.87, ... 0.36]  (384 dimensions)

Similarity Score: 95.2% (very similar vectors → semantically similar foods)
```

### Why This Matters
- **Synonym Understanding**: "dessert" ~ "sweet treat"
- **Concept Matching**: "healthy meal" matches both salads AND grilled fish
- **Semantic Search**: Finds foods by meaning, not just keyword matching
- **Flexible Queries**: Works with natural language, not rigid databases

### Similarity Score (0-100%)
- **90-100%**: Almost identical foods
- **70-89%**: Related foods with same category
- **50-69%**: Similar but different
- **< 50%**: Loosely related

## Shared Functions Module

All systems use `shared_functions.py` for reusable utilities:

```python
# Load and normalize food data from JSON
food_items = load_food_data('./FoodDataSet.json')

# Create Chroma DB collection for similarity search
collection = create_similarity_search_collection(
    "food_search",
    {'description': 'Food similarity search'}
)

# Add all foods to collection (computes embeddings)
populate_similarity_collection(collection, food_items)

# Perform similarity search
results = perform_similarity_search(
    collection, 
    query="chocolate dessert",
    n_results=5
)

# Search with metadata filters
results = perform_filtered_similarity_search(
    collection,
    query="pasta",
    cuisine_filter="Italian",
    max_calories=500,
    n_results=5
)
```

## Example Usage Scenarios

### Scenario 1: Dietary Restriction
```
User Query: "healthy meal under 300 calories"

System:
1. Converts to embedding
2. Searches for healthy, low-calorie foods
3. Returns: Grilled fish, salads, vegetable soups

Results exclude: Desserts, fried foods, high-calorie items
```

### Scenario 2: Cuisine Preference
```
User Query: "creamy pasta" with "Italian" filter

System:
1. Finds pasta dishes semantically
2. Filters to Italian cuisine only
3. Returns: Fettuccine Alfredo, Carbonara, Penne Creamy

Results exclude: Thai pasta, Asian noodles, Mexican dishes
```

### Scenario 3: Combined Constraints
```
User Query: "quick dinner"
Constraints: "Asian" cuisine, "< 400 cal"

System:
1. Finds quick/easy to prepare foods
2. Filters to Asian cuisine
3. Filters to under 400 calories
4. Returns: Thai curry, Stir fry, Vietnamese soup

All constraints must be satisfied
```

## Learning Outcomes

After working with this project, you'll understand:

1. ✅ How embeddings work and why they're powerful
2. ✅ How to use vector databases for similarity search
3. ✅ How to combine search with metadata filtering
4. ✅ How to build RAG systems (retrieval + generation)
5. ✅ How modern recommendation systems work
6. ✅ How to structure Python projects with reusable modules

## Technical Details

### Embedding Model
- **Model**: all-MiniLM-L6-v2
- **Dimensions**: 384
- **Speed**: ~6800 embeddings/sec
- **Size**: 22 MB
- **Language**: English (optimized for semantic search)

### Vector Similarity
- **Metric**: Cosine Distance
- **Range**: 0 to 1 (higher = more similar)
- **Time Complexity**: O(n) for n foods in database
- **Scalability**: Works efficiently up to millions of items

### Database
- **Type**: Local vector database (no cloud dependency)
- **Storage**: In-memory (fast, for demonstrations)
- **Persistence**: Can be configured for disk storage
- **Scaling**: Handles hundreds of thousands of items

## Troubleshooting

### "No such file or directory: './FoodDataSet.json'"
**Solution**: Run scripts from the project directory
```bash
cd "C:\Ai Projects\food-search-rag-chatbot"
python interactive_search.py
```

### "No module named 'chromadb'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Unicode/Emoji errors on Windows
**Solution**: Already fixed! UTF-8 encoding is set in scripts

### Slow first run
**Solution**: First run downloads the embedding model (~100 MB). Subsequent runs are faster.

## Project Structure

```
food-search-rag-chatbot/
├── shared_functions.py      # Reusable utility functions
├── interactive_search.py    # Interactive CLI search
├── advanced_search.py       # Advanced search with filtering
├── FoodDataSet.json         # 185 food items dataset
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── .gitignore             # Git ignore rules
```

## Next Steps & Extensions

### Current (Implemented)
- ✅ Semantic similarity search
- ✅ Metadata filtering
- ✅ Interactive CLI interface
- ✅ Advanced menu system

### Coming Soon
- 🔄 RAG Chatbot with IBM Granite LLM
- 🔄 Conversational responses
- 🔄 Multi-turn conversations
- 🔄 Dietary profile learning

### Possible Extensions
- Add nutrition analysis
- Implement recipe generation
- Create web interface
- Connect to restaurant APIs
- Add user preferences learning
- Implement meal planning
- Add cost estimation
- Create mobile app

## Resources & Learning Links

- [Sentence-Transformers Docs](https://www.sbert.net/)
- [Chroma DB Documentation](https://docs.trychroma.com/)
- [Vector Database Concepts](https://www.pinecone.io/learn/vector-database/)
- [RAG Architecture Guide](https://www.anthropic.com/research/rag)
- [Embeddings Explained](https://openai.com/blog/new-and-improved-embedding-model)

## Git & Version Control

```bash
# View commit history
git log --oneline

# See what changed
git diff HEAD~1

# Check current branch
git branch -v

# Push changes to GitHub
git push origin master
```

## Performance Notes

- **Embedding Generation**: ~6,800 items/second
- **Similarity Search**: <50ms for 185 items
- **Filtering**: Instant (metadata-based)
- **Model Download**: ~100 MB on first run
- **Memory Usage**: ~500 MB (including model)

## Contributing & Modifications

This is a learning project. Feel free to:
- Add more food items to the dataset
- Implement additional cuisines
- Create new search strategies
- Build the RAG chatbot with LLM
- Add persistence to vector database
- Implement user preference learning

## License

This project is for educational purposes. Built with open-source tools (ChromaDB, Sentence-Transformers, etc.).

---

**Stack**: Python 3.8+, ChromaDB, Sentence-Transformers, NumPy, SciPy  
**Status**: Learning/Demonstration Project  
**Last Updated**: 2026-06-14  
**Repository**: https://github.com/ssadiqh/food-search-rag-chatbot
# IIIT Kalyani College Chatbot 🎓

A powerful AI-powered chatbot built from scratch to provide real-time information about IIIT Kalyani. This chatbot uses natural language processing with sentence transformers to understand queries and provide accurate responses about the college.

## 🌟 Features

- **Real College Data**: Contains actual information fetched from IIIT Kalyani's official website
- **Intelligent Response System**: Uses sentence transformers (Mini-LM model) for semantic understanding
- **Beautiful Web Interface**: Modern, responsive chat interface
- **REST API**: Complete API for integration with other systems
- **Real-time Web Scraping**: Can fetch live data from the college website
- **Multi-topic Coverage**: Information about:
  - Admissions process
  - Academic programs (B.Tech, M.Tech, PhD)
  - Departments and specializations
  - Research facilities and sponsored projects
  - Student achievements
  - Events and activities
  - Placements
  - Facilities and infrastructure
  - Fee structure
  - Scholarships
  - Contact information

## 🏗️ Project Structure

```
college-chat-bot/
├── app.py                  # Flask web application
├── chatbot_model.py        # Core chatbot logic with LLM
├── web_scraper.py          # Real-time data fetching
├── college_data.json       # College information database
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface
└── README.md              # Documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Navigate to Project
```bash
cd /Users/anurag/Desktop/college-chat-bot
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note**: The first run will download the sentence transformer model (~100MB). This is a one-time download.

## 💻 Usage

### Method 1: Web Interface (Recommended)

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and go to:
```
http://localhost:5000
```

3. Start chatting! Try questions like:
   - "What programs does IIIT Kalyani offer?"
   - "How can I get admission?"
   - "Tell me about the placement statistics"
   - "What are the research facilities?"
   - "What is the fee structure?"

### Method 2: Command Line Interface

For testing the chatbot model directly:
```bash
python chatbot_model.py
```

This will start an interactive chat session in your terminal.

### Method 3: Use the REST API

Send POST requests to interact programmatically:

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What programs are offered?"}'
```

Response:
```json
{
  "response": "IIIT Kalyani offers...",
  "status": "success"
}
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/api/chat` | POST | Send message to chatbot |
| `/api/health` | GET | Health check |
| `/api/info` | GET | Get basic college info |

## 🌐 Web Scraping

To fetch the latest data from the college website:

```bash
python web_scraper.py
```

This will:
1. Fetch live announcements and events
2. Update the college data file
3. Make the chatbot aware of the latest information

## 🧠 How It Works

### The LLM Model

The chatbot uses a **retrieval-based approach** with semantic understanding:

1. **Data Preparation**: College information is broken into semantic chunks
2. **Embedding Generation**: Each chunk is converted to a vector using `all-MiniLM-L6-v2` sentence transformer
3. **Query Processing**: User questions are also converted to vectors
4. **Similarity Matching**: Cosine similarity finds the most relevant information
5. **Response Generation**: Top matching chunks are combined to form a coherent answer

### Architecture

```
User Query
    ↓
Sentence Embedding (LLM)
    ↓
Similarity Search (Cosine)
    ↓
Top-K Retrieval
    ↓
Response Generation
    ↓
User Response
```

## 📊 Sample Questions to Try

**Admissions:**
- "How do I apply for B.Tech?"
- "What is the admission process?"
- "Is GATE required for M.Tech?"

**Programs:**
- "What courses are available?"
- "Tell me about the CSE department"
- "What specializations are offered?"

**Research:**
- "What research facilities are available?"
- "Tell me about ongoing projects"
- "What labs does the college have?"

**Placements:**
- "How are the placements?"
- "Which companies visit for placements?"

**General:**
- "What is IIIT Kalyani?"
- "Where is the college located?"
- "How do I contact the college?"

## 🎨 Customization

### Adding New Data

Edit `college_data.json` to add or update information:

```json
{
  "new_section": {
    "title": "Your Title",
    "content": "Your content..."
  }
}
```

Then restart the application.

### Changing the Model

In `chatbot_model.py`, you can change the sentence transformer model:

```python
self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Default
# Or try:
# self.model = SentenceTransformer('all-mpnet-base-v2')  # More accurate
```

### Customizing the UI

Edit `templates/index.html` to modify colors, layout, or styling.

## 🔍 Technical Details

**NLP Model**: `all-MiniLM-L6-v2`
- Lightweight and fast
- 384-dimensional embeddings
- Good balance of speed and accuracy

**Similarity Metric**: Cosine Similarity
- Measures semantic similarity between query and knowledge base
- Returns top-k most relevant chunks

**Web Framework**: Flask
- Lightweight Python web framework
- RESTful API design
- CORS enabled for cross-origin requests

## 🐛 Troubleshooting

### Issue: Model download takes too long
**Solution**: This is normal for first run. The model is ~100MB and downloads once.

### Issue: "Module not found" errors
**Solution**: Make sure you installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Port 5000 already in use
**Solution**: Either stop the other service or change the port in `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Issue: Web scraper not working
**Solution**: The college website might be down or changed structure. The chatbot will still work with static data.

## 📝 Future Enhancements

- [ ] Add generative AI capabilities using GPT/LLaMA
- [ ] Implement conversation history
- [ ] Add voice input/output
- [ ] Multi-language support
- [ ] Mobile app
- [ ] Integration with college database
- [ ] Student authentication
- [ ] Personalized responses based on user profile

## 🤝 Contributing

This is a college project. Feel free to:
1. Fork the repository
2. Add new features
3. Improve the model
4. Enhance the UI
5. Add more data

## 📄 License

This project is created for educational purposes as part of a college project at IIIT Kalyani.

## 👥 Credits

- **College Data**: Fetched from [IIIT Kalyani Official Website](https://iiitkalyani.ac.in)
- **NLP Model**: Sentence Transformers by UKPLab
- **Web Framework**: Flask by Pallets

## 📞 Support

For questions or issues:
- Check the troubleshooting section
- Review the code comments
- Test with the sample questions

---

**Built with ❤️ for IIIT Kalyani**

*Last Updated: October 2025*

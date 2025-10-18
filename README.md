# 🎓 IIIT Kalyani College Chatbot# IIIT Kalyani College Chatbot 🎓



[![GitHub](https://img.shields.io/badge/github-College--ChatBot-blue)](https://github.com/Anurag02012004/College-ChatBot)A powerful AI-powered chatbot built from scratch to provide real-time information about IIIT Kalyani. This chatbot uses natural language processing with sentence transformers to understand queries and provide accurate responses about the college.

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

[![Flask](https://img.shields.io/badge/flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)## 🌟 Features

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

- **Real College Data**: Contains actual information fetched from IIIT Kalyani's official website

An intelligent AI-powered chatbot for IIIT Kalyani providing comprehensive information about faculty, courses, placements, events, and more using advanced natural language processing.- **Intelligent Response System**: Uses sentence transformers (Mini-LM model) for semantic understanding

- **Beautiful Web Interface**: Modern, responsive chat interface

## ✨ Features- **REST API**: Complete API for integration with other systems

- **Real-time Web Scraping**: Can fetch live data from the college website

- 🤖 **AI-Powered**: Uses Sentence Transformers for semantic understanding- **Multi-topic Coverage**: Information about:

- 📊 **Comprehensive Data**: 16+ faculty members, 494+ data points  - Admissions process

- 📝 **Structured Responses**: Beautiful, well-formatted information display  - Academic programs (B.Tech, M.Tech, PhD)

- ⚡ **Real-time Chat**: Responsive and fast web interface  - Departments and specializations

- 🔌 **RESTful API**: Easy integration with other applications  - Research facilities and sponsored projects

- 🎨 **Modern UI**: Clean gradient design with smooth animations  - Student achievements

  - Events and activities

## 🚀 Quick Start  - Placements

  - Facilities and infrastructure

### Prerequisites  - Fee structure

- Python 3.11+  - Scholarships

- Git  - Contact information

- pip

## 🏗️ Project Structure

### Local Setup

```

```bashcollege-chat-bot/

# Clone repository├── app.py                  # Flask web application

git clone https://github.com/Anurag02012004/College-ChatBot.git├── chatbot_model.py        # Core chatbot logic with LLM

cd College-ChatBot├── web_scraper.py          # Real-time data fetching

├── college_data.json       # College information database

# Create virtual environment├── requirements.txt        # Python dependencies

python3 -m venv venv├── templates/

source venv/bin/activate  # Windows: venv\Scripts\activate│   └── index.html         # Web interface

└── README.md              # Documentation

# Install dependencies```

pip install -r requirements.txt

## 🚀 Installation

# Run application

python app.py### Prerequisites

- Python 3.8 or higher

# Open browser- pip (Python package manager)

# Navigate to http://localhost:5001

```### Step 1: Clone or Navigate to Project

```bash

## 🌐 Deployment (FREE!)cd /Users/anurag/Desktop/college-chat-bot

```

### ✅ Step 1: GitHub (DONE!)

Your code is at: https://github.com/Anurag02012004/College-ChatBot### Step 2: Create Virtual Environment (Recommended)

```bash

### Step 2: Deploy Backend to Renderpython3 -m venv venv

source venv/bin/activate  # On macOS/Linux

1. Go to [render.com](https://render.com) and sign in with GitHub```

2. Click "New +" → "Web Service"

3. Connect `Anurag02012004/College-ChatBot` repository### Step 3: Install Dependencies

4. Render auto-detects settings from `render.yaml````bash

5. Click "Create Web Service"pip install -r requirements.txt

6. Wait 5-10 minutes, get your URL: `https://your-app.onrender.com````



### Step 3: Deploy Frontend to Netlify**Note**: The first run will download the sentence transformer model (~100MB). This is a one-time download.



1. Update API URL:## 💻 Usage

   ```bash

   ./update_api_url.sh https://your-backend.onrender.com### Method 1: Web Interface (Recommended)

   git add static-frontend/index.html

   git commit -m "Update production API URL"1. Start the Flask server:

   git push```bash

   ```python app.py

```

2. Go to [netlify.com](https://www.netlify.com) and sign in

3. "Add new site" → "Import from GitHub"2. Open your web browser and go to:

4. Select `College-ChatBot` repo```

5. Base directory: `static-frontend`http://localhost:5000

6. Deploy!```



**See [DEPLOYMENT_STEPS.md](DEPLOYMENT_STEPS.md) for detailed guide.**3. Start chatting! Try questions like:

   - "What programs does IIIT Kalyani offer?"

## 💬 Example Queries   - "How can I get admission?"

   - "Tell me about the placement statistics"

- "Tell me about Dr. Anirban Lakshman"   - "What are the research facilities?"

- "Who is the director?"   - "What is the fee structure?"

- "Show me CSE faculty"

- "What are the placement records?"### Method 2: Command Line Interface

- "Tell me about recent events"

For testing the chatbot model directly:

## 🔌 API Endpoints```bash

python chatbot_model.py

### `POST /api/chat````

```json

{This will start an interactive chat session in your terminal.

  "message": "Tell me about Dr. Anirban Lakshman"

}### Method 3: Use the REST API

```

Send POST requests to interact programmatically:

### `GET /api/health`

Health check```bash

curl -X POST http://localhost:5000/api/chat \

### `GET /api/info`  -H "Content-Type: application/json" \

Basic college information  -d '{"message": "What programs are offered?"}'

```

## 🛠️ Technology Stack

Response:

- **Backend**: Flask, Python 3.11, Gunicorn```json

- **AI/ML**: Sentence Transformers, PyTorch{

- **Frontend**: HTML5, CSS3, JavaScript  "response": "IIIT Kalyani offers...",

- **Deployment**: Render (backend), Netlify (frontend)  "status": "success"

}

## 📁 Project Structure```



```## 🔧 API Endpoints

College-ChatBot/

├── app.py                     # Flask application| Endpoint | Method | Description |

├── structured_chatbot.py      # AI chatbot|----------|--------|-------------|

├── faculty_data.json          # 16+ faculty members| `/` | GET | Web interface |

├── comprehensive_college_data.json  # 494+ data points| `/api/chat` | POST | Send message to chatbot |

├── templates/index.html       # Web interface| `/api/health` | GET | Health check |

├── static-frontend/           # Netlify frontend| `/api/info` | GET | Get basic college info |

├── requirements.txt           # Dependencies

└── render.yaml               # Deployment config## 🌐 Web Scraping

```

To fetch the latest data from the college website:

## 🤝 Contributing

```bash

1. Fork the repositorypython web_scraper.py

2. Create feature branch: `git checkout -b feature/AmazingFeature````

3. Commit changes: `git commit -m 'Add AmazingFeature'`

4. Push: `git push origin feature/AmazingFeature`This will:

5. Open Pull Request1. Fetch live announcements and events

2. Update the college data file

## 📧 Contact3. Make the chatbot aware of the latest information



- **Developer**: Anurag## 🧠 How It Works

- **GitHub**: [@Anurag02012004](https://github.com/Anurag02012004)

- **Issues**: [Report bugs](https://github.com/Anurag02012004/College-ChatBot/issues)### The LLM Model



## 📄 LicenseThe chatbot uses a **retrieval-based approach** with semantic understanding:



MIT License - see LICENSE file1. **Data Preparation**: College information is broken into semantic chunks

2. **Embedding Generation**: Each chunk is converted to a vector using `all-MiniLM-L6-v2` sentence transformer

---3. **Query Processing**: User questions are also converted to vectors

4. **Similarity Matching**: Cosine similarity finds the most relevant information

<div align="center">5. **Response Generation**: Top matching chunks are combined to form a coherent answer



**Made with ❤️ for IIIT Kalyani**### Architecture



[⭐ Star this repo](https://github.com/Anurag02012004/College-ChatBot) | [📖 Documentation](DEPLOYMENT_STEPS.md) | [🐛 Report Bug](https://github.com/Anurag02012004/College-ChatBot/issues)```

User Query

</div>    ↓

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

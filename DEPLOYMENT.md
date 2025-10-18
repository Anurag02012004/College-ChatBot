# IIIT Kalyani College Chatbot 🎓

An intelligent chatbot for IIIT Kalyani that provides information about faculty, courses, placements, events, and more using AI-powered natural language processing.

## 🌟 Features

- **AI-Powered Responses**: Uses sentence transformers for semantic understanding
- **Comprehensive Data**: 16+ faculty members, placement records, events, research projects
- **Structured Responses**: Well-formatted, easy-to-read information
- **Real-time Chat**: Beautiful, responsive web interface
- **RESTful API**: Easy integration with other applications

## 🚀 Live Demo

- **Backend API**: [Your Render/Railway URL]
- **Frontend**: [Your Netlify URL]

## 📋 Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git

## 🛠️ Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anurag02012004/College-ChatBot.git
   cd College-ChatBot
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5001
   ```

## 🌐 Deployment

### Backend Deployment (Render/Railway/Heroku)

#### Option 1: Render (Recommended - Free Tier)
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new "Web Service"
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml`
6. Click "Create Web Service"

#### Option 2: Railway
1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-deploy using `Procfile`

#### Option 3: Heroku
```bash
heroku login
heroku create your-chatbot-name
git push heroku main
```

### Frontend Deployment (Netlify)

1. Go to [netlify.com](https://www.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Select the `static-frontend` folder
4. Update the API URL in `index.html`:
   ```javascript
   const API_URL = 'https://your-backend-url.onrender.com';
   ```
5. Deploy!

## 📁 Project Structure

```
college-chat-bot/
├── app.py                          # Flask application
├── structured_chatbot.py           # AI chatbot with structured responses
├── faculty_data.json               # Real faculty information
├── comprehensive_college_data.json # College data (494+ items)
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── render.yaml                     # Render deployment config
├── templates/
│   └── index.html                  # Web interface
└── static-frontend/
    └── index.html                  # Standalone frontend for Netlify
```

## 🔌 API Endpoints

### `POST /api/chat`
Send a message to the chatbot
```json
Request:
{
  "message": "Tell me about Dr. Anirban Lakshman"
}

Response:
{
  "response": "👨‍🏫 FACULTY INFORMATION\n...",
  "status": "success"
}
```

### `GET /api/health`
Check API health status

### `GET /api/info`
Get basic college information

## 💡 Example Queries

- "Tell me about Dr. Anirban Lakshman"
- "Who is the director?"
- "Show me CSE faculty"
- "What are the placement records?"
- "Tell me about upcoming events"
- "What research projects are ongoing?"

## 🧠 Technology Stack

- **Backend**: Flask, Python 3.11
- **AI/ML**: Sentence Transformers, PyTorch
- **Frontend**: HTML5, CSS3, JavaScript
- **Data**: BeautifulSoup4 for web scraping
- **Deployment**: Render (backend), Netlify (frontend)

## 📊 Data Sources

All data is scraped from official IIIT Kalyani website:
- Faculty: https://iiitkalyani.ac.in/newfacultypages/faculty1.php
- College Info: https://iiitkalyani.ac.in

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👥 Authors

- Anurag - [@Anurag02012004](https://github.com/Anurag02012004)

## 🙏 Acknowledgments

- IIIT Kalyani for providing publicly available information
- Sentence Transformers library
- Flask framework

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ for IIIT Kalyani

# QUICK START GUIDE 🚀

## First Time Setup (5 minutes)

### Option 1: Automatic Setup (Recommended)
```bash
cd /Users/anurag/Desktop/college-chat-bot
./setup.sh
```

### Option 2: Manual Setup
```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

## Running the Chatbot

### Easy Way (Menu-driven)
```bash
python3 run.py
```

### Specific Methods

**1. Web Interface** (Best for testing)
```bash
python3 app.py
# Open: http://localhost:5000
```

**2. Command Line**
```bash
python3 chatbot_model.py
```

**3. Demo Mode** (See all features)
```bash
python3 demo.py
```

## Sample Questions to Test

✅ **Try these to see real data responses:**

### About College
- "What is IIIT Kalyani?"
- "Where is IIIT Kalyani located?"
- "When was it established?"

### Programs
- "What programs are offered?"
- "Tell me about B.Tech in CSE"
- "What M.Tech specializations are available?"

### Admissions
- "How to get admission?"
- "What is the admission process for B.Tech?"
- "Do I need GATE for M.Tech?"

### Facilities
- "What research facilities are there?"
- "Tell me about the labs"
- "What facilities are available for students?"

### Placements & Fees
- "How are the placements?"
- "What is the fee structure?"
- "Are scholarships available?"

### Contact
- "How to contact the college?"
- "What is the address?"

## Project Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Flask web server |
| `chatbot_model.py` | Core AI chatbot logic |
| `college_data.json` | Real IIIT Kalyani data |
| `web_scraper.py` | Fetch live data from website |
| `run.py` | Easy launcher script |
| `demo.py` | Full feature demonstration |
| `requirements.txt` | Python dependencies |

## Common Issues & Solutions

### ❌ "Module not found"
```bash
pip install -r requirements.txt
```

### ❌ "Port already in use"
Change port in `app.py` line 78:
```python
app.run(host='0.0.0.0', port=5001)  # Changed from 5000
```

### ❌ "Model downloading is slow"
This is normal on first run (~100MB). One-time only.

### ❌ Virtual environment issues
```bash
deactivate  # Exit current venv
rm -rf venv  # Remove old venv
python3 -m venv venv  # Create new venv
source venv/bin/activate  # Activate
pip install -r requirements.txt  # Reinstall
```

## How It Works (Simple Explanation)

```
Your Question
     ↓
AI converts to numbers (embedding)
     ↓
Compares with college data
     ↓
Finds most similar info
     ↓
Returns answer
```

**Technology:**
- 🧠 **AI Model**: Sentence Transformers (Mini-LM)
- 🔍 **Matching**: Cosine Similarity
- 🌐 **Web**: Flask Framework
- 📊 **Data**: Real IIIT Kalyani information

## Next Steps

1. ✅ Test with sample questions above
2. ✅ Try the web interface
3. ✅ Add more data to `college_data.json`
4. ✅ Customize the UI in `templates/index.html`
5. ✅ Deploy to a server (optional)

## Need Help?

- Check `README.md` for detailed docs
- Run `python3 demo.py` to see all features
- Look at code comments for technical details

---

**Built for IIIT Kalyani College Project** 🎓

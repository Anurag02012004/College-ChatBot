#!/bin/bash

# College Chatbot Setup Script for macOS/Linux

echo "🎓 IIIT Kalyani College Chatbot - Setup Script"
echo "=============================================="
echo ""

# Check Python version
echo "📌 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Found: $PYTHON_VERSION"
else
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✅ Virtual environment created!"
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "⬆️  Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1

# Install dependencies
echo ""
echo "📥 Installing dependencies (this may take a few minutes)..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully!"
else
    echo "❌ Error installing dependencies. Please check requirements.txt"
    exit 1
fi

# Test installation
echo ""
echo "🧪 Testing chatbot..."
python3 quick_start.py

echo ""
echo "=============================================="
echo "🎉 Setup Complete!"
echo "=============================================="
echo ""
echo "📌 To start the chatbot:"
echo "   1. Activate virtual environment: source venv/bin/activate"
echo "   2. Run the web app: python app.py"
echo "   3. Open browser: http://localhost:5000"
echo ""
echo "📌 For CLI mode:"
echo "   python chatbot_model.py"
echo ""
echo "Happy chatting! 🤖"
echo ""

"""
Quick Start Script for College Chatbot
Run this to test the chatbot quickly
"""

import sys
import os

def check_dependencies():
    """Check if required packages are installed."""
    required = ['flask', 'sentence_transformers', 'numpy', 'sklearn', 'bs4']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("❌ Missing dependencies:")
        for pkg in missing:
            print(f"   - {pkg}")
        print("\n📦 Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies installed!")
    return True


def test_chatbot():
    """Test the chatbot with sample queries."""
    try:
        from chatbot_model import CollegeChatbot
        
        print("\n" + "="*60)
        print("🤖 Testing College Chatbot")
        print("="*60)
        
        chatbot = CollegeChatbot()
        
        test_queries = [
            "What is IIIT Kalyani?",
            "What programs are offered?",
            "How can I get admission?",
            "Tell me about placements"
        ]
        
        print("\n📝 Running test queries...\n")
        
        for i, query in enumerate(test_queries, 1):
            print(f"Q{i}: {query}")
            response = chatbot.get_response(query)
            print(f"A{i}: {response}\n")
            print("-" * 60 + "\n")
        
        print("✅ Chatbot is working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing chatbot: {e}")
        return False


def main():
    """Main function to run quick tests."""
    print("\n🚀 College Chatbot - Quick Start\n")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Test chatbot
    if not test_chatbot():
        sys.exit(1)
    
    print("\n" + "="*60)
    print("🎉 Setup Complete!")
    print("="*60)
    print("\n📌 Next Steps:")
    print("   1. Run 'python app.py' to start the web server")
    print("   2. Open http://localhost:5000 in your browser")
    print("   3. Start chatting!\n")
    print("   Or run 'python chatbot_model.py' for CLI mode\n")


if __name__ == "__main__":
    main()

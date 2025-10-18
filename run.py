#!/usr/bin/env python3
"""
Simple run script for the College Chatbot
"""

import sys
import os

def main():
    """Main function to run the chatbot."""
    
    print("\n" + "="*60)
    print("🎓 IIIT Kalyani College Chatbot")
    print("="*60)
    print("\nChoose an option:")
    print("  1. Start Web Interface (Recommended)")
    print("  2. Start CLI Chatbot")
    print("  3. Run Demo with Test Queries")
    print("  4. Update Live Data from Website")
    print("  5. Exit")
    print("\n" + "="*60)
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        print("\n🌐 Starting web server...")
        print("Open http://localhost:5000 in your browser")
        print("Press Ctrl+C to stop the server\n")
        os.system("python3 app.py")
    
    elif choice == "2":
        print("\n💬 Starting CLI chatbot...\n")
        os.system("python3 chatbot_model.py")
    
    elif choice == "3":
        print("\n🎯 Running demo...\n")
        os.system("python3 demo.py")
    
    elif choice == "4":
        print("\n🌐 Fetching live data from website...\n")
        os.system("python3 web_scraper.py")
    
    elif choice == "5":
        print("\n👋 Goodbye!\n")
        sys.exit(0)
    
    else:
        print("\n❌ Invalid choice. Please try again.\n")
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)

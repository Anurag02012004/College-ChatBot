"""
Demo Script - Test the Chatbot with Various Queries
This script demonstrates the chatbot's capabilities
"""

from chatbot_model import CollegeChatbot
import time


def print_separator():
    """Print a visual separator."""
    print("\n" + "="*70 + "\n")


def demo_chatbot():
    """Run a comprehensive demo of the chatbot."""
    
    print_separator()
    print("🎓 IIIT KALYANI COLLEGE CHATBOT - DEMO")
    print_separator()
    
    print("Initializing chatbot with real college data...")
    chatbot = CollegeChatbot()
    
    print_separator()
    print("✅ Chatbot Ready! Let's test with real queries...")
    print_separator()
    
    # Test queries covering different topics
    test_queries = [
        {
            "category": "Basic Information",
            "queries": [
                "What is IIIT Kalyani?",
                "Where is the college located?",
                "When was IIIT Kalyani established?"
            ]
        },
        {
            "category": "Academic Programs",
            "queries": [
                "What programs does IIIT Kalyani offer?",
                "Tell me about B.Tech courses",
                "What is the duration of M.Tech program?"
            ]
        },
        {
            "category": "Admissions",
            "queries": [
                "How can I get admission to IIIT Kalyani?",
                "What is the admission process for B.Tech?",
                "Is GATE required for M.Tech admission?"
            ]
        },
        {
            "category": "Facilities & Research",
            "queries": [
                "What research facilities are available?",
                "Tell me about the VLSI lab",
                "What sponsored projects are running?"
            ]
        },
        {
            "category": "Student Life",
            "queries": [
                "What facilities are available for students?",
                "Tell me about recent events",
                "What are student achievements?"
            ]
        },
        {
            "category": "Placements & Career",
            "queries": [
                "How are the placements?",
                "What scholarships are available?",
                "What is the fee structure?"
            ]
        },
        {
            "category": "Contact & General",
            "queries": [
                "How can I contact the college?",
                "What is the address of IIIT Kalyani?"
            ]
        }
    ]
    
    for section in test_queries:
        print(f"📚 {section['category']}")
        print("-" * 70)
        
        for query in section['queries']:
            print(f"\n❓ Question: {query}")
            
            # Get response
            response = chatbot.get_response(query)
            
            print(f"🤖 Answer: {response}")
            time.sleep(0.5)  # Small delay for readability
        
        print_separator()
    
    # Interactive mode
    print("🎯 INTERACTIVE MODE")
    print("-" * 70)
    print("Now you can ask your own questions!")
    print("Type 'quit' to exit")
    print_separator()
    
    while True:
        user_query = input("Your Question: ").strip()
        
        if not user_query:
            continue
        
        if user_query.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thank you for testing the chatbot! Goodbye!")
            break
        
        response = chatbot.get_response(user_query)
        print(f"\n🤖 Answer: {response}\n")
        print("-" * 70 + "\n")


if __name__ == "__main__":
    try:
        demo_chatbot()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure you have installed all dependencies:")
        print("pip install -r requirements.txt")

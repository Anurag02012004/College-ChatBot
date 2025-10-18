"""
Test Suite for College Chatbot
Validates that the chatbot is working correctly with real data
"""

import json
import sys


def test_data_file():
    """Test that college data file exists and is valid."""
    print("📝 Test 1: Checking data file...")
    try:
        with open('college_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check required sections
        required_keys = ['college_info', 'about', 'departments', 'programs', 
                        'research_facilities', 'admissions', 'contact_info']
        
        for key in required_keys:
            if key not in data:
                print(f"   ❌ Missing section: {key}")
                return False
        
        print(f"   ✅ Data file is valid")
        print(f"   ✅ Contains {len(data['departments'])} departments")
        print(f"   ✅ Contains {len(data['research_facilities'])} research facilities")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_imports():
    """Test that required packages are installed."""
    print("\n📦 Test 2: Checking dependencies...")
    packages = {
        'flask': 'Flask',
        'sentence_transformers': 'Sentence Transformers',
        'numpy': 'NumPy',
        'sklearn': 'Scikit-learn',
        'bs4': 'BeautifulSoup4'
    }
    
    all_ok = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"   ✅ {name}")
        except ImportError:
            print(f"   ❌ {name} not installed")
            all_ok = False
    
    return all_ok


def test_chatbot_initialization():
    """Test chatbot can be initialized."""
    print("\n🤖 Test 3: Initializing chatbot...")
    try:
        from chatbot_model import CollegeChatbot
        chatbot = CollegeChatbot()
        print(f"   ✅ Chatbot initialized successfully")
        print(f"   ✅ Knowledge base has {len(chatbot.knowledge_base)} entries")
        return True, chatbot
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False, None


def test_responses(chatbot):
    """Test chatbot responses to various queries."""
    print("\n💬 Test 4: Testing responses...")
    
    test_cases = [
        ("What is IIIT Kalyani?", ["IIIT", "Kalyani", "Institute"]),
        ("What programs are offered?", ["B.Tech", "M.Tech", "program"]),
        ("How to get admission?", ["admission", "JEE", "GATE"]),
        ("What facilities are available?", ["facility", "facilities", "lab"]),
        ("Tell me about placements", ["placement", "companies"]),
    ]
    
    all_passed = True
    for query, expected_keywords in test_cases:
        try:
            response = chatbot.get_response(query)
            
            # Check if response contains expected keywords
            has_keyword = any(keyword.lower() in response.lower() 
                            for keyword in expected_keywords)
            
            if has_keyword and len(response) > 20:
                print(f"   ✅ '{query[:40]}...'")
            else:
                print(f"   ⚠️  '{query[:40]}...' - Weak response")
                all_passed = False
        except Exception as e:
            print(f"   ❌ '{query[:40]}...' - Error: {e}")
            all_passed = False
    
    return all_passed


def test_real_data_accuracy():
    """Verify that responses contain real IIIT Kalyani data."""
    print("\n🎯 Test 5: Verifying real data...")
    try:
        from chatbot_model import CollegeChatbot
        chatbot = CollegeChatbot()
        
        # Test specific factual queries
        tests = [
            {
                "query": "Where is IIIT Kalyani located?",
                "expected": "Kalyani",
                "description": "Location check"
            },
            {
                "query": "What is the full name of the college?",
                "expected": "Indian Institute of Information Technology",
                "description": "Full name check"
            },
            {
                "query": "What departments are there?",
                "expected": "Computer Science",
                "description": "Department check"
            }
        ]
        
        all_passed = True
        for test in tests:
            response = chatbot.get_response(test["query"])
            if test["expected"].lower() in response.lower():
                print(f"   ✅ {test['description']}")
            else:
                print(f"   ❌ {test['description']} - Expected '{test['expected']}'")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("🧪 COLLEGE CHATBOT - TEST SUITE")
    print("="*60 + "\n")
    
    results = []
    
    # Test 1: Data file
    results.append(("Data File", test_data_file()))
    
    # Test 2: Dependencies
    results.append(("Dependencies", test_imports()))
    
    # Test 3 & 4: Chatbot initialization and responses
    init_success, chatbot = test_chatbot_initialization()
    results.append(("Initialization", init_success))
    
    if init_success and chatbot:
        results.append(("Responses", test_responses(chatbot)))
        results.append(("Real Data", test_real_data_accuracy()))
    else:
        results.append(("Responses", False))
        results.append(("Real Data", False))
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} | {test_name}")
    
    print("="*60)
    print(f"\nResult: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! The chatbot is ready to use.")
        print("\n📌 Next steps:")
        print("   • Run 'python3 app.py' to start the web interface")
        print("   • Run 'python3 demo.py' for a full demonstration")
        return True
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\n💡 Common fixes:")
        print("   • Install dependencies: pip install -r requirements.txt")
        print("   • Check college_data.json exists and is valid")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

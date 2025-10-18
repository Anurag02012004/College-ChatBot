"""
Enhanced College Chatbot with Structured Responses
Provides well-formatted, structured information instead of plain sentences
"""

import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
import re


class StructuredCollegeChatbot:
    """Chatbot that provides structured, well-formatted responses."""
    
    def __init__(self):
        """Initialize chatbot with all data sources."""
        print("Initializing Structured College Chatbot...")
        
        # Load all data sources
        self.load_all_data()
        
        # Initialize AI model
        print("Loading language model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Prepare knowledge base
        self.knowledge_base = self._prepare_knowledge_base()
        
        # Generate embeddings
        print("Generating embeddings...")
        self.embeddings = self._generate_embeddings()
        
        print(f"✅ Chatbot ready with {len(self.knowledge_base)} knowledge items!")
    
    def load_all_data(self):
        """Load all data files."""
        # Load faculty data
        try:
            with open('faculty_data.json', 'r', encoding='utf-8') as f:
                self.faculty_data = json.load(f)
            print("✅ Loaded faculty data (16+ faculty members)")
        except:
            self.faculty_data = {}
            print("⚠️ Faculty data not found")
        
        # Load comprehensive data
        try:
            with open('comprehensive_college_data.json', 'r', encoding='utf-8') as f:
                self.comprehensive_data = json.load(f)
            print("✅ Loaded comprehensive college data")
        except:
            self.comprehensive_data = {}
            print("⚠️ Comprehensive data not found")
        
        # Load basic data
        try:
            with open('college_data.json', 'r', encoding='utf-8') as f:
                self.basic_data = json.load(f)
            print("✅ Loaded basic college data")
        except:
            self.basic_data = {}
    
    def _prepare_knowledge_base(self):
        """Prepare searchable knowledge base."""
        knowledge = []
        
        # Add faculty information
        if self.faculty_data:
            # Director
            if 'director' in self.faculty_data:
                director = self.faculty_data['director']
                knowledge.append({
                    'text': f"Director: {director['name']}. {director['designation']}. "
                           f"Email: {director['email']}. Expertise: {', '.join(director['areas_of_expertise'])}",
                    'category': 'faculty',
                    'subcategory': 'director',
                    'data': director
                })
            
            # All faculty
            if 'faculty_members' in self.faculty_data:
                for faculty in self.faculty_data['faculty_members']:
                    text = f"Professor: {faculty['name']}. {faculty['designation']}. "
                    text += f"Department: {faculty['department']}. "
                    text += f"Qualification: {faculty['qualification']}. "
                    text += f"Email: {faculty['email']}. "
                    text += f"Expertise: {', '.join(faculty['areas_of_expertise'])}"
                    
                    knowledge.append({
                        'text': text,
                        'category': 'faculty',
                        'subcategory': 'professor',
                        'data': faculty
                    })
        
        # Add comprehensive data
        if self.comprehensive_data:
            # Student achievements
            if 'achievements_detailed' in self.comprehensive_data:
                for ach in self.comprehensive_data['achievements_detailed'][:25]:
                    text = ""
                    if 'student' in ach:
                        text += f"Student: {ach['student']}. "
                    if 'achievement' in ach:
                        text += f"Achievement: {ach['achievement']}. "
                    if 'event' in ach:
                        text += f"Event: {ach['event']}. "
                    if 'company' in ach:
                        text += f"Company: {ach['company']}."
                    
                    if text:
                        knowledge.append({
                            'text': text,
                            'category': 'achievements',
                            'data': ach
                        })
            
            # Placements
            if 'placements_detailed' in self.comprehensive_data:
                pl = self.comprehensive_data['placements_detailed']
                knowledge.append({
                    'text': f"Placements: {pl.get('overview', '')}. " + ". ".join(pl.get('highlights', [])[:3]),
                    'category': 'placements',
                    'data': pl
                })
            
            # Admissions
            if 'admissions_detailed' in self.comprehensive_data:
                adm = self.comprehensive_data['admissions_detailed']
                
                # UG
                if 'undergraduate' in adm and 'programs' in adm['undergraduate']:
                    for prog in adm['undergraduate']['programs']:
                        text = f"B.Tech Admission: {prog.get('name', '')}. "
                        text += f"Seats: {prog.get('seats', '')}. "
                        text += f"Entrance: {prog.get('entrance_exam', 'JEE Main')}. "
                        text += f"Counseling: {prog.get('counseling', 'JoSAA')}"
                        knowledge.append({
                            'text': text,
                            'category': 'admissions',
                            'subcategory': 'undergraduate',
                            'data': prog
                        })
                
                # Fees
                if 'fee_structure' in adm:
                    fees = adm['fee_structure']
                    if 'btech' in fees:
                        knowledge.append({
                            'text': f"B.Tech Fee: {fees['btech'].get('tuition_per_semester', '')} per semester. "
                                   f"Total annual (with hostel): {fees['btech'].get('total_annual', '')}",
                            'category': 'fees',
                            'data': fees['btech']
                        })
            
            # Research projects
            if 'research_projects' in self.comprehensive_data:
                res = self.comprehensive_data['research_projects']
                if 'projects' in res:
                    for proj in res['projects'][:10]:
                        text = f"Research Project: {proj.get('title', '')}. "
                        text += f"Sponsor: {proj.get('sponsor', '')}. "
                        text += f"Funding: {proj.get('amount', '')}. "
                        text += f"Area: {proj.get('area', '')}"
                        knowledge.append({
                            'text': text,
                            'category': 'research',
                            'data': proj
                        })
            
            # Events
            if 'events_detailed' in self.comprehensive_data:
                for event in self.comprehensive_data['events_detailed'][:15]:
                    text = f"Event: {event.get('name', '')}. "
                    if 'date' in event:
                        text += f"Date: {event['date']}. "
                    if 'type' in event:
                        text += f"Type: {event['type']}. "
                    if 'description' in event:
                        text += event['description']
                    knowledge.append({
                        'text': text,
                        'category': 'events',
                        'data': event
                    })
        
        # Add basic college info
        if self.basic_data:
            if 'college_info' in self.basic_data:
                info = self.basic_data['college_info']
                knowledge.append({
                    'text': f"College: {info['name']} ({info['short_name']}). "
                           f"Location: {info['location']}. Established: {info['established']}. "
                           f"Type: {info['type']}. Website: {info['website']}",
                    'category': 'basic_info',
                    'data': info
                })
            
            if 'contact_info' in self.basic_data:
                contact = self.basic_data['contact_info']
                knowledge.append({
                    'text': f"Contact: {contact['address']}. Phone: {contact['phone']}. "
                           f"Email: {contact['email']}",
                    'category': 'contact',
                    'data': contact
                })
        
        return knowledge
    
    def _generate_embeddings(self):
        """Generate embeddings for knowledge base."""
        texts = [item['text'] for item in self.knowledge_base]
        return self.model.encode(texts)
    
    def get_response(self, query, top_k=5):
        """Get structured response for query."""
        # Handle greetings
        greetings = ['hi', 'hello', 'hey', 'greetings']
        if any(greet in query.lower() for greet in greetings):
            return self._format_greeting()
        
        # Handle thanks
        if any(word in query.lower() for word in ['thank', 'thanks']):
            return "You're welcome! Ask me anything about IIIT Kalyani!"
        
        # Check for specific faculty query
        if self._is_faculty_query(query):
            return self._handle_faculty_query(query)
        
        # General query - use semantic search
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        if similarities[top_indices[0]] < 0.2:
            return self._format_help_message()
        
        # Get top results
        top_results = [self.knowledge_base[i] for i in top_indices]
        
        # Format based on category
        return self._format_structured_response(query, top_results)
    
    def _is_faculty_query(self, query):
        """Check if query is about faculty."""
        faculty_keywords = ['professor', 'faculty', 'teacher', 'dr', 'prof', 'sir', 'madam', 'anirban', 'lakshman']
        return any(kw in query.lower() for kw in faculty_keywords)
    
    def _handle_faculty_query(self, query):
        """Handle faculty-specific queries with structured response."""
        query_lower = query.lower()
        
        # Search for specific faculty member
        if self.faculty_data and 'faculty_members' in self.faculty_data:
            # Check director
            if 'director' in query_lower:
                director = self.faculty_data['director']
                return self._format_faculty_info(director, is_director=True)
            
            # Check for specific name
            for faculty in self.faculty_data['faculty_members']:
                name_parts = faculty['name'].lower().split()
                if any(part in query_lower for part in name_parts if len(part) > 3):
                    return self._format_faculty_info(faculty)
            
            # If no specific match, show all faculty by department
            if 'cse' in query_lower or 'computer science' in query_lower:
                return self._format_department_faculty('Computer Science and Engineering')
            elif 'ece' in query_lower or 'electronics' in query_lower:
                return self._format_department_faculty('Electronics and Communication Engineering')
            elif 'math' in query_lower:
                return self._format_department_faculty('Mathematics')
            else:
                # Show faculty list
                return self._format_all_faculty_list()
        
        return "Faculty information not available. Please try again."
    
    def _format_faculty_info(self, faculty, is_director=False):
        """Format faculty information in structured way."""
        title = "🎓 DIRECTOR INFORMATION" if is_director else "👨‍🏫 FACULTY INFORMATION"
        
        response = f"\n{title}\n{'='*50}\n\n"
        response += f"📛 Name: {faculty['name']}\n"
        response += f"💼 Designation: {faculty['designation']}\n"
        response += f"🏫 Department: {faculty.get('department', 'N/A')}\n"
        response += f"🎓 Qualification: {faculty['qualification']}\n"
        response += f"📧 Email: {faculty['email']}\n"
        response += f"\n🔬 Areas of Expertise:\n"
        for i, area in enumerate(faculty['areas_of_expertise'], 1):
            response += f"   {i}. {area}\n"
        
        if 'profile_url' in faculty:
            response += f"\n🌐 Profile: {faculty['profile_url']}\n"
        
        return response
    
    def _format_department_faculty(self, department):
        """Format faculty list by department."""
        response = f"\n🏫 {department.upper()} FACULTY\n{'='*50}\n\n"
        
        faculty_list = [f for f in self.faculty_data.get('faculty_members', []) 
                       if f.get('department') == department]
        
        for i, faculty in enumerate(faculty_list, 1):
            response += f"{i}. {faculty['name']}\n"
            response += f"   └─ {faculty['designation']}\n"
            response += f"   └─ Email: {faculty['email']}\n"
            response += f"   └─ Expertise: {', '.join(faculty['areas_of_expertise'][:2])}\n\n"
        
        return response
    
    def _format_all_faculty_list(self):
        """Format complete faculty list."""
        response = "\n👨‍🏫 IIIT KALYANI FACULTY MEMBERS\n" + "="*50 + "\n\n"
        
        # Director
        if 'director' in self.faculty_data:
            director = self.faculty_data['director']
            response += f"🎓 DIRECTOR:\n   {director['name']} - {director['email']}\n\n"
        
        # By department
        if 'departments_summary' in self.faculty_data:
            for dept, info in self.faculty_data['departments_summary'].items():
                response += f"🏫 {dept}:\n"
                for name in info['faculty_names']:
                    response += f"   • {name}\n"
                response += "\n"
        
        response += "💡 Tip: Ask about a specific professor for detailed information!\n"
        return response
    
    def _format_structured_response(self, query, results):
        """Format response based on query type and results."""
        if not results:
            return self._format_help_message()
        
        category = results[0]['category']
        
        # Format based on category
        if category == 'achievements':
            return self._format_achievements(results)
        elif category == 'placements':
            return self._format_placements(results)
        elif category == 'admissions':
            return self._format_admissions(results)
        elif category == 'research':
            return self._format_research(results)
        elif category == 'events':
            return self._format_events(results)
        elif category == 'contact':
            return self._format_contact(results)
        else:
            # Default formatting
            return self._format_default(results)
    
    def _format_achievements(self, results):
        """Format student achievements."""
        response = "\n🏆 STUDENT ACHIEVEMENTS\n" + "="*50 + "\n\n"
        
        for i, result in enumerate(results[:5], 1):
            data = result['data']
            response += f"{i}. "
            if 'student' in data:
                response += f"{data['student']}\n"
            if 'achievement' in data:
                response += f"   ✓ {data['achievement']}\n"
            if 'event' in data:
                response += f"   📅 {data['event']}\n"
            if 'company' in data:
                response += f"   🏢 {data['company']}\n"
            if 'rank' in data:
                response += f"   🎖️ {data['rank']}\n"
            response += "\n"
        
        return response
    
    def _format_placements(self, results):
        """Format placement information."""
        response = "\n💼 PLACEMENT INFORMATION\n" + "="*50 + "\n\n"
        
        if results and 'data' in results[0]:
            pl = results[0]['data']
            if 'overview' in pl:
                response += f"📋 Overview:\n{pl['overview']}\n\n"
            
            if 'highlights' in pl:
                response += "✨ Highlights:\n"
                for highlight in pl['highlights']:
                    response += f"   • {highlight}\n"
                response += "\n"
            
            if 'internships' in pl:
                response += "🎓 Internship Opportunities:\n"
                for intern in pl['internships'][:5]:
                    response += f"   • {intern}\n"
        
        return response
    
    def _format_admissions(self, results):
        """Format admission information."""
        response = "\n📝 ADMISSION INFORMATION\n" + "="*50 + "\n\n"
        
        for result in results[:3]:
            data = result['data']
            if 'name' in data:
                response += f"🎓 Program: {data['name']}\n"
            if 'duration' in data:
                response += f"   ⏱️ Duration: {data['duration']}\n"
            if 'seats' in data:
                response += f"   💺 Seats: {data['seats']}\n"
            if 'entrance_exam' in data:
                response += f"   📋 Entrance Exam: {data['entrance_exam']}\n"
            if 'counseling' in data:
                response += f"   🎯 Counseling: {data['counseling']}\n"
            response += "\n"
        
        return response
    
    def _format_research(self, results):
        """Format research projects."""
        response = "\n🔬 RESEARCH PROJECTS\n" + "="*50 + "\n\n"
        
        for i, result in enumerate(results[:5], 1):
            data = result['data']
            response += f"{i}. {data.get('title', 'Project')}\n"
            response += f"   💰 Funding: {data.get('amount', 'N/A')}\n"
            response += f"   🏛️ Sponsor: {data.get('sponsor', 'N/A')}\n"
            response += f"   🔬 Area: {data.get('area', 'N/A')}\n\n"
        
        return response
    
    def _format_events(self, results):
        """Format events."""
        response = "\n📅 EVENTS AT IIIT KALYANI\n" + "="*50 + "\n\n"
        
        for i, result in enumerate(results[:6], 1):
            data = result['data']
            response += f"{i}. {data.get('name', 'Event')}\n"
            if 'date' in data:
                response += f"   📆 {data['date']}\n"
            if 'type' in data:
                response += f"   🎭 Type: {data['type']}\n"
            if 'description' in data:
                response += f"   📝 {data['description']}\n"
            response += "\n"
        
        return response
    
    def _format_contact(self, results):
        """Format contact information."""
        response = "\n📞 CONTACT INFORMATION\n" + "="*50 + "\n\n"
        
        if results and 'data' in results[0]:
            contact = results[0]['data']
            response += f"🏢 Address:\n   {contact.get('address', 'N/A')}\n\n"
            response += f"📞 Phone: {contact.get('phone', 'N/A')}\n"
            response += f"📧 Email: {contact.get('email', 'N/A')}\n"
            response += f"👤 Director: {contact.get('director_email', 'N/A')}\n"
        
        return response
    
    def _format_default(self, results):
        """Default formatting."""
        response = "\n📚 INFORMATION\n" + "="*50 + "\n\n"
        
        for result in results[:3]:
            if 'data' in result:
                data = result['data']
                for key, value in data.items():
                    if isinstance(value, str) and len(value) < 200:
                        response += f"{key.replace('_', ' ').title()}: {value}\n"
                response += "\n"
        
        return response
    
    def _format_greeting(self):
        """Format greeting message."""
        return ("\n👋 Hello! Welcome to IIIT Kalyani Chatbot!\n" + "="*50 + "\n\n"
                "I can help you with:\n"
                "   👨‍🏫 Faculty information\n"
                "   🎓 Admissions and Programs\n"
                "   🏆 Student achievements\n"
                "   💼 Placements\n"
                "   🔬 Research projects\n"
                "   📅 Events\n"
                "   📞 Contact details\n"
                "   💰 Fee structure\n\n"
                "What would you like to know?")
    
    def _format_help_message(self):
        """Format help message."""
        return ("\n💡 I can help you with IIIT Kalyani information!\n\n"
                "Try asking:\n"
                "   • 'Tell me about Dr. Anirban Lakshman'\n"
                "   • 'Show me CSE faculty'\n"
                "   • 'What are the admission requirements?'\n"
                "   • 'Tell me about placements'\n"
                "   • 'Show student achievements'\n"
                "   • 'What research projects are there?'\n")


if __name__ == "__main__":
    chatbot = StructuredCollegeChatbot()
    
    # Test queries
    test_queries = [
        "Tell me about Dr. Anirban Lakshman",
        "Who is the director?",
        "Show me faculty members",
        "What are student achievements?"
    ]
    
    for query in test_queries:
        print(f"\n{'='*70}")
        print(f"Q: {query}")
        print(chatbot.get_response(query))

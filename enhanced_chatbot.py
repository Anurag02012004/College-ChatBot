"""
Enhanced College Chatbot with Comprehensive Data
Uses all collected data from the website including faculty, placements, events, etc.
"""

import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os


class EnhancedCollegeChatbot:
    """Enhanced chatbot with comprehensive college information."""
    
    def __init__(self):
        """Initialize the chatbot with comprehensive data."""
        print("Initializing Enhanced College Chatbot...")
        
        # Try to load comprehensive data first, fall back to basic data
        if os.path.exists('comprehensive_college_data.json'):
            print("Loading comprehensive data...")
            with open('comprehensive_college_data.json', 'r', encoding='utf-8') as f:
                self.comprehensive_data = json.load(f)
            self.data_source = 'comprehensive'
        else:
            print("Comprehensive data not found, using basic data...")
            self.comprehensive_data = {}
            self.data_source = 'basic'
        
        # Load basic college data
        with open('college_data.json', 'r', encoding='utf-8') as f:
            self.basic_data = json.load(f)
        
        # Initialize sentence transformer model
        print("Loading language model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Prepare enhanced knowledge base
        self.knowledge_base = self._prepare_enhanced_knowledge_base()
        
        # Generate embeddings
        print("Generating embeddings for knowledge base...")
        self.embeddings = self._generate_embeddings()
        
        print(f"✅ Chatbot initialized with {len(self.knowledge_base)} knowledge items!")
        if self.data_source == 'comprehensive':
            print("✅ Using comprehensive data with faculty, placements, and detailed information!")
    
    def _prepare_enhanced_knowledge_base(self):
        """Create comprehensive knowledge base with all data."""
        knowledge = []
        
        # Add all basic data (existing functionality)
        knowledge.extend(self._add_basic_data())
        
        # Add comprehensive data if available
        if self.data_source == 'comprehensive':
            knowledge.extend(self._add_comprehensive_data())
        
        return knowledge
    
    def _add_basic_data(self):
        """Add basic college data."""
        knowledge = []
        data = self.basic_data
        
        # Basic info
        info = data['college_info']
        knowledge.append({
            'text': f"The college name is {info['name']}, also known as {info['short_name']}. "
                   f"It is located in {info['location']}. Established in {info['established']}. "
                   f"It is an {info['type']}. Motto: {info['motto']}. Website: {info['website']}",
            'category': 'basic_info'
        })
        
        # About
        about = data['about']
        knowledge.append({
            'text': f"About IIIT Kalyani: {about['description']} Vision: {about['vision']} "
                   f"Mission: {about['mission']}",
            'category': 'about'
        })
        
        # Departments
        for dept in data['departments']:
            knowledge.append({
                'text': f"Department: {dept['name']}. Programs: {', '.join(dept['programs'])}. "
                       f"Specializations: {', '.join(dept['specializations'])}",
                'category': 'departments'
            })
        
        # Programs
        for ug in data['programs']['undergraduate']:
            knowledge.append({
                'text': f"B.Tech program: {ug['name']}. Duration: {ug['duration']}. "
                       f"Seats: {ug['seats']}. Admission through: {ug['admission']}",
                'category': 'programs'
            })
        
        for pg in data['programs']['postgraduate']:
            knowledge.append({
                'text': f"M.Tech program: {pg['name']}. Duration: {pg['duration']}. "
                       f"Admission: {pg['admission']}",
                'category': 'programs'
            })
        
        # Contact
        contact = data['contact_info']
        knowledge.append({
            'text': f"Contact: Address: {contact['address']}. Phone: {contact['phone']}. "
                   f"Email: {contact['email']}. Director Email: {contact['director_email']}",
            'category': 'contact'
        })
        
        return knowledge
    
    def _add_comprehensive_data(self):
        """Add comprehensive data from enhanced scraper."""
        knowledge = []
        data = self.comprehensive_data
        
        # Faculty information
        if 'faculty' in data and data['faculty']:
            faculty_data = data['faculty']
            if 'known_faculty' in faculty_data:
                for faculty in faculty_data['known_faculty']:
                    text = f"Faculty: {faculty.get('name', 'Unknown')}. "
                    if 'department' in faculty:
                        text += f"Department: {faculty['department']}. "
                    if 'specialization' in faculty:
                        text += f"Specialization: {faculty['specialization']}. "
                    if 'affiliation' in faculty:
                        text += f"Affiliation: {faculty['affiliation']}."
                    knowledge.append({'text': text, 'category': 'faculty'})
        
        # Director information
        if 'director' in data and data['director']:
            dir_info = data['director']
            text = f"Director information: {dir_info.get('name', 'Director of IIIT Kalyani')}. "
            text += f"Previous position: {dir_info.get('previous_position', 'Professor at IIT')}. "
            if dir_info.get('message'):
                text += f"Message: {dir_info['message'][:200]}"
            knowledge.append({'text': text, 'category': 'director'})
        
        # Detailed events
        if 'events_detailed' in data and data['events_detailed']:
            for event in data['events_detailed']:
                text = f"Event: {event.get('name', 'Event')}. "
                if 'date' in event:
                    text += f"Date: {event['date']}. "
                if 'type' in event:
                    text += f"Type: {event['type']}. "
                if 'description' in event:
                    text += f"Description: {event['description']}. "
                if 'sponsor' in event:
                    text += f"Sponsored by: {event['sponsor']}."
                knowledge.append({'text': text, 'category': 'events'})
        
        # Student achievements (detailed)
        if 'achievements_detailed' in data and data['achievements_detailed']:
            for ach in data['achievements_detailed'][:30]:  # Top 30 achievements
                text = ""
                if 'student' in ach:
                    text += f"Student: {ach['student']}. "
                if 'achievement' in ach:
                    text += f"Achievement: {ach['achievement']}. "
                if 'event' in ach:
                    text += f"Event: {ach['event']}. "
                if 'paper' in ach:
                    text += f"Paper: {ach['paper']}. "
                if 'company' in ach:
                    text += f"Company: {ach['company']}. "
                if 'rank' in ach:
                    text += f"Rank: {ach['rank']}."
                if 'supervisor' in ach:
                    text += f"Supervisor: {ach['supervisor']}."
                if text:
                    knowledge.append({'text': text, 'category': 'achievements'})
        
        # Placement details
        if 'placements_detailed' in data and data['placements_detailed']:
            pl_data = data['placements_detailed']
            text = f"Placements at IIIT Kalyani: {pl_data.get('overview', '')}. "
            if 'highlights' in pl_data:
                text += "Highlights: " + ". ".join(pl_data['highlights'][:3])
            knowledge.append({'text': text, 'category': 'placements'})
            
            if 'internships' in pl_data:
                text = "Internship opportunities: " + ", ".join(pl_data['internships'])
                knowledge.append({'text': text, 'category': 'placements'})
        
        # Detailed admission information
        if 'admissions_detailed' in data and data['admissions_detailed']:
            adm_data = data['admissions_detailed']
            
            # UG admissions
            if 'undergraduate' in adm_data:
                ug_adm = adm_data['undergraduate']
                if 'programs' in ug_adm:
                    for prog in ug_adm['programs']:
                        text = f"B.Tech Admission: {prog.get('name', '')}. "
                        text += f"Seats: {prog.get('seats', 'N/A')}. "
                        text += f"Entrance: {prog.get('entrance_exam', 'JEE Main')}. "
                        text += f"Counseling: {prog.get('counseling', 'JoSAA')}. "
                        if 'process' in prog:
                            text += "Process: " + ", ".join(prog['process'][:3])
                        knowledge.append({'text': text, 'category': 'admissions'})
            
            # PG admissions
            if 'postgraduate' in adm_data:
                pg_adm = adm_data['postgraduate']
                if 'programs' in pg_adm:
                    for prog in pg_adm['programs']:
                        text = f"M.Tech Admission: {prog.get('name', '')}. "
                        text += f"Duration: {prog.get('duration', '2 years')}. "
                        if 'admission_modes' in prog:
                            text += "Admission modes: " + ", ".join(prog['admission_modes'])
                        knowledge.append({'text': text, 'category': 'admissions'})
            
            # PhD admissions
            if 'phd' in adm_data:
                phd_adm = adm_data['phd']
                text = "PhD Admission: Available in " + ", ".join(phd_adm.get('areas', []))
                text += f". Sessions: {', '.join(phd_adm.get('sessions', []))}. "
                if 'admission_process' in phd_adm:
                    text += "Process: " + ", ".join(phd_adm['admission_process'])
                knowledge.append({'text': text, 'category': 'admissions'})
            
            # Fee structure
            if 'fee_structure' in adm_data:
                fees = adm_data['fee_structure']
                if 'btech' in fees:
                    text = f"B.Tech Fee Structure: Tuition per semester: {fees['btech'].get('tuition_per_semester', 'N/A')}. "
                    text += f"Total annual (including hostel): {fees['btech'].get('total_annual', 'N/A')}"
                    knowledge.append({'text': text, 'category': 'fees'})
            
            # Scholarships
            if 'scholarships' in adm_data:
                text = "Scholarships available at IIIT Kalyani: " + ", ".join(adm_data['scholarships'][:5])
                knowledge.append({'text': text, 'category': 'scholarships'})
        
        # Research projects
        if 'research_projects' in data and data['research_projects']:
            res_data = data['research_projects']
            if 'projects' in res_data:
                for proj in res_data['projects'][:10]:  # Top 10 projects
                    text = f"Research Project: {proj.get('title', '')}. "
                    text += f"Sponsor: {proj.get('sponsor', '')}. "
                    text += f"Funding: {proj.get('amount', '')}. "
                    text += f"Area: {proj.get('area', '')}"
                    knowledge.append({'text': text, 'category': 'research'})
            
            if 'total_funding' in res_data:
                text = f"Total research funding: {res_data['total_funding']} across {res_data.get('total_projects', 0)} projects"
                knowledge.append({'text': text, 'category': 'research'})
        
        # Detailed departments
        if 'departments_detailed' in data and data['departments_detailed']:
            for dept in data['departments_detailed']:
                text = f"Department: {dept.get('name', '')}. "
                text += f"Programs: {', '.join(dept.get('programs', []))}. "
                text += f"Specializations: {', '.join(dept.get('specializations', [])[:5])}. "
                if 'labs' in dept:
                    text += f"Labs: {', '.join(dept['labs'])}. "
                if 'faculty_count' in dept:
                    text += f"Faculty: {dept['faculty_count']}. "
                if 'student_strength' in dept:
                    text += f"Students: {dept['student_strength']}"
                knowledge.append({'text': text, 'category': 'departments'})
        
        return knowledge
    
    def _generate_embeddings(self):
        """Generate embeddings for all knowledge items."""
        texts = [item['text'] for item in self.knowledge_base]
        return self.model.encode(texts)
    
    def get_response(self, query, top_k=3):
        """Get response for user query."""
        # Handle greetings
        greetings = ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
        if any(greet in query.lower() for greet in greetings):
            return ("Hello! I'm the IIIT Kalyani chatbot with comprehensive information. "
                   "I can tell you about admissions, faculty, placements, student achievements, "
                   "research projects, events, departments, and much more. What would you like to know?")
        
        # Handle thanks
        thanks = ['thank', 'thanks', 'appreciate']
        if any(thank in query.lower() for thank in thanks):
            return "You're welcome! Feel free to ask anything else about IIIT Kalyani!"
        
        # Generate query embedding
        query_embedding = self.model.encode([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Get top k most similar items
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Check similarity threshold
        if similarities[top_indices[0]] < 0.2:
            return ("I have comprehensive information about IIIT Kalyani including admissions, "
                   "programs, faculty members, student achievements, placements, research projects, "
                   "events, fees, scholarships, and contact details. Please ask me something specific!")
        
        # Get relevant texts
        relevant_texts = [self.knowledge_base[i]['text'] for i in top_indices]
        
        # Generate response
        response = self._generate_answer(query, relevant_texts)
        
        return response
    
    def _generate_answer(self, query, relevant_texts):
        """Generate coherent answer from relevant texts."""
        # Combine relevant information
        combined_info = " ".join(relevant_texts)
        
        # Remove duplicate sentences
        sentences = combined_info.split('. ')
        unique_sentences = []
        seen = set()
        
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and sentence.lower() not in seen and len(sentence) > 10:
                unique_sentences.append(sentence)
                seen.add(sentence.lower())
        
        response = '. '.join(unique_sentences[:6])  # Up to 6 sentences for comprehensive answers
        
        if not response.endswith('.'):
            response += '.'
        
        return response


if __name__ == "__main__":
    # Test the enhanced chatbot
    chatbot = EnhancedCollegeChatbot()
    
    print("\n" + "="*70)
    print("Enhanced College Chatbot - Test Mode")
    print("="*70)
    
    test_queries = [
        "Who are the faculty members?",
        "Tell me about student achievements",
        "What are the placement details?",
        "Tell me about research projects",
        "What events happen at IIIT Kalyani?"
    ]
    
    for query in test_queries:
        print(f"\nQ: {query}")
        response = chatbot.get_response(query)
        print(f"A: {response}\n")
        print("-" * 70)

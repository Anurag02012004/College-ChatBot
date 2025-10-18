"""
College Chatbot - Simple LLM Model
This module implements a retrieval-based chatbot using sentence embeddings
and cosine similarity to answer questions about IIIT Kalyani.
"""

import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re


class CollegeChatbot:
    """
    A simple LLM-based chatbot for college information retrieval.
    Uses sentence transformers for semantic understanding.
    """
    
    def __init__(self, data_file='college_data.json'):
        """Initialize the chatbot with college data and model."""
        print("Initializing College Chatbot...")
        
        # Load college data
        with open(data_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        # Initialize sentence transformer model
        print("Loading language model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Prepare knowledge base
        self.knowledge_base = self._prepare_knowledge_base()
        
        # Generate embeddings for all knowledge items
        print("Generating embeddings for knowledge base...")
        self.embeddings = self._generate_embeddings()
        
        print("Chatbot initialized successfully!")
    
    def _prepare_knowledge_base(self):
        """Convert JSON data into searchable text chunks."""
        knowledge = []
        
        # Basic college info
        info = self.data['college_info']
        knowledge.append({
            'text': f"The college name is {info['name']}, also known as {info['short_name']}. "
                   f"It is located in {info['location']}. The college was established in {info['established']}. "
                   f"It is an {info['type']}. The motto is {info['motto']}. "
                   f"Website: {info['website']}",
            'category': 'basic_info'
        })
        
        # About
        about = self.data['about']
        knowledge.append({
            'text': f"About IIIT Kalyani: {about['description']} "
                   f"Vision: {about['vision']} Mission: {about['mission']}",
            'category': 'about'
        })
        
        # Departments
        for dept in self.data['departments']:
            knowledge.append({
                'text': f"Department: {dept['name']}. Programs offered: {', '.join(dept['programs'])}. "
                       f"Specializations: {', '.join(dept['specializations'])}",
                'category': 'departments'
            })
        
        # Programs
        for ug in self.data['programs']['undergraduate']:
            knowledge.append({
                'text': f"Undergraduate program: {ug['name']}. Duration: {ug['duration']}. "
                       f"Number of seats: {ug['seats']}. Admission through: {ug['admission']}",
                'category': 'programs'
            })
        
        for pg in self.data['programs']['postgraduate']:
            knowledge.append({
                'text': f"Postgraduate program: {pg['name']}. Duration: {pg['duration']}. "
                       f"Admission: {pg['admission']}",
                'category': 'programs'
            })
        
        for phd in self.data['programs']['doctoral']:
            knowledge.append({
                'text': f"PhD program: {phd['name']}. Admission: {phd['admission']}",
                'category': 'programs'
            })
        
        # Research facilities
        for facility in self.data['research_facilities']:
            knowledge.append({
                'text': f"Research Facility: {facility['name']}. {facility['description']}",
                'category': 'research'
            })
        
        # Projects
        for project in self.data['sponsored_projects'][:5]:  # Top 5
            knowledge.append({
                'text': f"Sponsored Project: {project['title']}. "
                       f"Sponsored by: {project['sponsor']}. Amount: {project['amount']}",
                'category': 'research'
            })
        
        # Achievements
        achievements_text = "Student Achievements at IIIT Kalyani: " + ". ".join(self.data['achievements'])
        knowledge.append({
            'text': achievements_text,
            'category': 'achievements'
        })
        
        # Events
        events_text = "Recent events at IIIT Kalyani: "
        for event in self.data['events'][:5]:
            events_text += f"{event['name']} "
            if 'month' in event:
                events_text += f"in {event['month']}. "
            if 'description' in event:
                events_text += f"{event['description']}. "
        knowledge.append({
            'text': events_text,
            'category': 'events'
        })
        
        # Placements
        knowledge.append({
            'text': f"Placements: {self.data['placements']['description']}. "
                   f"Portal: {self.data['placements']['portal']}. "
                   f"Companies: {self.data['placements']['companies']}",
            'category': 'placements'
        })
        
        # Admissions
        adm = self.data['admissions']
        knowledge.append({
            'text': f"Undergraduate Admission: Through {adm['undergraduate']['exam']} and "
                   f"{adm['undergraduate']['counseling']} counseling. "
                   f"Process: {adm['undergraduate']['process']}",
            'category': 'admissions'
        })
        
        knowledge.append({
            'text': f"M.Tech VLSI Admission: {adm['postgraduate']['mtech_vlsi']}. "
                   f"Executive M.Tech: {adm['postgraduate']['mtech_executive']}",
            'category': 'admissions'
        })
        
        knowledge.append({
            'text': f"PhD Admission: {adm['phd']['process']}. "
                   f"Sessions: {adm['phd']['sessions']}. Fellowship: {adm['phd']['fellowship']}",
            'category': 'admissions'
        })
        
        # Facilities
        facilities_text = "Facilities at IIIT Kalyani: " + ", ".join(self.data['facilities'])
        knowledge.append({
            'text': facilities_text,
            'category': 'facilities'
        })
        
        # Scholarships
        scholarships_text = "Scholarships available: " + ", ".join(self.data['scholarships'])
        knowledge.append({
            'text': scholarships_text,
            'category': 'scholarships'
        })
        
        # Fee structure
        fee = self.data['fee_structure']
        knowledge.append({
            'text': f"B.Tech Fee Structure: Tuition fee is {fee['btech']['tuition_fee']}. "
                   f"{fee['btech']['hostel']}. {fee['btech']['other']}",
            'category': 'fees'
        })
        
        # Contact
        contact = self.data['contact_info']
        knowledge.append({
            'text': f"Contact Information: Address: {contact['address']}. "
                   f"Phone: {contact['phone']}. Email: {contact['email']}. "
                   f"Director Email: {contact['director_email']}",
            'category': 'contact'
        })
        
        return knowledge
    
    def _generate_embeddings(self):
        """Generate embeddings for all knowledge base items."""
        texts = [item['text'] for item in self.knowledge_base]
        return self.model.encode(texts)
    
    def get_response(self, query, top_k=3):
        """
        Get response for a user query.
        
        Args:
            query: User's question
            top_k: Number of top similar documents to consider
            
        Returns:
            Response string
        """
        # Handle greetings
        greetings = ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
        if any(greet in query.lower() for greet in greetings):
            return ("Hello! I'm the IIIT Kalyani chatbot. I can help you with information about "
                   "our college including admissions, programs, facilities, placements, events, "
                   "research, and more. What would you like to know?")
        
        # Handle thanks
        thanks = ['thank', 'thanks', 'appreciate']
        if any(thank in query.lower() for thank in thanks):
            return "You're welcome! Feel free to ask if you have any other questions about IIIT Kalyani."
        
        # Generate query embedding
        query_embedding = self.model.encode([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Get top k most similar items
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Check if similarity is too low
        if similarities[top_indices[0]] < 0.2:
            return ("I'm not sure about that. I can help you with information about IIIT Kalyani's "
                   "admissions, programs, departments, facilities, placements, research, events, "
                   "scholarships, fees, and contact information. Please ask me something related to these topics.")
        
        # Combine top results
        relevant_texts = [self.knowledge_base[i]['text'] for i in top_indices]
        
        # Generate response
        response = self._generate_answer(query, relevant_texts)
        
        return response
    
    def _generate_answer(self, query, relevant_texts):
        """Generate a coherent answer from relevant texts."""
        # Simple response generation - combine relevant information
        # For a production system, you'd use a generative model here
        
        # Combine unique information
        combined_info = " ".join(relevant_texts)
        
        # Remove duplicate sentences
        sentences = combined_info.split('. ')
        unique_sentences = []
        seen = set()
        
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and sentence.lower() not in seen:
                unique_sentences.append(sentence)
                seen.add(sentence.lower())
        
        response = '. '.join(unique_sentences[:5])  # Limit to 5 sentences
        
        if not response.endswith('.'):
            response += '.'
        
        return response
    
    def chat(self):
        """Interactive chat loop for testing."""
        print("\n" + "="*60)
        print("College Chatbot - IIIT Kalyani")
        print("="*60)
        print("Ask me anything about IIIT Kalyani!")
        print("Type 'quit' or 'exit' to end the conversation.")
        print("="*60 + "\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("Chatbot: Goodbye! Have a great day!")
                break
            
            response = self.get_response(user_input)
            print(f"\nChatbot: {response}\n")


if __name__ == "__main__":
    # Test the chatbot
    chatbot = CollegeChatbot()
    chatbot.chat()

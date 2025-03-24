from django.shortcuts import render, redirect
from .forms import ContactForm

# Sample technology data (You can later fetch this from a database)
TECHNOLOGY_DATA = {
    "groot_n1": {
        "title": "Groot N1",
        "image": "technology/images/groot_n1.jpg",
        "description": "An advanced AI model with real-time decision-making capabilities.",
        "inventor": "AI Labs",
        "purpose": "To enhance AI-driven automation and decision-making.",
        "usage": "Used in robotics, self-learning systems, and automation."
    },
    "ai_model_x": {
        "title": "AI Model X",
        "image": "technology/images/ai_model.jpg",
        "description": "A next-gen deep learning AI with self-learning features.",
        "inventor": "Tech Innovators",
        "purpose": "Improving AI adaptability in different domains.",
        "usage": "Used in finance, healthcare, and smart assistants."
    },
    "neural_brain": {
        "title": "Neural Brain AI",
        "image": "technology/images/neural_brain.jpg",
        "description": "A neural network-based AI designed to mimic human cognitive functions.",
        "inventor": "NeuroTech AI",
        "purpose": "To enhance deep learning models for medical research and AI-driven neuroscience.",
        "usage": "Used in neuroscience research, deep learning applications, and brain-computer interfaces."
    },
    "vision_ai": {
        "title": "Vision AI",
        "image": "technology/images/vision_ai.jpg",
        "description": "An advanced AI for real-time image and video analysis.",
        "inventor": "VisionTech",
        "purpose": "To improve AI-based image processing and recognition.",
        "usage": "Used in self-driving cars, medical imaging, and surveillance systems."
    },
    "voice_assistant": {
        "title": "Voice Assistant AI",
        "image": "technology/images/voice_assistant.jpg",
        "description": "An intelligent voice assistant that understands natural language.",
        "inventor": "Smart AI Corp",
        "purpose": "To enhance human-computer interaction using voice recognition.",
        "usage": "Used in smart speakers, customer service, and accessibility applications."
    },
    "quantum_ai": {
        "title": "Quantum AI",
        "image": "technology/images/quantum_ai.jpg",
        "description": "AI-powered by quantum computing for ultra-fast processing.",
        "inventor": "Quantum Innovations",
        "purpose": "To revolutionize AI problem-solving using quantum mechanics.",
        "usage": "Used in cryptography, complex simulations, and optimization problems."
    },
    "nlp_ai": {
        "title": "NLP AI",
        "image": "technology/images/nlp_ai.jpg",
        "description": "An AI model specialized in natural language processing tasks.",
        "inventor": "Linguistic AI Labs",
        "purpose": "To enhance language understanding and automated text generation.",
        "usage": "Used in chatbots, translation services, and sentiment analysis."
    },
    "self_driving": {
        "title": "Self-Driving AI",
        "image": "technology/images/self_driving.jpg",
        "description": "An autonomous AI system for self-driving vehicles.",
        "inventor": "AutoDrive AI",
        "purpose": "To make transportation safer and more efficient.",
        "usage": "Used in autonomous vehicles, delivery robots, and traffic management."
    },
    "ai_robot": {
        "title": "AI Robot",
        "image": "technology/images/ai_robot.jpg",
        "description": "An AI-powered robot designed for various automation tasks.",
        "inventor": "Robotics AI Co.",
        "purpose": "To assist in industrial automation and personal assistance.",
        "usage": "Used in factories, healthcare, and household robotics."
    },
    "cybersecurity_ai": {
        "title": "Cybersecurity AI",
        "image": "technology/images/cybersecurity_ai.jpg",
        "description": "AI technology for detecting and preventing cyber threats.",
        "inventor": "CyberSec AI",
        "purpose": "To enhance digital security and threat detection.",
        "usage": "Used in network security, fraud detection, and cyber threat analysis."
    }
}

def welcome(request):
    return render(request, 'technology/welcome.html')

def home(request):
    return render(request, 'technology/home.html', {'technologies': TECHNOLOGY_DATA})

def new_technology(request):
    return render(request, 'technology/new_technology.html')

def contact(request):
    return render(request, 'technology/contact.html')

def technology_detail(request, tech_name):
    tech_info = TECHNOLOGY_DATA.get(tech_name, None)
    if tech_info:
        return render(request, 'technology/technology_detail.html', {'tech': tech_info})
    else:
        return render(request, 'technology/not_found.html', status=404)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('contact')  # Redirect to the contact page after submission
    else:
        form = ContactForm()

    return render(request, 'technology/contact.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ContactForm
from django.contrib import messages
from .forms import SignupForm


# Sample technology data (You can later fetch this from a database)
TECHNOLOGY_DATA = {
    "groot_n1": {
        "title": "Groot N1",
        "image": "technology/images/groot_n1.jpg",
        "description": "An advanced AI model with real-time decision-making capabilities.",
        "inventor": "AI Labs",
        "purpose": "To enhance AI-driven automation and decision-making.",
        "usage": "Used in robotics, self-learning systems, and automation.",
        "video":"https://www.youtube.com/watch?v=m1CH-mgpdYg"
    },
    "ai_model_x": {
        "title": "AI Model X",
        "image": "technology/images/ai_model.jpg",
        "description": "A next-gen deep learning AI with self-learning features.",
        "inventor": "Tech Innovators",
        "purpose": "Improving AI adaptability in different domains.",
        "usage": "Used in finance, healthcare, and smart assistants.",
        "video":"https://www.youtube.com/watch?v=U9d0p96N1iw"
    },
    "neural_brain": {
        "title": "Neural Brain AI",
        "image": "technology/images/neural_brain.jpg",
        "description": "A neural network-based AI designed to mimic human cognitive functions.",
        "inventor": "NeuroTech AI",
        "purpose": "To enhance deep learning models for medical research and AI-driven neuroscience.",
        "usage": "Used in neuroscience research, deep learning applications, and brain-computer interfaces.",
        "video":"https://www.youtube.com/watch?v=Ay3_D7VgzZs"
    },
    "vision_ai": {
        "title": "Vision AI",
        "image": "technology/images/vision_ai.jpg",
        "description": "An advanced AI for real-time image and video analysis.",
        "inventor": "VisionTech",
        "purpose": "To improve AI-based image processing and recognition.",
        "usage": "Used in self-driving cars, medical imaging, and surveillance systems.",
        "video":"https://www.youtube.com/watch?v=nvmV0a2geaQ"
    },
    "voice_assistant": {
        "title": "Voice Assistant AI",
        "image": "technology/images/voice_assistant.jpg",
        "description": "An intelligent voice assistant that understands natural language.",
        "inventor": "Smart AI Corp",
        "purpose": "To enhance human-computer interaction using voice recognition.",
        "usage": "Used in smart speakers, customer service, and accessibility applications.",
        "video":"https://www.youtube.com/watch?v=m1CH-mgpdYg"
    },
    "quantum_ai": {
        "title": "Quantum AI",
        "image": "technology/images/quantum_ai.jpg",
        "description": "AI-powered by quantum computing for ultra-fast processing.",
        "inventor": "Quantum Innovations",
        "purpose": "To revolutionize AI problem-solving using quantum mechanics.",
        "usage": "Used in cryptography, complex simulations, and optimization problems.",
        "video":"https://www.youtube.com/watch?v=v3BP_9gyOqQ"
    },
    "nlp_ai": {
        "title": "NLP AI",
        "image": "technology/images/nlp_ai.jpg",
        "description": "An AI model specialized in natural language processing tasks.",
        "inventor": "Linguistic AI Labs",
        "purpose": "To enhance language understanding and automated text generation.",
        "usage": "Used in chatbots, translation services, and sentiment analysis.",
        "video":"https://www.youtube.com/watch?v=fLvJ8VdHLA0"
    },    
    "self_driving": {
        "title": "Self-Driving AI",
        "image": "technology/images/self_driving.jpg",
        "description": "An autonomous AI system for self-driving vehicles.",
        "inventor": "AutoDrive AI",
        "purpose": "To make transportation safer and more efficient.",
        "usage": "Used in autonomous vehicles, delivery robots, and traffic management.",
        "video":"https://www.youtube.com/watch?v=-D2KC1WSgj8"
    },
    "ai_robot": {
        "title": "AI Robot",
        "image": "technology/images/ai_robot.jpg",
        "description": "An AI-powered robot designed for various automation tasks.",
        "inventor": "Robotics AI Co.",
        "purpose": "To assist in industrial automation and personal assistance.",
        "usage": "Used in factories, healthcare, and household robotics.",
        "video":"https://www.youtube.com/watch?v=eRXxUlGSHjk"
    },
    "cybersecurity_ai": {
        "title": "Cybersecurity AI",
        "image": "technology/images/cybersecurity_ai.jpg",
        "description": "AI technology for detecting and preventing cyber threats.",
        "inventor": "CyberSec AI",
        "purpose": "To enhance digital security and threat detection.",
        "usage": "Used in network security, fraud detection, and cyber threat analysis.",
        "video":"https://www.youtube.com/watch?v=kqaMIFEz15s"
    }
    # Add more AI technologies here...
}

def welcome(request):
    return render(request, 'technology/welcome.html')
def user_login(request):
    return render(request, 'technology/login.html')  # Update path if needed

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
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'technology/contact.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful signup
            messages.success(request, "Account created successfully!")
            return redirect('home')  # Redirect to home page
        else:
            messages.error(request, "Signup failed! Please check the details.")
    else:
        form = SignupForm()

    return render(request, 'technology/signup.html', {'form': form})
def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if user exists by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'technology/login.html', {'error': 'Invalid email or password'})

        # Authenticate using username (Django default)
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return render(request, 'technology/login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'technology/login.html')
from flask import Flask, render_template, send_file, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Personal information
personal_info = {
    'name': 'Sathwik Shenoy',
    'title': 'Machine Learning & Full-Stack Developer',
    'description': 'Passionate about building innovative solutions with expertise in machine learning, web development, and Python applications. Specializing in privacy-preserving AI and interactive web experiences.',
    'email': 'sathwikshenoy907@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/sathwik-shenoy-b278551b7/',
    'instagram': 'https://www.instagram.com/sathwik_shenoy/',
    'github': 'https://github.com/Sathwik-Shenoy',
    'profile_photo': 'images/profile/profile.jpeg'
}

# Skills organized by category
skills = {
    'Programming Languages': ['Python', 'JavaScript', 'Java', 'C++', 'SQL'],
    'Machine Learning': ['PyTorch', 'scikit-learn', 'TensorFlow', 'PySyft', 'Pandas', 'NumPy'],
    'Web Development': ['Flask', 'Django', 'React', 'HTML/CSS', 'RESTful APIs', 'WebSockets'],
    'Databases': ['PostgreSQL', 'MySQL', 'MongoDB', 'Redis'],
    'DevOps & Tools': ['Docker', 'Git', 'AWS', 'Nginx', 'Celery', 'JWT'],
    'Other': ['Data Analysis', 'System Design', 'Federated Learning', 'Edge Computing']
}

# Work Experience
experience = [
    {
        'title': 'Research Intern',
        'company': 'Bhabha Atomic Research Centre (BARC)',
        'duration': '2024',
        'description': 'Conducted cutting-edge research in nuclear science and technology at India\'s premier atomic research facility. Worked on advanced computational models and data analysis for nuclear applications.',
        'achievements': [
            'Developed computational models for nuclear physics simulations',
            'Collaborated with senior researchers on classified projects',
            'Published research findings in internal technical reports',
            'Gained expertise in high-performance computing and scientific programming'
        ]
    },
    {
        'title': 'Machine Learning Developer',
        'company': 'Personal Projects',
        'duration': '2023 - Present',
        'description': 'Developed privacy-preserving federated learning systems and full-stack web applications. Specialized in PyTorch implementations and Flask-based platforms.',
        'achievements': [
            'Built federated learning framework achieving 93% accuracy',
            'Developed scalable web applications serving various users',
            'Implemented real-time ML systems with <500ms response times'
        ]
    }
]

# Sample projects
projects = [
    {
        'title': 'FairwayFund SaaS',
        'description': 'Investor-ready SaaS where subscribers track golf scores, enter draws, and fund real charity impact through every subscription.',
        'image': 'images/projects/golf-charity-saas.svg',
        'github_link': 'https://github.com/Sathwik-Shenoy/golf-charity-saas',
        'technologies': ['Next.js 14', 'TypeScript', 'Supabase', 'Stripe', 'Tailwind CSS', 'Framer Motion']
    },
    {
        'title': 'P2P Watch Party (Video Streaming)',
        'description': 'A WebRTC watch-party app that streams host video peer-to-peer with synced playback, low-latency chat, and resilient room signaling.',
        'image': 'images/projects/video-streaming.svg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Video-Streaming',
        'technologies': ['WebRTC', 'Node.js', 'Express', 'Socket.io', 'Vanilla JavaScript', 'Data Channels']
    },
    {
        'title': 'Privacy-Preserving Federated Learning in Social IoT',
        'description': 'Federated learning system for decentralized IoT that trains private models without sharing raw data, reaching 93% edge accuracy.',
        'image': 'images/projects/Federated.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Privacy_FL',
        'technologies': ['PyTorch', 'PySyft', 'Flask', 'WebSockets', 'Edge Computing']
    },
    {
        'title': 'WebRTC Object Detection Demo',
        'description': 'Real-time phone-camera streaming with live object detection overlays, performance metrics, and dual WASM or server inference modes.',
        'image': 'images/projects/object-detection.svg',
        'github_link': 'https://github.com/Sathwik-Shenoy/webrtc-object-detection',
        'technologies': ['WebRTC', 'Node.js', 'ONNX Runtime', 'WASM', 'Docker', 'Real-time Metrics']
    },
    {
        'title': 'Stock Market Alert System',
        'description': 'Real-time stock monitoring platform with rule-based alerts, automated market ingestion, and smart signal-triggered notifications.',
        'image': 'images/projects/stock.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Stock-Market-Alert-System',
        'technologies': ['Python', 'API Integration', 'Real-time Data', 'Automation']
    },
    {
        'title': 'Personal Finance Tracker',
        'description': 'Secure Flask and PostgreSQL finance platform delivering real-time insights, JWT-backed APIs, and faster decision-ready reporting.',
        'image': 'images/projects/finance.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Personal-Finance-Tracker',
        'technologies': ['Python', 'Flask', 'PostgreSQL', 'Docker', 'JWT', 'Bootstrap 5', 'Plotly']
    },
    {
        'title': 'Movie Recommendation System',
        'description': 'Personalized movie recommendation platform using TF-IDF and cosine similarity for fast, real-time suggestion quality.',
        'image': 'images/projects/movie.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Mov-Rec-Website',
        'technologies': ['Python', 'scikit-learn', 'Flask', 'AJAX', 'TF-IDF', 'Pandas']
    },
    {
        'title': 'YouTube Video Download Platform',
        'description': 'Async Flask downloader built for high concurrency with Celery and Redis orchestration, plus automated storage cleanup workflows.',
        'image': 'images/projects/video_downloader.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Video-dowload',
        'technologies': ['Flask', 'Celery', 'Redis', 'yt-dlp', 'Cron Jobs', 'Task Queues']
    },
    {
        'title': 'Portfolio Website',
        'description': 'A modern Flask portfolio with polished UI, smooth interactions, and responsive storytelling for technical work.',
        'image': 'images/projects/portfolio.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Portfolio-Website',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript']
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                         personal_info=personal_info, 
                         projects=projects, 
                         project_count=len(projects),
                         skills=skills, 
                         experience=experience)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you could integrate with email service like SendGrid, SMTP, etc.
        # For now, we'll just simulate success
        
        # Log the contact form submission (in production, save to database or send email)
        print(f"Contact form submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        return redirect(url_for('index') + '#contact')
    
    return redirect(url_for('index'))

@app.route('/download-resume')
def download_resume():
    try:
        return send_file(
            'static/documents/resume.pdf',
            as_attachment=True,
            download_name='Sathwik_Shenoy_Resume.pdf'
        )
    except Exception as e:
        return str(e), 404

if __name__ == '__main__':
    app.run(debug=False)
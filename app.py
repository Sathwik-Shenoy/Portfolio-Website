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
        'title': 'Privacy-Preserving Federated Learning in Social IoT',
        'description': 'Implemented PyTorch-based federated learning for decentralized IoT devices, enabling privacy-focused model training without raw data sharing. Achieved 93% accuracy on edge-based MNIST dataset, with only 5% drop from centralized methods.',
        'image': 'images/projects/Federated.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Privacy_FL',
        'technologies': ['PyTorch', 'PySyft', 'Flask', 'WebSockets', 'Edge Computing']
    },
    {
        'title': 'Stock Market Alert System',
        'description': 'Real-time stock monitoring and alert system that tracks market movements and sends notifications based on user-defined criteria. Features automated data collection and intelligent alert mechanisms.',
        'image': 'images/projects/stock.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Stock-Market-Alert-System',
        'technologies': ['Python', 'API Integration', 'Real-time Data', 'Automation']
    },
    {
        'title': 'Personal Finance Tracker',
        'description': 'Developed secure Flask-PostgreSQL platform for 500+ users, delivering real-time financial insights and reports. Designed dual authentication (sessions/JWT) and RESTful API with 15+ Swagger endpoints, reducing analysis time by 70%.',
        'image': 'images/projects/finance.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Personal-Finance-Tracker',
        'technologies': ['Python', 'Flask', 'PostgreSQL', 'Docker', 'JWT', 'Bootstrap 5', 'Plotly']
    },
    {
        'title': 'Movie Recommendation System',
        'description': 'Created Python/Flask platform with scikit-learn for real-time, personalized movie suggestions. Engineered TF-IDF vectorization on 5,000+ TMDB entries with cosine similarity, hitting 87% accuracy on 200+ test cases under 500ms response.',
        'image': 'images/projects/movie.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Mov-Rec-Website',
        'technologies': ['Python', 'scikit-learn', 'Flask', 'AJAX', 'TF-IDF', 'Pandas']
    },
    {
        'title': 'YouTube Video Download Platform',
        'description': 'Built full-stack Flask app using yt-dlp to manage 200+ concurrent downloads with 95% completion rate. Implemented Celery/Redis for asynchronous tasks and cron jobs for 95% storage efficiency via auto-cleanup.',
        'image': 'images/projects/video_downloader.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Video-dowload',
        'technologies': ['Flask', 'Celery', 'Redis', 'yt-dlp', 'Cron Jobs', 'Task Queues']
    },
    {
        'title': 'Portfolio Website',
        'description': 'A modern, responsive portfolio website built with Flask and modern CSS. Features smooth animations, interactive elements, and optimized performance for showcasing professional work.',
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
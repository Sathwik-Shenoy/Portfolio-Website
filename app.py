from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Personal information
personal_info = {
    'name': 'Sathwik Shenoy',
    'title': 'Machine Learning & Full-Stack Developer',
    'description': 'Passionate about building innovative solutions with expertise in machine learning, web development, and Python applications. Specializing in privacy-preserving AI and interactive web experiences.',
    'email': 'sathwikshenoy907@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/sathwik-shenoy-b278551b7//',
    'instagram': 'https://www.instagram.com/sathwik_shenoy/',
    'github': 'https://github.com/Sathwik-Shenoy',
    'profile_photo': 'images/profile/profile.jpeg'
}

# Sample projects
projects = [
    {
        'title': 'Federated Learning for Privacy Preservation',
        'description': 'A privacy-preserving federated learning framework leveraging functional encryption and Bayesian differential privacy for secure, efficient multiparty data sharing in social IoT environments.',
        'image': 'images/projects/federated.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Privacy_FL',
        'technologies': ['Python', 'Machine Learning', 'Privacy']
    },
    {
        'title': 'Portfolio Website',
        'description': 'A modern portfolio website built with Flask and modern CSS.',
        'image': 'images/projects/portfolio.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Portfolio-Website',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS']
    },
    {
        'title': 'Movie Recommendation System',
        'description': 'A content-based movie recommendation system using machine learning algorithms.',
        'image': 'images/projects/movie.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Mov-Rec-Website',
        'technologies': ['Python', 'Machine Learning', 'Pandas', 'Scikit-learn']
    },
    {
        'title': 'Video Downloader',
        'description': 'A video downloader that allows users to download videos from a given YouTube URL.',
        'image': 'images/projects/video_downloader.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/Video-dowload',
        'technologies': ['Python', 'HTML']
    },
    {
        'title': 'Rock Paper Scissors Game',
        'description': 'A rock paper scissors game that allows users to play against the computer.',
        'image': 'images/projects/rps.jpg',
        'github_link': 'https://github.com/Sathwik-Shenoy/rps',
        'technologies': ['Python']
    }
]

@app.route('/')
def index():
    return render_template('index.html', personal_info=personal_info, projects=projects)

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
    app.run(debug=True) 
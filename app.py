from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Personal information
personal_info = {
    'name': 'Sathwik Shenoy',
    'title': 'Software Developer',
    'email': 'sathwikshenoy907@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/sathwik-shenoy-b278551b7//',
    'instagram': 'https://www.instagram.com/sathwik_shenoy//'
}

# Sample projects
projects = [
    {
        'title': 'Portfolio Website',
        'description': 'A modern portfolio website built with Flask and modern CSS.',
        'image': 'images/projects/portfolio.jpg',
        'github_link': 'https://github.com/yourusername/portfolio',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS']
    },
    {
        'title': 'Portfolio Website',
        'description': 'A modern portfolio website built with Flask and modern CSS.',
        'image': 'images/projects/portfolio.jpg',
        'github_link': 'https://github.com/yourusername/portfolio',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS']
    },
        {
        'title': 'Portfolio Website',
        'description': 'A modern portfolio website built with Flask and modern CSS.',
        'image': 'images/projects/portfolio.jpg',
        'github_link': 'https://github.com/yourusername/portfolio',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS']
    },
        {
        'title': 'Portfolio Website',
        'description': 'A modern portfolio website built with Flask and modern CSS.',
        'image': 'images/projects/portfolio.jpg',
        'github_link': 'https://github.com/yourusername/portfolio',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS']
    }
    # Add more projects here
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
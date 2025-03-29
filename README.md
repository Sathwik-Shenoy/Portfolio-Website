# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, HTML, and CSS.

## Features

- Responsive design that works on all devices
- Project showcase section
- Social media links
- Resume download functionality
- Contact information
- Modern UI with smooth animations

## Setup Instructions

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your resume PDF file to the `static` folder and name it `resume.pdf`
5. Update your personal information in `app.py`:
   - Name
   - Title
   - Email
   - LinkedIn profile URL
   - Instagram profile URL
6. Update the projects section in `app.py` with your own projects
7. Add project images to the `static` folder

## Running the Website

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to `http://localhost:5000`

## Customization

- Edit the HTML template in `templates/index.html`
- Modify the styling in `static/style.css`
- Update the project information in `app.py`

## Project Structure

```
portfolio-website/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, images, resume)
│   └── style.css
└── templates/         # HTML templates
    └── index.html
``` 
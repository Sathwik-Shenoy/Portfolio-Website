# Personal Portfolio Website

A modern, responsive portfolio website built with Flask featuring professional design, interactive contact form, and comprehensive project showcase.

## ✨ Features

- **Modern Design**: Professional red/orange gradient color scheme
- **Responsive Layout**: Works perfectly on all devices (desktop, tablet, mobile)
- **Interactive Contact Form**: Working backend with flash message notifications
- **Skills Showcase**: Organized technical skills by category
- **Experience Section**: Professional work history and achievements
- **Project Portfolio**: Detailed project descriptions with GitHub integration
- **Resume Download**: One-click resume download functionality
- **Social Integration**: Direct links to LinkedIn, GitHub, and email
- **Smooth Animations**: Professional animations and hover effects
- **Navigation Highlights**: Active section highlighting while scrolling
- **SEO Optimized**: Proper meta tags and Open Graph integration

## 🚀 Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins, Space Grotesk)
- **Animations**: CSS transitions and keyframes

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
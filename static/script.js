// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Mobile menu toggle
const mobileMenu = document.querySelector('.mobile-menu');
const navLinks = document.querySelector('.nav-links');

if (mobileMenu) {
    mobileMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenu.classList.toggle('active');
    });
}

// Contact form enhancement
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('.submit-btn');
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;
        
        // Note: The form will submit normally, this just adds visual feedback
    });
}

// Auto-hide flash messages
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            if (message.parentElement) {
                message.style.opacity = '0';
                setTimeout(() => {
                    message.remove();
                }, 300);
            }
        }, 5000); // Auto-hide after 5 seconds
    });
});

// Scroll-based navigation highlighting
function updateActiveNavigation() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', updateActiveNavigation);

// Header scroll effect
let lastScrollTop = 0;
const header = document.querySelector('header');

window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Add scrolled class for styling
    if (scrollTop > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
    
    lastScrollTop = scrollTop;
});

// Typing animation for hero subtitle
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing animation when page loads
document.addEventListener('DOMContentLoaded', function() {
    const subtitle = document.querySelector('.hero-subtitle');
    if (subtitle) {
        const originalText = subtitle.textContent;
        setTimeout(() => {
            typeWriter(subtitle, originalText, 80);
        }, 1000);
    }
});

// Hide cursor when mouse leaves window
document.addEventListener('mouseleave', () => {
    cursor.style.display = 'none';
    cursorFollower.style.display = 'none';
});

// Show cursor when mouse enters window
document.addEventListener('mouseenter', () => {
    cursor.style.display = 'block';
    cursorFollower.style.display = 'block';
});

// Add hover effect to interactive elements
const interactiveElements = document.querySelectorAll('a, button, .project-card, .contact-card');
interactiveElements.forEach(element => {
    element.addEventListener('mouseenter', () => {
        cursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
        cursorFollower.style.transform = 'translate(-50%, -50%) scale(1.2)';
    });

    element.addEventListener('mouseleave', () => {
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
        cursorFollower.style.transform = 'translate(-50%, -50%) scale(1)';
    });
});

// Projects horizontal scroll
const projectsContainer = document.querySelector('.projects-container');
const scrollLeftBtn = document.querySelector('.scroll-indicator-left');
const scrollRightBtn = document.querySelector('.scroll-indicator-right');

function scrollProjects(direction) {
    const scrollAmount = 400; // Width of one project card
    projectsContainer.scrollBy({
        left: direction * scrollAmount,
        behavior: 'smooth'
    });
}

scrollLeftBtn.addEventListener('click', () => scrollProjects(-1));
scrollRightBtn.addEventListener('click', () => scrollProjects(1));

// Hide/show scroll indicators based on scroll position
projectsContainer.addEventListener('scroll', () => {
    const isAtStart = projectsContainer.scrollLeft === 0;
    const isAtEnd = projectsContainer.scrollLeft + projectsContainer.clientWidth >= projectsContainer.scrollWidth - 1;

    scrollLeftBtn.style.opacity = isAtStart ? '0.5' : '1';
    scrollRightBtn.style.opacity = isAtEnd ? '0.5' : '1';
});

// Initialize scroll indicators
scrollLeftBtn.style.opacity = '0.5';

// Ensure page starts from top when loaded
window.addEventListener('load', function() {
    // Remove any hash from the URL
    if (window.location.hash) {
        history.replaceState(null, null, ' ');
    }
    // Scroll to top
    window.scrollTo(0, 0);
}); 
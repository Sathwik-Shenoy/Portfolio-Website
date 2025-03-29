// Custom cursor
const cursor = document.createElement('div');
const cursorFollower = document.createElement('div');
cursor.className = 'cursor';
cursorFollower.className = 'cursor-follower';
document.body.appendChild(cursor);
document.body.appendChild(cursorFollower);

let mouseX = 0;
let mouseY = 0;
let cursorX = 0;
let cursorY = 0;
let followerX = 0;
let followerY = 0;

// Initialize cursor position
function initCursor() {
    cursor.style.display = 'block';
    cursorFollower.style.display = 'block';
    cursor.style.left = '0px';
    cursor.style.top = '0px';
    cursorFollower.style.left = '0px';
    cursorFollower.style.top = '0px';
}

// Update cursor position
document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    
    // Update cursor position immediately
    cursor.style.left = mouseX + 'px';
    cursor.style.top = mouseY + 'px';
});

// Smooth cursor animation
function animate() {
    // Cursor follower animation
    followerX += (mouseX - followerX) * 0.1;
    followerY += (mouseY - followerY) * 0.1;
    cursorFollower.style.left = followerX + 'px';
    cursorFollower.style.top = followerY + 'px';

    requestAnimationFrame(animate);
}

// Initialize cursor
initCursor();
animate();

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
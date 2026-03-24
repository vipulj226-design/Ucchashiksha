document.addEventListener('DOMContentLoaded', () => {

    // Mobile Menu Toggle logic
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    
    mobileToggle.addEventListener('click', () => {
        mobileNavOverlay.classList.toggle('open');
        if(mobileNavOverlay.classList.contains('open')) {
            mobileToggle.innerHTML = '&#10005;'; // X icon
        } else {
            mobileToggle.innerHTML = '&#9776;'; // Hamburger icon
        }
    });

    // Close mobile menu when a link is clicked
    const mobileLinks = document.querySelectorAll('.mobile-nav-overlay a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileNavOverlay.classList.remove('open');
            mobileToggle.innerHTML = '&#9776;';
        });
    });

    // Sticky Header Scroll Effect
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // --- Lightbox Implementation for Gallery ---
    const galleryImages = document.querySelectorAll('.gallery-item img, .slider-track img');
    
    if (galleryImages.length > 0) {
        // Create modal elements natively
        const lightbox = document.createElement('div');
        lightbox.className = 'lightbox-modal';
        lightbox.innerHTML = `
            <span class="lightbox-close">&times;</span>
            <img class="lightbox-content" src="" alt="Full Screen User Media">
        `;
        document.body.appendChild(lightbox);
        
        const lightboxImg = lightbox.querySelector('.lightbox-content');
        const closeBtn = lightbox.querySelector('.lightbox-close');
        
        // Open lightbox upon user click
        galleryImages.forEach(img => {
            img.style.cursor = 'zoom-in'; 
            img.title = 'Click to enlarge';
            img.addEventListener('click', () => {
                lightboxImg.src = img.src;
                lightbox.classList.add('active');
            });
        });
        
        // Function to safely close
        const closeLightbox = () => {
            lightbox.classList.remove('active');
        };

        // Close when cross icon is clicked
        closeBtn.addEventListener('click', closeLightbox);
        
        // Close when background is clicked
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });
        
        // Close on ESC key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && lightbox.classList.contains('active')) {
                closeLightbox();
            }
        });
    }

});

document.querySelectorAll('.register-link a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault(); 
        const href = event.target.getAttribute('href');
        document.body.classList.add('fade-out');
        setTimeout(() => {
            window.location.href = href;
        }, 500); 
    });
});

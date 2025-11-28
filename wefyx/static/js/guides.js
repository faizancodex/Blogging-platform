document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.guide-link').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            alert('This guide will open soon!');
        });
    });
});

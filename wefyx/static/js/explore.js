document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.blog-card');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            alert('This would navigate to the full post!');
        });
    });
});

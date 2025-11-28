document.addEventListener('DOMContentLoaded', () => {
    const books = document.querySelectorAll('.buy-btn');

    books.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            alert('This book would be added to your cart!');
        });
    });
});

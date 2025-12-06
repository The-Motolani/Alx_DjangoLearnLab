const searchForm = document.querySelector('.search-form');
const searchInput = document.querySelector('.search-form input[type="text"]');

searchForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const query = searchInput.value.trim();

    if (query !== '') {
        searchForm.submit();
    }
});
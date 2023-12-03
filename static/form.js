alert("Make sure you add ', ' to seperate values in input, basicaly a comma and space");

document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input, textarea');

    inputs.forEach(input => {
        input.addEventListener('input', function () {
            updateWordCount(input);
        });
    });

    function updateWordCount(input) {
        const characters = input.value.trim().length;
        const wordCountElement = document.getElementById(`${input.id}-word-count`);

        if (wordCountElement) {
            wordCountElement.textContent = `Word count: ${characters}`;

            if (characters > 100) {
                wordCountElement.style.color = 'red';
            } else {
                wordCountElement.style.color = '#888';
            }
        }
    }
});

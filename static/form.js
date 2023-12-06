alert("Make sure you add ', ' to separate values in input, basically a comma and space");

document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('input, textarea');

    inputs.forEach(input => {
        input.addEventListener('input', function () {
            updateWordCount(input);
        });
    });

    function updateWordCount(input) {
        const characters = input.value.length;
        const wordCountElement = document.getElementById(`${input.id}-word-count`);

        console.log(input.maxLength);

        if (wordCountElement) {
            var n = `/ ${input.maxLength}`;

            if (input.maxLength == -1) {
                n = '';
            }

            wordCountElement.textContent = `count: ${characters} ${n}`;

            if (input.maxLength == -1) {
                wordCountElement.style.color = '#888';
            } else if (characters > input.maxLength - 3) {
                wordCountElement.style.color = 'red';
            } else if (characters > (input.maxLength / 2) + 10) {
                wordCountElement.style.color = '#E8C331';

            } else {
                wordCountElement.style.color = '#888';
            }
        }
    }
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('analyze-btn').addEventListener('click', function() {
        var inputText = document.getElementById('input-text').value;
        if (!inputText.trim()) {
            document.getElementById('output').innerHTML = '<div>Please enter a product review.</div>';
            return;
        }

        // Perform sentiment analysis using JavaScript
        analyzeSentiment(inputText);
    });
});

function analyzeSentiment(inputText) {
    // Perform sentiment analysis here (you can use libraries or custom logic)
    // For this example, let's assume a placeholder sentiment score
    var sentimentScore = Math.random() * 10; // Placeholder score
    var sentimentCategory = sentimentScore > 5 ? 'Positive' : 'Negative'; // Placeholder category
    var color = sentimentCategory === 'Positive' ? 'green' : 'red'; // Placeholder color

    // Update the UI with the sentiment analysis result
    var outputHTML = '<div style="color: ' + color + ';">';
    outputHTML += 'Sentiment Score: ' + sentimentScore.toFixed(2) + '<br>';
    outputHTML += 'Sentiment Category: ' + sentimentCategory + '</div>';
    document.getElementById('output').innerHTML = outputHTML;
}

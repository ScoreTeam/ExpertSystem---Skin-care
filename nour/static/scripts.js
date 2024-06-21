console.log('inside script');
document.addEventListener("DOMContentLoaded", function() {
    const startButton = document.querySelector("button[type='submit']");
    if (startButton) {
        startButton.addEventListener("click", function(event) {
            console.log("Start button clicked");
            // You can add any additional functionality here if needed
        });
    }
});

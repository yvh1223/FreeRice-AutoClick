--F12--> Console--> allow typing --> paste below

window.autoAnswerFunction = function() {
  const questionElement = document.querySelector(".card-title");
  const answerButtons = document.querySelectorAll('.card-button');

  if (questionElement && answerButtons.length >= 3) {
    answerButtons[2].click(); // Clicks the third answer option
  }

  // Clear all existing timeouts
  while (window.timeoutList.length) {
    clearTimeout(window.timeoutList.shift());
  }

  // Set a new timeout
  window.timeoutList.push(setTimeout(window.autoAnswerFunction, 400));
};

// Initialize the array and start the loop
window.timeoutList = [setTimeout(window.autoAnswerFunction, 400)];

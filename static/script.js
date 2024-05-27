const chatContainer = document.querySelector('.chat-container');
      const inputForm = document.querySelector('.typing-textarea');
      const inputField = document.getElementById('chat_input');
      const resetButton = document.getElementById('reset-btn');

      // Add event listener for form submission
      inputForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        // Get input value and split it into numbers
        const numbers = inputField.value.split(' ').map(Number);
        
        // Check if the input contains at least two numbers
        if (numbers.length < 2) {
          addBotMessage('Please enter at least two numbers.');
          return;
        }
        
        // Calculate sum of the numbers
        const sum = numbers.reduce((acc, curr) => acc + curr, 0);
        
        // Display user's message
        addUserMessage(inputField.value);
        
        // Display bot's message with the result
        addBotMessage(`The sum of ${numbers.join(' + ')} is ${sum}.`);
        
        // Clear input field
        inputField.value = '';
      });

      // Function to add user's message to the chat container
      function addUserMessage(message) {
        const userMessageElement = document.createElement('div');
        userMessageElement.classList.add('user-message');
        userMessageElement.textContent = message;
        chatContainer.appendChild(userMessageElement);
      }

      // Function to add bot's message to the chat container
      function addBotMessage(message) {
        const botMessageElement = document.createElement('div');
        botMessageElement.classList.add('bot-message');
        botMessageElement.textContent = message;
        chatContainer.appendChild(botMessageElement);
      }

      // Add event listener for reset button
      resetButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default behavior of button click

        // Clear chat container
        chatContainer.innerHTML = '';

        // Clear input field
        inputField.value = '';
      });
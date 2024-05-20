# quiz_game

This Python script is a simulation of the popular quiz game "Kaun Banega Crorepati" (KBC), designed to provide an interactive and engaging user experience. The game features a series of multiple-choice questions, incrementally rewarding the player with virtual money for each correct answer. Here's an in-depth look at the script's functionality and features:

#Overview
* User Interaction: The game begins by asking the player for their name and welcoming them to KBC, creating a personalized experience.
* Question Bank: The script includes 16 well-crafted questions, each with four answer choices. The correct answer for each question is specified, allowing the game to validate the player's responses.
* Prize Levels: The game uses a structured prize ladder, starting from Rs. 1,000 and going up to Rs. 10,000,000, providing a sense of progression and achievement.
  
#Features
Interactive Gameplay:
* Players are prompted to press Enter to start the game and to continue to the next question after each correct answer, maintaining a flow in the gameplay.
* At any point, the player can choose to quit the game by entering '0', securing the prize money they have won up to that point.

#Dynamic Question Presentation:
* Questions are presented one at a time, with the prize amount for the current question displayed prominently.
* The script clearly shows the question and the four possible answers, making it easy for the player to read and decide.
  
#Answer Validation and Feedback:
* After the player selects an answer, the script checks if it's correct.
* If the answer is correct, the player is congratulated, and the prize money is updated.
* If the answer is incorrect, the game ends, and the player is informed of their final winnings.
  
#Graceful Exit:
* The player can exit the game anytime by choosing '0'. The script will then display the total prize money won.
* If an incorrect answer is given, the game ends smoothly, informing the player of their prize up to the last correct answer.

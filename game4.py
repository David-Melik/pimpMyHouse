import pygame

import time

from pygame.time import delay

from components import components

# Initialize Pygame
pygame.init()


# Set up the display
gameDisplay = pygame.display.set_mode(
    (1920, 1200), pygame.FULLSCREEN
)  # Set the screen size (width x height)
pygame.display.set_caption("Pimp My House")  # Set the window caption

green = (0, 152, 5)
red = (219, 63, 16)
black = (0, 0, 0)
white = (255, 255, 255)
box_position = (0, 1080)  # Top-left corner of the box
box_size = (1920, 120)

# Define font for text
font = pygame.font.Font(None, 50)  # You can adjust the size (50) as per your preference

playerScore = [[], [], [], []]


def show_message(message, x_pos, color):
    # Render the text as an image (surface)
    text = font.render(message, True, color)
    gameDisplay.blit(text, (x_pos, 1125))
    pygame.display.update()  # Update the display to show the message


def show_box(size, position):
    pygame.draw.rect(gameDisplay, black, pygame.Rect(position, size))
    pygame.display.update()


def show_messageNoUpdate(message, x_pos, color):
    # Render the text as an image (surface)
    text = font.render(message, True, color)
    gameDisplay.blit(text, (x_pos, 1125))


def show_messagePosition(message, x_pos, y_pos, color):
    # Render the text as an image (surface)
    text = font.render(message, True, color)
    gameDisplay.blit(text, (x_pos, y_pos))


def show_boxNoUpdate(size, position):
    pygame.draw.rect(gameDisplay, black, pygame.Rect(position, size))


def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle quit event
            pygame.quit()
            quit()


def slideReady(i):
    player_ready = [[], [], [], []]  # Track readiness for each player
    positionPlayer = [50, 505, 960, 1415]
    player_keys = {
        pygame.K_a: "Player 1",  # 'A' for Player 1
        pygame.K_z: "Player 2",  # 'Z' for Player 2
        pygame.K_e: "Player 3",  # 'E' for Player 3
        pygame.K_r: "Player 4",  # 'R' for Player 4
    }

    image_filename = "image/" + str(i) + ".jpg"
    image = pygame.image.load(image_filename)
    gameDisplay.blit(
        image, (0, 0)
    )  # Draw the image on the screen at coordinates (0, 0)
    pygame.display.update()

    while player_ready != [[1], [1], [1], [1]]:  # Check if everyone is ready
        # Show instructions for players if they haven't pressed their button
        show_message(str(i), 10, white)

        for j in range(0, 4):  # 0, 1, 2, 3 for the 4 players
            # Check if the player hasn't pressed their button yet (ready list is empty)
            if player_ready[j] == []:
                # Display message for the corresponding player, based on index `j`
                show_message(
                    f"Press button for {player_keys[list(player_keys.keys())[j]]}",
                    positionPlayer[j],
                    red,
                )
            elif player_ready[j] == [1]:  # If the player is already ready
                # Show that the player is ready
                show_message(
                    f"{player_keys[list(player_keys.keys())[j]]} is ready!",
                    positionPlayer[j],
                    green,
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle quit event
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in player_keys:  # Check if a player pressed a valid key
                    player_index = list(player_keys.keys()).index(
                        event.key
                    )  # Get the player index
                    if (
                        len(player_ready[player_index]) == 0
                    ):  # If the player hasn't pressed yet

                        gameDisplay.blit(image, (0, 0))
                        show_box(box_size, box_position)
                        player_ready[player_index].append(1)  # Mark the player as ready
                        show_message(
                            f"{player_keys[event.key]} is ready!",
                            positionPlayer[player_index],
                            green,
                        )  # Show confirmation message

        pygame.time.wait(250)  # Add a small delay for smooth updates
    show_box(box_size, box_position)


def slideChapter(chapter, pageReview):

    # Initialize image Review
    image_filename = "image/" + str(pageReview) + ".jpg"
    image = pygame.image.load(image_filename)
    gameDisplay.blit(image, (0, 0))
    pygame.display.update()

    # Initialize info about the Chapter
    items = components[chapter]
    names = [item["name"] for item in items]
    num_items = len(items)

    show_message("You have " + str(num_items) + " items available", 10, white)

    previous_time_left = None
    start_time = time.time()
    timeLeft = 10
    while timeLeft > 0:
        quitGame()
        timeLeft = max(10 - int(time.time() - start_time), 0)
        if timeLeft != previous_time_left:
            show_boxNoUpdate((500, 80), (1400, 1125))
            show_messageNoUpdate(f"Countdown {timeLeft}s", 1500, white)
            previous_time_left = timeLeft  # Update the previous time for comparison
            pygame.display.update()
    show_box(box_size, box_position)


def slideCard(chapter, pageReview):
    # Initialize player setup
    player_claim = [[0], [0], [0], [0]]  # Track readiness for each player
    positionPlayer = [50, 50, 50, 50]
    player_keys = {
        pygame.K_a: "Player 1",  # 'A' for Player 1
        pygame.K_z: "Player 2",  # 'Z' for Player 2
        pygame.K_e: "Player 3",  # 'E' for Player 3
        pygame.K_r: "Player 4",  # 'R' for Player 4
    }

    # Initialize info about the Chapter
    items = components[chapter]
    names = [item["name"] for item in items]
    num_items = len(items)
    j = 0
    for i in range(pageReview + 1, pageReview + num_items):

        # Initialize image Review
        image_filename = "image/" + str(i) + ".jpg"
        image = pygame.image.load(image_filename)
        gameDisplay.blit(image, (0, 0))
        pygame.display.update()

        # Card item
        start_time = time.time()  # Start the timer for 30 seconds
        previous_time_left = None
        claim = False
        while any(0 in claim for claim in player_claim):
            show_box(
                (800, 80), (1000, 1125)
            )  # to remove the red text about the player already selected item

            if claim == True:
                break
            # show how much card left
            show_message(str(num_items) + " items left", 10, white)
            # show_message("image numero " + str(i), 300, white)
            # show_message(str(names[j]), 800, white)
            timeLeft = max(10 - int(time.time() - start_time), 0)

            if timeLeft != previous_time_left:
                show_boxNoUpdate((100, 50), (1830, 1125))
                show_messageNoUpdate(f"{timeLeft}s", 1830, white)
                previous_time_left = timeLeft  # Update the previous time for comparison

            if timeLeft == 0:
                break

            for event in pygame.event.get():
                quitGame()
                if event.type == pygame.KEYDOWN:
                    if (
                        event.key in player_keys
                    ):  # Check if a player pressed a valid key
                        player_index = list(player_keys.keys()).index(
                            event.key
                        )  # Get the player index
                        if player_claim[player_index] == [1]:
                            gameDisplay.blit(image, (0, 0))
                            show_box(box_size, box_position)
                            show_message(
                                f"{player_keys[event.key]} you already claimed a item !",
                                1000,
                                red,
                            )
                            pygame.time.wait(
                                500
                            )  # Add a small delay for smooth updates

                        if player_claim[player_index] == [
                            0
                        ]:  # If the player hasn't pressed yet

                            gameDisplay.blit(image, (0, 0))
                            show_box(box_size, box_position)
                            player_claim[player_index] = [1]
                            show_message(
                                f"{player_keys[event.key]} claim the item!",
                                50,
                                green,
                            )  # Show confirmation message
                            playerScore[j].append(names[j])
                            j = j + 1
                            timeLeft = 0
                            claim = True
                            pygame.time.wait(
                                2000
                            )  # Add a small delay for smooth updates
        if player_claim == [[1], [1], [1], [1]]:  # if everyone has already a item
            i = pageReview + num_items

            show_box(box_size, box_position)
            previous_time_left = None
            start_time = time.time()
            timeLeft = 1
            while timeLeft > 0:
                quitGame()
                timeLeft = max(10 - int(time.time() - start_time), 0)
                if timeLeft != previous_time_left:
                    show_boxNoUpdate((1000, 80), (1000, 1125))
                    show_messageNoUpdate(
                        f"Everyone have a item so let's move on, next item on {timeLeft}s",
                        1000,
                        green,
                    )
                    previous_time_left = (
                        timeLeft  # Update the previous time for comparison
                    )
                    pygame.display.update()

            break

        claim = False
        previous_time_left = None  # when item is finish coutdown for the next part
        start_time = time.time()
        timeLeft = 1
        while timeLeft > 0:
            quitGame()
            timeLeft = max(5 - int(time.time() - start_time), 0)
            if timeLeft != previous_time_left:
                show_boxNoUpdate((500, 50), (1400, 1125))
                show_messageNoUpdate(
                    f"Time left before next item {timeLeft}s",
                    1400,
                    white,
                )
                previous_time_left = timeLeft  # Update the previous time for comparison
                pygame.display.update()
        show_box(box_size, box_position)


def calculate_score_for_player(player_cards):
    # Coefficients
    coef_prix = 2
    coef_eco_friendly = 3
    coef_durability = 1
    coef_energy_consumption = 1
    score = 0
    for card_name in player_cards:
        # Chercher la carte dans components
        found = False
        for category, items in components.items():
            for item in items:
                if item["name"] == card_name:
                    # Calculer le score en fonction des coefficients
                    score += (
                        item["prix"] * coef_prix
                        + item["durability"] * coef_durability
                        + item["energy_consumption"] * coef_energy_consumption
                        + item["eco_friendly"] * coef_eco_friendly
                    )
                    found = True
                    break
            if found:
                break
    return score


def showResult():
    font = pygame.font.Font(None, 50)  # Adjust the font size as needed
    show_box((1920, 1200), (0, 0))  # Clear the screen or display background
    position = 50

    # Initialize the list to store the scores of each player
    scores = []  # This needs to be initialized before appending scores

    # Calculate and display the scores for each player
    for i, player_cards in enumerate(playerScore):
        player_score = calculate_score_for_player(player_cards)
        scores.append(player_score)  # Add the score to the scores list
        print(f"Player {i + 1}'s Score: {player_score}")
        show_messageNoUpdate(f"Player {i + 1}'s Score: {player_score}", position, white)

        position = position + 500  # Adjust space between player score messages
        pygame.display.update()

    # Determine the winner by finding the maximum score
    max_score = max(scores)
    winner_index = scores.index(max_score)  # Get the index of the winner

    # Display the winner's message
    show_messagePosition(
        f"The winner is Player {winner_index + 1} with a score of {max_score}!",
        540,
        480,
        green,
    )

    pygame.display.update()

    # Wait for the player to close the window
    waiting = True
    while waiting:
        quitGame()  # Check if the user wants to quit


# Calculer et afficher le score de chaque joueur


slideReady(1)
slideReady(2)
#
#
# for i in range(0, 6):  # for 7 chapter
#    pageReview = [3, 8, 15, 22, 28, 35, 42, 49]
#    chapter = list(components.keys())[i]
#
#    slideChapter(chapter, pageReview[i])
#    slideCard(chapter, pageReview[i])
#    # review
#    # all item
#
i = 5
pageReview = [3, 8, 15, 22, 28, 35, 42, 49]
chapter = list(components.keys())[i]

# slideChapter(chapter, pageReview[i])
slideCard(chapter, pageReview[i])
calculate_score_for_player(playerScore)
showResult()

pygame.quit()

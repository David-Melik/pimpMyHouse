import pygame
import time

from components import components

# Initialize Pygame
pygame.init()


# Set up the display
gameDisplay = pygame.display.set_mode(
    (1920, 1200)
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

player1Score = []
player2Score = []
player3Score = []
player4Score = []


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
    player_claim = [[], [], [], []]  # Track readiness for each player
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
        while player_claim == [[], [], [], []]:
            # show how much card left
            show_message(str(num_items) + " items left", 10, white)
            show_message("image numero " + str(i), 300, white)
            show_message(str(names[j]), 800, white)
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
                        if (
                            len(player_claim[player_index]) == 0
                        ):  # If the player hasn't pressed yet

                            gameDisplay.blit(image, (0, 0))
                            show_box(box_size, box_position)
                            player_claim[player_index].append(1)
                            show_message(
                                f"{player_keys[event.key]} claim the item!",
                                positionPlayer[player_index],
                                green,
                            )  # Show confirmation message
                            player1Score.append(names[j])
                            j = j + 1
                            timeLeft = 0

        previous_time_left = None
        start_time = time.time()
        timeLeft = 10
        while timeLeft > 0:
            quitGame()
            timeLeft = max(10 - int(time.time() - start_time), 0)
            if timeLeft != previous_time_left:
                show_boxNoUpdate((500, 50), (1400, 1125))
                show_messageNoUpdate(
                    f"Time left before next item {timeLeft}s", 1400, white
                )
                previous_time_left = timeLeft  # Update the previous time for comparison
                pygame.display.update()
        show_box(box_size, box_position)
        player_claim = [[], [], [], []]


def showResult():
    return


slideReady(1)
slideReady(2)


for i in range(0, 6):  # for 7 chapter
    pageReview = [3, 8, 15, 22, 28, 35, 42, 49]
    chapter = list(components.keys())[i]

    slideChapter(chapter, pageReview[i])
    slideCard(chapter, pageReview[i])
    # review
    # all item

showResult()


"""
start_time = time.time()  # Start the timer for 10 seconds
while time.time() - start_time < 10:  # Display each item for 10 seconds
   screen.fill((255, 255, 255))  # Clear screen with white background

            # Display current option's image and stats
   screen.blit(
   option["image_obj"], (100, 150)
   )  # Adjust position for each image
            font = pygame.font.Font(None, 36)
            text = font.render(
                f"{option['name']} (Aesthetics: {option['aesthetics']}, Durability: {option['durability']})",
                True,
                (0, 0, 0),
            )
            screen.blit(text, (300, 160))  # Position next to the image

            pygame.display.flip()  # Update screen display

            # Check for player input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle quit event
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:  # Player 1 presses 'A'
                        choose_component(
                            0, component_name, i
                        )  # Player 1 claims the item
                        continue
                    elif event.key == pygame.K_z:  # Player 2 presses 'Z'
                        choose_component(1, component_name, i)
                        return
                    elif event.key == pygame.K_e:  # Player 3 presses 'E'
                        choose_component(2, component_name, i)
                        return
                    elif event.key == pygame.K_r:  # Player 4 presses 'R'
                        choose_component(3, component_name, i)
                        return

"""
pygame.quit()

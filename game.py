import pygame
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))

# Define paths for component images
components = {
    "kitchen": [
        {
            "name": "Marble Kitchen",
            "aesthetics": 9,
            "durability": 8,
            "image": "1.jpg",
            "claimed": False,
        },
        {
            "name": "Ceramic Kitchen",
            "aesthetics": 7,
            "durability": 6,
            "image": "2.jpg",
            "claimed": False,
        },
        {
            "name": "Wooden Kitchen",
            "aesthetics": 8,
            "durability": 7,
            "image": "3.jpg",
            "claimed": False,
        },
    ],
    # Additional components like walls, flooring, etc. with their images
}

# Load images for each component option
for component_name, options in components.items():
    for option in options:
        option["image_obj"] = pygame.image.load(
            option["image"]
        )  # Load image and store in "image_obj"

# Game variables
players = [0, 0, 0, 0]  # Scores for 4 players
selected_components = {
    player: {} for player in range(4)
}  # Store chosen components for each player


def choose_component(player, component_name, choice_index):
    """
    Choose an item for a specific player, marking it as claimed if available.
    """
    choice = components[component_name][choice_index]
    if not choice["claimed"]:
        selected_components[player][component_name] = choice
        choice["claimed"] = True  # Mark as claimed


def display_component_one_by_one(component_name, options):
    """
    Display each item in `options` one by one, allowing players to choose within 10 seconds.
    """
    for i, option in enumerate(options):
        if option["claimed"]:
            continue  # Skip if item is already claimed

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
                        continue  # Exit the loop to move to the next item
                    elif event.key == pygame.K_z:  # Player 2 presses 'Z'
                        choose_component(1, component_name, i)
                        return  # Exit the loop to move to the next item
                    elif event.key == pygame.K_e:  # Player 3 presses 'E'
                        choose_component(2, component_name, i)
                        return  # Exit the loop to move to the next item
                    elif event.key == pygame.K_r:  # Player 4 presses 'R'
                        choose_component(3, component_name, i)
                        return  # Exit the loop to move to the next item

        # If no one claims the item within 10 seconds, move on to the next item
        # (no additional code needed, as the loop will naturally continue to the next item)


# Run one round for each component, displaying items one by one
for component_name, options in components.items():
    display_component_one_by_one(component_name, options)


# Scoring after all rounds
def calculate_score(player_components):
    score = 0
    for part, details in player_components.items():
        score += details["aesthetics"] + details["durability"]
    return score


# Calculate and display final scores
for i in range(4):
    players[i] = calculate_score(selected_components[i])
print("Player scores:", players)

pygame.quit()

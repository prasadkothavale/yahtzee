import argparse
from core.sections import Sections
from game import Game



def main():
    parser = argparse.ArgumentParser(description="Play Yahtzee from the terminal.")
    parser.add_argument("--players", type=int, default=2, help="Number of players (default: 2)")
    args = parser.parse_args()
    players = args.players

    # Initialize the game
    games = []
    current_player = 0
    players = 0

    for i in range(args.players):
        game = Game(i)
        games.append(game)
        
    game = games[current_player]  # Start with the first player

    print("Welcome to Yahtzee!")
    print(f"Starting a game with {args.players} players.\n")

    while not game.is_game_over():
        print(f"Player {current_player + 1}'s turn:")
        game.roll_dice()
        print(f"Dice rolled: {game.get_dice_values()}")
        
        for _ in range(2):  # Allow up to 2 re-rolls
            reroll = input("Enter dice indices to keep (comma-separated) or for no change press Enter: ")
            indices = [int(i) for i in reroll.split(",") if i.isdigit()]
            game.keep_dice(indices)
            if (len(indices) == 5):
                print("All dice kept, no re-roll.")
                break
            game.roll_dice()
            print(f"Dice after re-roll: {game.get_dice_values()}")

        print("Available categories:")
        for idx, category in enumerate(game.get_available_categories()):
            print(f"{idx}: {category}")
        
        category_choice = int(input("Choose a category by [number]: "))
        game.score_section(Sections[category_choice])
        print(f"Scorecard: {game.get_score_sheet()}\n")
        current_player = (current_player + 1) % players
        game = games[current_player]

    print("Game over!")
    print("Final scores:")
    for game in games:
        print(f"Player {game.get_player()}: {game.get_score()} points")

if __name__ == "__main__":
    main()
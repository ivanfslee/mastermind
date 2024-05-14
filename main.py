from cli import CLI
from game import Game


def main() -> None:
    cli = CLI()
    cli.display_game_intro()
    game_setup: dict[str, int | dict] = cli.game_setup_prompts()
    game = Game(cli, game_setup)
    game.play()


if __name__ == "__main__":
    main()

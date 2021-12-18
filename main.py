# python 3.10
# UTF-8
import argparse

import find_command


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-chatbot',
                        nargs='+',
                        type=str,
                        dest='chatbot',
                        help="Commandes du chatbot voulu"
                        )

    args = parser.parse_args()
    find_command.find_command(args.chatbot)

    # attention: argparse supprime automatiquement des guillemets dans un paramètre
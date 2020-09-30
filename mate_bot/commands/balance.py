"""
MateBot command executor classes for /balance
"""

import telegram

from mate_bot.state.user import MateBotUser
from mate_bot.commands.base import BaseCommand
from mate_bot.parsing.types import user as user_type
from mate_bot.parsing.util import Namespace


class BalanceCommand(BaseCommand):
    """
    Command executor for /balance
    """

    def __init__(self):
        super().__init__("balance", "The `/balance` command prints the current account balance of an "
                                    "account. If no account name is provided the balance of the "
                                    "sender is given.")
        self.parser.add_argument("user", type=user_type, nargs="?")

    def run(self, args: Namespace, update: telegram.Update) -> None:
        """
        :param args: parsed namespace containing the arguments
        :type args: argparse.Namespace
        :param update: incoming Telegram update
        :type update: telegram.Update
        :return: None
        """

        if args.user:
            user = args.user
            update.effective_message.reply_text(f"Balance of {user.name} is: {user.balance / 100 : .2f}€")
        else:
            user = MateBotUser(update.effective_message.from_user)
            update.effective_message.reply_text(f"Your balance is: {user.balance / 100 :.2f}€")

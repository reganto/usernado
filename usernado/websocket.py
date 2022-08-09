from typing import Any, Dict, Union, Set

import usernado

from .base import BaseSocket


class WebSocketHandler(BaseSocket):
    """Every websocket handler MUST inherit from ``WebSocketHandler``."""

    def send(
        self,
        message: Union[bytes, str, Dict[str, Any]],
        binary: bool = False,
    ) -> None:
        """Send a message to the particular participant.

        :param message: Message to send.
        :type message: Union[bytes, str, Dict[str, Any]]
        :param binary: Type of the message, defaults to False.
        :type binary: bool, optional
        """
        self.write_message(message, binary)

    def broadcast(
        self,
        participants: Set["usernado.WebSocketHandler"],
        message: Union[bytes, str, Dict[str, Any]],
        binary: bool = False,
    ) -> None:
        """Broadcast a message to all participants.

        :param participants: Participants to send message.
        :type participants: Set[usernado.WebSocketHandler]
        :param message: Message to send.
        :type message: Union[bytes, str, Dict[str, Any]]
        :param binary: Type of message, defaults to False.
        :type binary: bool, optional
        """
        for participant in participants:
            participant.send(message, binary)

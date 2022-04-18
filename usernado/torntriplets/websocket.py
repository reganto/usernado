from typing import Any, Dict, Union

from usernado.torntriplets.base import BaseSocket


class WebSocketHandler(BaseSocket):
    def send(
        self,
        message: Union[bytes, str, Dict[str, Any]],
        binary: bool = False,
    ):
        """Send a message to specific participant.

        :param message: Message to send
        :type message: Union[bytes, str, Dict[str, Any]]
        :param binary: Type of message, defaults to False
        :type binary: bool, optional
        """
        self.write_message(message, binary)

    def broadcast(
        self,
        participants: set,
        message: Union[bytes, str, Dict[str, Any]],
        binary: bool = False,
    ):
        """Broadcast a message to all participants.

        :param participants: Participants to send message
        :type participants: set
        :param message: Message to send
        :type message: Union[bytes, str, Dict[str, Any]]
        :param binary: Type of message, defaults to False
        :type binary: bool, optional
        """
        for participant in participants:
            participant.send(message, binary)

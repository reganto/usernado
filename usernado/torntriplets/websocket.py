from typing import Any, Dict, Union

from usernado.torntriplets.base import BaseSocket


class WebSocketHandler(BaseSocket):
    def send(
        self,
        message: Union[bytes, str, Dict[str, Any]],
        binary: bool = False,
    ):
        """Send a message to specific participant

        :message: Message to send
        :returns: None

        """
        self.write_message(message, binary)

    def broadcast(
        self,
        participants: set,
        message: Union[bytes, str, Dict[str, Any]],
        binary: bool = False,
    ):
        """Broadcast a message to all participants

        :participants: Participants to send broadcast message
        :message: Message to send to all participants
        :returns: None

        """
        for participant in participants:
            participant.send(message, binary)

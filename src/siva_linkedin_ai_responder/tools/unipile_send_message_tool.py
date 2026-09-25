
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests


class UnipileSendMessageToolInput(BaseModel):
    """Input schema for UnipileSendMessageTool."""

    chat_id: str = Field(
        ...,
        description="The Unipile chat/conversation ID to reply to.",
    )
    reply_text: str = Field(
        ...,
        description="The message text to send as a reply.",
    )


class UnipileSendMessageTool(BaseTool):
    """Tool for sending a LinkedIn message reply via the Unipile REST API."""

    name: str = "UnipileSendMessageTool"
    description: str = (
        "Sends a LinkedIn message reply to an existing chat thread via the Unipile REST API."
    )
    args_schema: Type[BaseModel] = UnipileSendMessageToolInput

    def _run(self, chat_id: str, reply_text: str) -> str:
        """
        Send a LinkedIn message reply to a chat thread using the Unipile API.

        Args:
            chat_id: The Unipile chat/conversation ID to reply to.
            reply_text: The message text to send.

        Returns:
            A success or failure message with relevant details.
        """
        BASE_URL = "https://api60.unipile.com:19027"
        API_KEY = "BmMrXufv.Fy7m3UpZj7+QYnV1afp3/eWbbW6DXiEJAnyVtO/CETY="
        ACCOUNT_ID = "j_-GuEvQQ-mic6FrF48ZWg"

        url = f"{BASE_URL}/api/v1/chats/{chat_id}/messages"

        headers = {
            "X-API-KEY": API_KEY,
            "accept": "application/json",
            "content-type": "application/json",
        }

        payload = {
            "text": reply_text,
            "account_id": ACCOUNT_ID,
        }

        try:
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code // 100 == 2:
                return f"Message sent successfully. Response: {response.json()}"
            else:
                return (
                    f"Failed to send message. "
                    f"Status: {response.status_code}. "
                    f"Error: {response.text}"
                )

        except requests.exceptions.RequestException as e:
            return f"An error occurred while sending the message: {str(e)}"

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests


class PhantomBusterSendReplyInput(BaseModel):
    """Input schema for PhantomBusterSendReplyTool."""

    webhook_url: str = Field(
        ...,
        description="The PhantomBuster webhook endpoint URL to send the POST request to.",
    )
    sender_name: str = Field(
        ...,
        description="The name of the LinkedIn message sender to whom the reply is directed.",
    )
    reply_text: str = Field(
        ...,
        description="The reply message text to send via PhantomBuster.",
    )


class PhantomBusterSendReplyTool(BaseTool):
    """Tool for sending a LinkedIn reply through a PhantomBuster webhook endpoint."""

    name: str = "PhantomBuster Send Reply Tool"
    description: str = (
        "Sends a LinkedIn reply via a PhantomBuster webhook URL. "
        "Accepts a webhook URL, the sender's name, and the reply text, "
        "then performs an HTTP POST request with the appropriate JSON payload."
    )
    args_schema: Type[BaseModel] = PhantomBusterSendReplyInput

    def _run(self, webhook_url: str, sender_name: str, reply_text: str) -> str:
        """
        Executes the HTTP POST request to the PhantomBuster webhook.

        Args:
            webhook_url (str): The PhantomBuster webhook endpoint URL.
            sender_name (str): The LinkedIn message sender's name.
            reply_text (str): The reply message to send.

        Returns:
            str: A success message with the HTTP status code, or an error message.
        """
        payload = {
            "sender_name": sender_name,
            "reply": reply_text,
        }

        try:
            response = requests.post(
                webhook_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30,
            )

            if response.ok:
                return (
                    f"✅ Reply successfully sent to '{sender_name}' via PhantomBuster. "
                    f"HTTP Status Code: {response.status_code}."
                )
            else:
                return (
                    f"⚠️ Request completed but returned a non-success status. "
                    f"HTTP Status Code: {response.status_code}. "
                    f"Response body: {response.text[:300]}"
                )

        except requests.exceptions.MalformedURLError as e:
            return f"❌ Invalid webhook URL provided: {str(e)}"
        except requests.exceptions.ConnectionError as e:
            return f"❌ Connection error while reaching the PhantomBuster webhook: {str(e)}"
        except requests.exceptions.Timeout:
            return "❌ The request to the PhantomBuster webhook timed out after 30 seconds."
        except requests.exceptions.RequestException as e:
            return f"❌ An unexpected error occurred during the HTTP request: {str(e)}"

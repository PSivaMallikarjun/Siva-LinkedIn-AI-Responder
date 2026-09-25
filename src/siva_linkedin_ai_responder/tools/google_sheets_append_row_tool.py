
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List
import requests


class GoogleSheetsAppendRowInput(BaseModel):
    """Input schema for GoogleSheetsAppendRowTool."""

    apps_script_url: str = Field(
        ...,
        description="The Google Apps Script Web App deployment URL to POST the row data to.",
    )
    row_data: List[str] = Field(
        ...,
        description="A list of string values representing the row to append to the Google Sheet.",
    )


class GoogleSheetsAppendRowTool(BaseTool):
    """Tool for appending a row to a Google Sheet via a Google Apps Script Web App URL."""

    name: str = "Google Sheets Append Row Tool"
    description: str = (
        "Appends a new row to a Google Sheet by sending a POST request to a Google Apps Script "
        "Web App deployment URL. Provide the Apps Script URL and a list of string values to append."
    )
    args_schema: Type[BaseModel] = GoogleSheetsAppendRowInput

    def _run(self, apps_script_url: str, row_data: List[str]) -> str:
        """
        Posts row_data as a JSON payload to the given Google Apps Script Web App URL.

        Args:
            apps_script_url: The deployed Apps Script Web App URL.
            row_data: List of string values to append as a new row.

        Returns:
            A success or descriptive error message string.
        """
        payload = {"row": row_data}

        try:
            response = requests.post(
                apps_script_url,
                json=payload,
                timeout=30,
            )

            if response.status_code == 200:
                return (
                    f"Row successfully appended to the Google Sheet. "
                    f"Response: {response.text[:500]}"  # Truncate long responses
                )
            else:
                return (
                    f"Failed to append row. HTTP {response.status_code}: {response.text[:500]}"
                )

        except requests.exceptions.ConnectionError as e:
            return f"Connection error: Unable to reach the Apps Script URL. Details: {str(e)}"
        except requests.exceptions.Timeout:
            return "Request timed out after 30 seconds. Please check the Apps Script URL and try again."
        except requests.exceptions.MissingSchema:
            return f"Invalid URL provided: '{apps_script_url}'. Please ensure it is a valid URL starting with http:// or https://."
        except requests.exceptions.InvalidURL as e:
            return f"Invalid URL error: {str(e)}"
        except requests.exceptions.RequestException as e:
            return f"An unexpected request error occurred: {str(e)}"

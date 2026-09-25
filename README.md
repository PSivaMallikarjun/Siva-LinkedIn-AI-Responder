# 🤖 siva-linkedin-ai-responder

![CrewAI](https://img.shields.io/badge/Built%20with-CrewAI-blue) ![Python](https://img.shields.io/badge/Python-3.10%2B-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

> A multi-agent CrewAI automation that reads, classifies, and replies to LinkedIn messages in Siva's voice — fully automated.

---

## 🧠 Overview

This automation listens to incoming LinkedIn messages via **Unipile's webhook**, classifies them by intent, drafts a contextual reply in **Siva's personal tone**, sends it back on LinkedIn, and logs the full interaction to **Google Sheets**.

---

## 🔄 Architecture

```
Unipile Webhook (Incoming LinkedIn Message)
              ↓
   [1] Message Classifier Agent
              ↓
   [2] Reply Drafting Agent
              ↓
     ┌────────┴────────┐
[3] Unipile Sender   [4] Google Sheets Logger
```

---

## 🤖 Agents

| # | Agent | Role |
|---|-------|------|
| 1 | **Message Classifier** | Categorizes the message: `recruiter`, `collaboration`, `cold_pitch`, `recommendation`, `connection_request`, `technical_discussion`, `generic_greeting` |
| 2 | **Siva's Voice Agent** | Drafts a reply in Siva's humble-confident first-person tone |
| 3 | **Unipile Dispatcher** | POSTs the reply to Unipile API for LinkedIn delivery |
| 4 | **Google Sheets Logger** | Appends a timestamped row with all interaction details |

---

## 🛠️ Tech Stack

- [CrewAI](https://crewai.com) — Multi-agent orchestration
- [Python 3.10+](https://python.org)
- [Unipile API](https://unipile.com) — LinkedIn messaging
- [Google Apps Script](https://script.google.com) — Sheets integration
- [Google Sheets](https://sheets.google.com) — Interaction logging

---

## ⚙️ Setup & Configuration

Set the following environment variables:

```env
UNIPILE_API_KEY=your_unipile_api_key
UNIPILE_DSN=your_unipile_dsn_url
UNIPILE_ACCOUNT_ID=your_unipile_account_id
APPS_SCRIPT_URL=your_google_apps_script_web_app_url
```

---

## 🚀 How It Works

1. Unipile detects a new LinkedIn message and sends a webhook payload
2. The **Classifier Agent** reads the message and assigns a category
3. The **Voice Agent** drafts a reply following Siva's persona rules
4. The **Dispatcher** sends the reply back via Unipile's API
5. The **Logger** records everything to Google Sheets

---

## 👤 Author

**Siva Mallikarjun Parvatham**  
Senior Software Developer & GenAI Specialist @ Wipro, Hyderabad  
[LinkedIn](https://linkedin.com/in/siva-mallikarjun-parvatham)

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/siva_linkedin_ai_responder/config/agents.yaml` to define your agents
- Modify `src/siva_linkedin_ai_responder/config/tasks.yaml` to define your tasks
- Modify `src/siva_linkedin_ai_responder/crew.py` to add your own logic, tools and specific args
- Modify `src/siva_linkedin_ai_responder/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the siva_linkedin_ai_responder Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The siva_linkedin_ai_responder Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the SivaLinkedinAiResponder Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

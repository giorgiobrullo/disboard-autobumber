# Disboard Auto-Bumper

Automatically send bump messages to multiple servers using the `discord.py-self` library. This bot automates the process of sending bump commands to each configured server with a 20-minute interval between bumps. A fork of kiyoopoon's [multiserver-bumper](https://github.com/kiyoopoon/multiserver-bumper).

⚠ Important Disclaimer: This bot operates as a self-bot, which is a violation of Discord's Terms of Service. Using a self-bot can result in account suspension or termination. I strongly recommend using a secondary or disposable account, rather than your primary account.

## Features
- Bumps all your configured servers at regular intervals.
- Logs bump actions in a designated log channel.

## Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/giorgiobrullo/disboard-autobumber.git
   cd your-repo
   ```

2. **Configure the Bot:**
   - Create a `.env` file in the root directory with the following variables:
     ```
     DISCORD_TOKEN=your_token_here
     CHANNEL_IDS=channel_id_1,channel_id_2,...
     LOG_CHANNEL=log_channel_id
     ```

3. **Install Dependencies:**
   If you're not using Docker, install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Bot

### Recommended: Docker

To simplify deployment, it's recommended to use Docker. After configuring the `.env` file, you can run the bot using Docker with these commands:

1. Build the Docker container:
   ```sh
   docker build -t disboard-bumper .
   ```

2. Run the Docker container:
   ```sh
   docker run --env-file .env disboard-bumper
   ```

### Option 2: Manual Setup (Not Recommended)

If Docker is not available or preferred, you can run the bot manually:

1. Create and activate a virtual environment:
   - **Linux/Mac:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```sh
     python -m venv venv
     venv\Scripts\activate.bat
     ```

2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the bot:
   ```sh
   python main.py
   ```
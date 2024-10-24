ValoBot – AI-Powered Valorant Esports Team Builder
ValoBot is an AI-driven chatbot designed to help Valorant esports managers create well-balanced, strategic teams. It leverages player performance data and role-based metrics to recommend optimal team compositions for different scenarios, without showing personal player data.

Table of Contents
Inspiration
Features
Technologies Used
How ValoBot Works
Setup and Installation
Usage
Challenges and Learnings
Contributing


Inspiration
Valorant esports managers face a complex task when building teams—balancing roles, assessing player synergy, and ensuring teams fit well on specific maps. ValoBot was inspired by the need to streamline this process by providing AI-powered team-building recommendations that focus on role-based performance and team dynamics.

Features
AI-Driven Team Building: Suggests optimal team compositions based on player roles (Duelist, Controller, Initiator, Sentinel) and synergy between roles.
Map-Specific Strategy: Recommends teams based on performance trends on different Valorant maps.
Role-Based Analysis: Focuses on the overall balance of team roles to create strong, synergistic lineups.
No Personal Data Required: Does not display or rely on personal player information; uses aggregated stats and role-based data for recommendations.
Technologies Used
AWS Bedrock: Powers the core AI capabilities for natural language processing and generating team recommendations.
Python: Primary language for building the AI logic and processing the data.
Chatbot Framework: Enables interactive conversations with esports managers for team-building suggestions.

How ValoBot Works
ValoBot uses AI models to analyze aggregated match data and make team composition suggestions. Here’s how it works:

Role Data Analysis: It looks at the aggregated performance of different roles (Duelists, Controllers, Initiators, and Sentinels) to recommend balanced teams.
Map-Specific Adjustments: ValoBot tailors its recommendations based on specific maps, analyzing performance trends and role success on each map.
Team Synergy: The AI ensures that the recommended teams have strong synergy, focusing on how roles interact and complement one another.
Chatbot Interface: Managers interact with ValoBot via a chatbot, where they can request team suggestions, get role breakdowns, and refine team setups for specific maps or playstyles.
Setup and Installation
Prerequisites:
Python 3.x
AWS Account with access to Bedrock, EC2, S3, RDS, and Lambda.
Install required Python libraries:
bash
Copy code
pip install -r requirements.txt
Steps:
Clone the Repository:

bash
Copy code
git clone https://github.com/Prashant1659/valorant-chatbot.git
cd chatbot
Set Up AWS Services:

Launch EC2 instances and configure S3, RDS, and Lambda.
Set up AWS Bedrock for the AI components.
Configure Environment Variables: Set up your AWS credentials and database connection strings in a .env file or export them as environment variables.

Run the Application:

Start the backend:
bash
Copy code
python app.py
Access ValoBot via the chatbot interface or integrate with your preferred platform (Discord, Slack, etc.).
Usage
To interact with ValoBot:

Ask for a team composition:
"Build Pro- Team"

Challenges and Learnings
Team Synergy Complexity: We learned that team performance depends heavily on synergy between roles, and not just individual skill levels. This shaped how ValoBot evaluates and suggests team lineups.
Handling Data without Personal Info: A key challenge was building a powerful AI without using personal player data. By focusing on aggregated and role-based data, we ensured ValoBot remained useful while maintaining data privacy.
Real-Time Adjustments: The project required refining the AI’s ability to make real-time adjustments based on map performance and role success.

Contributing
Contributions are welcome! Please follow these steps to contribute:
Fork the project.
Create a new branch.
Make your changes and test them.
Submit a pull request.
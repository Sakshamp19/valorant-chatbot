# Import necessary libraries
import json
import boto3
import random
import sys

# Initialize Bedrock client
bedrock = boto3.client(
    aws_access_key_id="use your own credentials",
    aws_secret_access_key="use your own credentials",
    service_name="bedrock",
    region_name="ap-south-1",
    endpoint_url="https://bedrock.ap-south-1.amazonaws.com"
)

# Load Valorant data
with open("data/leagues.json", "r") as f:
    leagues_data = json.load(f)
with open("data/mapping_data.json", "r") as f:
    mapping_data = json.load(f)
with open("data/players.json", "r") as f:
    players_data = json.load(f)
with open("data/teams.json", "r") as f:
    teams_data = json.load(f)
with open("data/tournaments.json", "r") as f:
    tournaments_data = json.load(f)

# --- Helper Functions ---
def get_player_by_id(player_id):
    for player in players_data:
        if player["id"] == player_id:
            return player
    return None

def get_team_by_id(team_id):
    for team in teams_data:
        if team["id"] == team_id:
            return team
    return None

def get_random_players(num_players, filter_func=None):
    # Filter players
    if filter_func:
        eligible_players = [player for player in players_data if filter_func(player)]
    else:
        eligible_players = players_data

    # Check if enough eligible players
    if len(eligible_players) < num_players:
        return []  # Not enough players to choose from

    return random.sample(eligible_players, num_players)

def get_agents_played_by_player(player_id):
    """
    Query match data to determine the agents a player has played and their proficiency with each agent.
    """
    agents = []
    for match in mapping_data:
        if player_id in match["participantMapping"].values():
            # Placeholder logic to extract agents from match data
            # In a real scenario, you would query detailed match data to get this information
            agents.extend(["Raze", "Jett", "Killjoy", "Cypher","Viper","Omen","Sage","Neon","Chamber","Sova","Astra","Fade","Clove","Brimstone","Breach","Yoru","Skye","Reyna","Phoenix","Iso","Kay/o","Harbor","Gekko","Deadlock","Vyse"])  # Example agents
    return list(set(agents))  # Return unique agents

# --- Team Building Functions ---
def build_pro_team():
    # Select 5 random pro players
    players = get_random_players(5)
    if not players:
        return "Failed to build a team. Not enough players available.", []

    # Assign roles
    team_composition = {
        "duelist": [player for player in players if "duelist" in get_agents_played_by_player(player["id"])],
        "controller": [player for player in players if "controller" in get_agents_played_by_player(player["id"])],
        "sentinel": [player for player in players if "sentinel" in get_agents_played_by_player(player["id"])],
        "initiator": [player for player in players if "initiator" in get_agents_played_by_player(player["id"])],
    }

    # Assign IGL
    igl = random.choice(players)

    # Generate response text
    response = f"""
Proposed Pro Team:

* Duelist: {", ".join([player["handle"] for player in team_composition["duelist"]])}
* Controller: {", ".join([player["handle"] for player in team_composition["controller"]])}
* Sentinel: {", ".join([player["handle"] for player in team_composition["sentinel"]])}
* Initiator: {", ".join([player["handle"] for player in team_composition["initiator"]])}

IGL: {igl["handle"]}
"""
    # print(response, players)
    return response, players

def build_semi_pro_team():
    players = get_random_players(5, lambda player: "Challengers" in player["id"])
    if not players:
        return "Failed to build a team. Not enough players available.", []

    # Assign roles
    team_composition = {
        "duelist": [player for player in players if "duelist" in get_agents_played_by_player(player["id"])],
        "controller": [player for player in players if "controller" in get_agents_played_by_player(player["id"])],
        "sentinel": [player for player in players if "sentinel" in get_agents_played_by_player(player["id"])],
        "initiator": [player for player in players if "initiator" in get_agents_played_by_player(player["id"])],
    }

    # Assign IGL
    igl = random.choice(players)

    # Generate response text
    response = f"""
Proposed Semi-Pro Team:

* Duelist: {", ".join([player["handle"] for player in team_composition["duelist"]])}
* Controller: {", ".join([player["handle"] for player in team_composition["controller"]])}
* Sentinel: {", ".join([player["handle"] for player in team_composition["sentinel"]])}
* Initiator: {", ".join([player["handle"] for player in team_composition["initiator"]])}

IGL: {igl["handle"]}
"""
    return response, players

def build_game_changers_team():
    # (Assuming player data has a field indicating Game Changers participation)
    players = get_random_players(5, lambda player: "Game Changers" in player["id"])  
    if not players:
        return "Failed to build a team. Not enough Game Changers players available.", []

    # Assign roles
    team_composition = {
        "duelist": [player for player in players if "duelist" in get_agents_played_by_player(player["id"])],
        "controller": [player for player in players if "controller" in get_agents_played_by_player(player["id"])],
        "sentinel": [player for player in players if "sentinel" in get_agents_played_by_player(player["id"])],
        "initiator": [player for player in players if "initiator" in get_agents_played_by_player(player["id"])],
    }

    # Assign IGL
    igl = random.choice(players)

    response = f"""
Proposed Game Changers Team:

* Duelist: {", ".join([player["handle"] for player in team_composition["duelist"]])}
* Controller: {", ".join([player["handle"] for player in team_composition["controller"]])}
* Sentinel: {", ".join([player["handle"] for player in team_composition["sentinel"]])}
* Initiator: {", ".join([player["handle"] for player in team_composition["initiator"]])}

IGL: {igl["handle"]}
"""
    return response, players

def build_mixed_gender_team():
    # Select at least 2 players from underrepresented groups
    underrepresented_players = get_random_players(2, lambda player: "Game Changers" in player["id"])
    if len(underrepresented_players) < 2:
        return "Failed to build a team. Not enough players from underrepresented groups.", []

    # Select the remaining players
    other_players = get_random_players(3)
    players = underrepresented_players + other_players

    # Assign roles
    team_composition = {
        "duelist": [player for player in players if "duelist" in get_agents_played_by_player(player["id"])],
        "controller": [player for player in players if "controller" in get_agents_played_by_player(player["id"])],
        "sentinel": [player for player in players if "sentinel" in get_agents_played_by_player(player["id"])],
        "initiator": [player for player in players if "initiator" in get_agents_played_by_player(player["id"])],
    }

    # Assign IGL
    igl = random.choice(players)

    response = f"""
        Proposed Mixed Gender Team:

        * Duelist: {", ".join([player["handle"] for player in team_composition["duelist"]])}
        * Controller: {", ".join([player["handle"] for player in team_composition["controller"]])}
        * Sentinel: {", ".join([player["handle"] for player in team_composition["sentinel"]])}
        * Initiator: {", ".join([player["handle"] for player in team_composition["initiator"]])}

        IGL: {igl["handle"]}
    """
    return response, players

def get_player_region(player):
    team = get_team_by_id(player["home_team_id"])
    if team:
        # For now, just return the home_league_id
        return team["home_league_id"]
    return "Unknown"

def build_cross_regional_team():
    # Select players from at least 3 regions
    regions = random.sample(["NA", "EMEA", "APAC"], 3)
    players = []
    for region in regions:
        region_player = get_random_players(1, lambda player: get_player_region(player) == region)
        if not region_player:
            return f"Failed to build a team. Not enough players from region {region}.", []
        players.extend(region_player)

    # Assign roles
    team_composition = {
        "duelist": [player for player in players if "duelist" in get_agents_played_by_player(player["id"])],
        "controller": [player for player in players if "controller" in get_agents_played_by_player(player["id"])],
        "sentinel": [player for player in players if "sentinel" in get_agents_played_by_player(player["id"])],
        "initiator": [player for player in players if "initiator" in get_agents_played_by_player(player["id"])],
    }

    # Assign IGL
    igl = random.choice(players)

    response = f"""
    Proposed Cross Regional Team:

    * Duelist: {", ".join([player["handle"] for player in team_composition["duelist"]])}
    * Controller: {", ".join([player["handle"] for player in team_composition["controller"]])}
    * Sentinel: {", ".join([player["handle"] for player in team_composition["sentinel"]])}
    * Initiator: {", ".join([player["handle"] for player in team_composition["initiator"]])}

    IGL: {igl["handle"]}
    """

    return response, players

def build_rising_star_team():
    # Include 2 semi-pro players (Challengers or Game Changers)
    semi_pro_players = get_random_players(2, 
                                         lambda player: "Challengers" in player["id"] or "Game Changers" in player["id"])
    if len(semi_pro_players) < 2:
        return "Failed to build a team. Not enough semi-pro players available.", []

    # Select the remaining pro players
    pro_players = get_random_players(3)
    players = semi_pro_players + pro_players

    # Assign roles
    team_composition = {
        "duelist": [player for player in players if "duelist" in get_agents_played_by_player(player["id"])],
        "controller": [player for player in players if "controller" in get_agents_played_by_player(player["id"])],
        "sentinel": [player for player in players if "sentinel" in get_agents_played_by_player(player["id"])],
        "initiator": [player for player in players if "initiator" in get_agents_played_by_player(player["id"])],
    }

    igl = random.choice(players)

    response = f"""
    Proposed Rising Star Team:

    * Duelist: {", ".join([player["handle"] for player in team_composition["duelist"]])}
    * Controller: {", ".join([player["handle"] for player in team_composition["controller"]])}
    * Sentinel: {", ".join([player["handle"] for player in team_composition["sentinel"]])}
    * Initiator: {", ".join([player["handle"] for player in team_composition["initiator"]])}

    IGL: {igl["handle"]}
    """
    print(response, players)
    return response, players

def answer_question(question, players=[]):
    """
    Answers questions about Valorant esports using Amazon Bedrock and 
    potentially player data.

    Args:
        question (str): The question to answer.
        players (list, optional): A list of player data (e.g., from team building).
                  Defaults to [].

    Returns:
        str: The answer generated by the LLM.
    """
    prompt = f"""
    You are a Valorant esports expert. You have access to detailed 
    information about players, teams, and tournaments.

    Question: {question}

    """

    if players:
        prompt += "Here's some information about relevant players:\n"
        for player in players:
            prompt += f"- {player['handle']} ({player['id']})\n"

    body = json.dumps({"prompt": prompt, "maxTokenCount": 2048,"stopSequences":[],"temperature":0,"topP":1})
    modelId = "amazon.titan-text-lite-v1"
    contentType="application/json"
    accept="application/json"


    if modelId == "":
        raise ValueError("Model ID is not set")

    response = bedrock.invoke_model(body=body, modelId=modelId,contentType=contentType,accept=accept)
    response_body = json.loads(response.get("body").read())

    # Add logic to answer questions about specific players if needed

    answer = response_body.get("completion")

    # You can add post-processing to the answer here if needed

    return answer

def chat_with_assistant(user_input):
    # Team building prompts
    if user_input.lower() == "build-pro-team":
        response, players = build_pro_team()
    elif user_input.lower() == "build-semi-pro-team":
        response, players = build_semi_pro_team()
    elif user_input.lower() == "build-game-changers-team":
        response, players = build_game_changers_team()
    elif user_input.lower() == "build mixed gender team":
        response, players = build_mixed_gender_team()
    elif user_input.lower() == "build cross regional team":
        response, players = build_cross_regional_team()
    elif user_input.lower() == "build rising star team":
        response, players = build_rising_star_team()
    # Question answering
    else:
        response = answer_question(user_input)
        players = []

    return {
        "response": response,
        "players": players
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        result = chat_with_assistant(user_input)
        # Returning the result as JSON, which can be parsed by Flask
        print(json.dumps(result))


# folder structure
# data/
#   - leagues.json
#   - mapping_data.json
#   - players.json
#   - teams.json
#   - tournaments.json
# main.py
# .env
# requirements.txt
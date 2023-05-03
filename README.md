# Slack Japanese Letter Bot
This Python script is a Slack bot that generates random Japanese letters, expressions and numbers, tags a user and sends them to a Slack channel every day at predifined time (soon random).
The bot utilizes the schedule library to schedule the message and the slack_sdk library to send the message to the Slack channel.

## Getting Started
First, to use the slack bot you'll need to have a token for the slack web client, to get that tokken please head to: https://api.slack.com/
register your bot and recive a bot tokken, the token should look as such: xoxb-12341...
Once you have the bot tokken please open a terminal and export the bot tokken as an enviorment variable, as such (change the <token> to bot token):
export SLACK_BOT_TOKEN="<token>"
Also, make sure you have the needed dependencies: slack_sdk and schedule. If not, please run: pip install <dependency>.

### Usage
simply run the python file

more ideas to come

# CIPs Twitter Bot

A basic twitter bot that follows the [CIPs repository](https://github.com/cardano-foundation/CIPs) and tweets notable events.

See [x.com/cip_updates](https://x.com/cip_updates).

See [developer.x.com](https://developer.x.com/en/portal/dashboard).

## Aims

- tweets when there are pull requests
- tweets when only new CIP pull requests
- tweets when new CIPs merged

### Steps to achieve

- get secrets handled in a sensible way
- get code detecting [new PRs on test repo](https://github.com/Ryun1/test-temp-repo)
- get code tweeting
- get PR tweets looking nice and sensible
- get a couple basic workflows setup
- wrap up everything in a docker container
- make the bot look pretty

## Setup

```shell
pip install tweepy requests
```

### Run 

```shell
python ./src/bot.py
```
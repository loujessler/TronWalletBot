## Installing on a local machine

### Clone repo
```shell
git clone git@github.com:loujessler/TronWalletBot.git
```

### Initialize environment and install dependencies:
```bash
pip install -r requirements.txt
```

### Run containers with db, redis and tor
```shell
docker-compose -f docker-compose.yml -p tron_wallet_bot up
```
### Create .env file and copy variables from .env-example
```shell
cp .env-example .env
```

# FASTAPI-ONION

# ディレクトリ構成
```
├── src  
│   ├── domain         # ドメイン層  
│   ├── usecase        # ユースケース層  
│   ├── presentation   # プレゼンテーション層  
│   ├── infrastructure # インフラストラクチャ層  
│   └── main.py        # エントリーポイント  
```

# Run server
docker compose up -d

# Access server

## POST
curl -X POST -H "Content-Type: application/json" -d '{"title": "My Task", "description": "Task details"}' http://localhost:8000/tasks

curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "title": "My Task", "description": "Task details"}' http://localhost:8000/tasks

## GET
curl http://localhost:8000/tasks/1

## Database
SQLite ?

# Shutdown server
docker compose down

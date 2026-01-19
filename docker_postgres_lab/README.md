# docker_postgres_lab

Docker Compose setup voor een PostgreSQL database container.

## 📋 Structuur

```
docker_postgres_lab/
├── docker-compose.yml    # Orchestratie van PostgreSQL container
├── Dockerfile            # Custom PostgreSQL image met init script
├── init.sql              # Maakt tabellen aan + test data (users & products)
├── .env.example          # Template voor environment variabelen
└── README.md             # Deze documentatie
```
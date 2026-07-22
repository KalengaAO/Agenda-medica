NAME            = agenda-medica

COMPOSE_FILE    = src/docker-compose.yml

all: up

up:
	@docker compose -f $(COMPOSE_FILE) up -d --build

down:
	@docker compose -f $(COMPOSE_FILE) down

logs:
	@docker compose -f $(COMPOSE_FILE) logs -f

clean:
	@docker compose -f $(COMPOSE_FILE) down

fclean: clean
	@docker compose -f $(COMPOSE_FILE) down -v --rmi local
	@docker system prune -f

re: fclean up

.PHONY: all up down logs clean fclean re
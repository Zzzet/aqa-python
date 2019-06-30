# aqa-python
docker-compose run ui-tests pytest test/selenium_tests -H selenoid -P 4444
# docker-compose run ui-tests source venv/bin/activate; pytest -H selenoid -P 4444

docker-compose build
docker-compose up -d --force-recreate --build   
docker-compose up
docker inspect $c1 -f "{{json .NetworkSettings.Networks }}"
docker network ls
docker network inspect aqa-python_ntw-123 -f "{{json .Containers }}"
docker ps -q | xargs -I {} docker inspect {} -f "{{json .NetworkSettings.Networks }}"
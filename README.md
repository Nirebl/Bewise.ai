# Bewise.ai
test task for the vacancy python (junior)


## Порядок запуска
1. иметь файл .env, например:


    DBS_USER=postgres

    DBS_PASS=easy_pass 

    DBS_URL=bewise_ai_dbs:5432


2. собрать докер через docker-compose up -d 
(возможна вариация docker compose up -d) 
(можно добавить флаг --build чтобы пересобрать)
3. обращаться на localhost:8000/questions/ запросом post


      пример запроса
      url = localhost:8000/questions/
      json={"questions_num": 5} 
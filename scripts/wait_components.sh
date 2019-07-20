dockerize -wait tcp://db:5432 -wait tcp://broker:5672 -timeout 60s

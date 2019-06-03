## Usage
run `sudo docker-compose up -d` in the `/vagrant/database` directory.

The `docker-entrypoint-initdb.d` folder will only be run once while the container is instantiated, so use `sudo docker-compose down -v` to stop & remove the image in order to re-activate this for the next run.

## Notes:
Grabbed connector from `https://dev.mysql.com/downloads/connector/python/` on Windows.
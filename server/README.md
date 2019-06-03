# Server

## Running on dev-box

`cd ./vagrant/server`
`mvn package`
`java -jar target/pick1-0.0.1-SNAPSHOT.jar`

## Images

This is a can of worms, but as of right now you can build and fire up the jar (requires waiting ~15min) and navigate to something like `http://192.168.33.10:8080/images/lea/001-Animate-Wall.jpeg` to see an image. This is the serving static content approach.
# guil test


you can run this app with docker

- build app
```
make build
```

- run app
```
make up
```

when the app is running you can visit the next url for endpoint documentation
http://localhost:8000/docs

there is only an endpoint with many parameters for each feature:

`http://localhost:8000/get_by/popularity`

`http://localhost:8000/get_by/duration`

`http://localhost:8000/get_by/year`

these endpoints allow the `order` parameter for get movies orderer ascending or descending

`http://localhost:8000/get_by/actor`

this endpoint require the `actor_name` parameter for get movies by actor

`http://localhost:8000/get_by/similar`

this endpoint require the `movie_name` parameter for get similar movies by movie

- run tests
``` 
make test
```
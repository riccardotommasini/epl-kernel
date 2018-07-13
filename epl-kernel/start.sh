#! /bin/bash
docker build -t eplkernel .
export EPL=$(docker run -d -p 8888:8888 --rm -v $(PWD):/home/jovyan/work eplkernel)
docker exec -it ${EPL} /bin/bash
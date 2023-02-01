### DEFINITION OF VARIABLES

IMAGE_TAG="powerplant_app"
CONTAINER_NAME="powerplant_app"
DOCKERFILE_PATH="./code/"
PORT=8888
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

### BUILD OF THE DOCKERFILE

# First, we check if the image called after $IMAGE_TAG exists in the docker list. If not, we will build it
if [[ $(docker image ls | grep -w $IMAGE_TAG) == "" ]];
    then echo "Preparing to build image...";
    docker build -t $IMAGE_TAG $DOCKERFILE_PATH;
fi;

clear

### RUN THE CONTAINER

# Once we're sure the image exists and is well built, we can run the container with "docker run" command
# Again, we will check that the container is not already running!
if ! [[ $(docker ps -a | grep -w $CONTAINER_NAME) == "" ]];
    then echo -e "${RED}The container is already running, it will be restarted${NC}";
    docker stop $CONTAINER_NAME >/dev/null
    docker rm $CONTAINER_NAME >/dev/null;
fi;

docker run --name $CONTAINER_NAME -dp $PORT:$PORT $IMAGE_TAG >/dev/null
echo -e "${GREEN}The container is running!${NC}"
sleep 1


### HELPING THE USER TO USE THE ENDPOINT

echo -e "You can try the endpoint by using the payloads in the folder example_payloads. For example, you can use this command:\n"
echo 'curl 0.0.0.0:8888/productionplan -X post -H "Content-Type: application/json" -d @example_payloads/payload1.json'
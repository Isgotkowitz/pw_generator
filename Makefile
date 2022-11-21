
run:
	python3 pw_generator.py

pwgen-build:
	sudo docker build -t pwgen-image . 

pwgen-run:
	sudo docker run --rm --name pwgen pwgen-image

mongosh-run:
	sudo docker exec -it mongo-container mongosh

activate:
	source ~/envs/docker_env/bin/activate

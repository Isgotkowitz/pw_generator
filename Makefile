
run:
	python3 pw_generator.py

pwgen-build:
	sudo docker build -t pwgen-image . 

pwgen-run:
	sudo docker run --link 502c51dd50cc:502c51dd50cc --rm --name pwgen pwgen-image

mongosh-run:
	sudo docker exec -it mongo-container mongosh

activate:
	source ~/envs/docker_env/bin/activate

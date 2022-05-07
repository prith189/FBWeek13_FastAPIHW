# FBWeek13_FastAPIHW
Items covered in this repo
- A FastAPI based server that can perform sentiment analysis 
- A dockerfile which can be used to build a docker image that runs the server directly upon running the docker image

Build the docker image using:
sudo docker run -it --rm --name my-running-app dockerfile

Run the docker image using:
sudo docker run -it --rm --name my-running-app dockerfile

Upon running the docker image, the FastAPI server should start directly. Here is a snapshot when the docker image was run:
![image](https://user-images.githubusercontent.com/9631296/167274637-9de5376c-2b40-4fc3-b764-8c9d77c8f2c0.png)


Also a snapshot of the API validation which shows that the sentiment was returned correctly:
![image](https://user-images.githubusercontent.com/9631296/167274728-49d2453a-12df-42da-bd33-8747181ee3d9.png)

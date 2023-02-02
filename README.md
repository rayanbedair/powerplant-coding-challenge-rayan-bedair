# powerplant-coding-challenge

## Welcome !

The goal of this coding challenge is to calculate how much power each of a multitude of different powerplants need to produce (a.k.a. the production-plan) when the load is given and taking into account the cost of the underlying energy sources (gas, kerosine) and the Pmin and Pmax of each powerplant.  

Since time is scarce, applicants are asked not to spend more than 4 hours on this challenge, I have respected the deadlines (I just took my dinner and went back home, which explains the 5 hours gap between my commits).

## Who am I

I am Rayan BEDAIR, a student finishing his Master in France, at ESILV. I am specialized in "**Informatique, Objets connectés et Sécurité**" (IoT and Cybersecurity), but I have to say I prefer programming and doing DevOps.

## The challenge

### Technologies used

This challenge has been made using:
- Python 3.8, with the library Flask (for the creation of the `/productionplan` endpoint);
- Docker (in order to give a containerized solution to this challenge);
- Shell (to build and run the container).

### Requirements

To make this project run correctly, you will only need Docker. Also, put yourself in the `docker` group (so you don't have to use the sudo command all the time):
```shell
sudo apt-get install -y docker docker.io
sudo usermod -aG docker $USER
```

### How to execute the project

I know, I know, I know, ... You're only here because this is the part you're interested in. Here is how to run the project:
```shell
./start.sh
```

Yes, only one line. Have fun!

### Ok but how does it work?

Well, firstly, the script will build the Dockerfile stored in the code/ folder. Then, it will run it, and finally, it will explain how you can make your POST request (just copy and paste the command given).

### Results

Here are the results with the payloads examples.
This photo is the basic dislpay results:
![alt text](Capture%20d'écran_20230202_005742.png)

This photo is the results with the cost of emission and cost of power:
![alt text](Capture%20d'écran_20230202_005857.png)

## More information

If you need any complementary information, you can contact me at bedair.rayan@gmail.com.
Thank you very much for the time you have spent reading and studying my application.
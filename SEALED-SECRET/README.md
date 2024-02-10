***AUTO-GENERATE SEALED SECRET***

This script generates a Kubernetes sealed secret(using kubeseal) from a .env file or input from a user. It saves the encoded(dealed-secret) data in a .txt file.

Pre-requisites;
1. Kubernetes Cluster up and Running
2. Sealed-Secret installed on kubernetes Cluster
3. Kubeseal CLI tool installed on your machine
4. Python 3.*.* installed on your machine

NOTE: This program should be ran in the directory you want your sealed-secret manifest to be stored.

**Usage**

1. Clone or extract the `secret-script.py` from this repo.
2. Run the programm using the command below;

`python3 secret-script.py`

3. Read carefuly and Follow intructions which will be prompted to you in your terminal.


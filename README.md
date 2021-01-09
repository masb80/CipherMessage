# Encrypt and Decrypt
Write a program that allows a user to encrypt and decrypt a message.

## Functionalities
In this task, I developed a code where a user can input a message(after running the code) and after hit enter he can see the encrypted and decrypted version of his message. This message accept the HTML special characters and also Unicode too. 

## Installation
Due to encryption and decryption libraries changes according to the python version, I have created a docker image for the python script which is versions and platform independent.

## Run
```bash
docker build -t 'chypermessage_python3' .
docker run -it 'chypermessage_python3'
```
## Run without Docker
```python
python3 chypermessage_python3.py
```
(python3 shoud support only 3.5 version)

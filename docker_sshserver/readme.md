# SSH Connection between Two Containers 

## 1. Overview
- This project contains docker files which are configured in such a way that we can connect to remote client without password authentication
- we create two docker images
    - ssh server : This is the ansible server
    - remote server : Remote server or client machine

## 1.1. SSH Server Setup
- Dockerfile for this container is under the folder ssh_server
- The docker file uses Ubuntu
- And it is configured in such a way that the image generates the RSA keypair for ssh connection

### 1.2. Build SSH Server Image from Docker file
- Building an image using below command
<br>
```docker build -t <imagename> . ```

### 1.3 Running a Container from the image
- I suggest to deploy container new network instead of default one.
- ``` docker run -d --name <name of container> -network <network> <image name>```

- By completing the above step we have the SSH server with key pair will be up and running

## 2. Pipeline command to get Docker Public Key
- Once our SSH server is up we can copy the public key using below command

- ``` docker cp <ssh_server_containername>:/home/remote_user/.ssh/id_rsa.pub /remote_user/id_rsa```

- Note : Make sure that the public key is copied to remote_server repo so that remote_server Docker file can use it during container creation

## 3. Client Setup 
- Docker file under remote_server folder is used to create n number of clients which can be accessed by SSH server without password using SSH Key pair. 

## 3.1 Building Client image
- Make sure you have the public key in the remote_server folder which you copied from previous step
-  ```docker build -t <imagename> . ```

## 3.2 Create Container from Image
 - ``` docker run -d --name <name of container> -network <network> <image name>```

- <b>All the clients creted using this image can be accessed by our SSH server using without password<b>

## 4. Testing
### 4.1 Direct SSH Test
- Get the ip address of the client using "docker inspect" and use below command to test the connection
- ```ssh -i /home/remote_user/.ssh/id_rsa -o "StrictHostKeyChecking=accept-new" remote_user@<ipaddress of client container> ```
- <b> Note: We enable host key check and it adds any new host keys to known hosts<b>

### 4.2 Via Ansible Skipping Host key check
- Configure ansible.cfg with below option
    - host_key_checking = False
- then create playbook and run with key file arg
- Example:
    - ``` ansible-playbook test.yml --key-file /home/remote_user/.ssh/id_rsa```
- Or we can configure all keyfile in ansible.cfg and direclty run it.

### 4.3 With Host key Checking
- We can also enable host key checking and perform ssh conneciton by adding below args to ansible.cfg or inventory folder
- ssh_args = -C StrictHostKeyChecking=accept-new
- Reference Document
    https://stackoverflow.com/questions/23074412/how-to-set-host-key-checking-false-in-ansible-inventory-file

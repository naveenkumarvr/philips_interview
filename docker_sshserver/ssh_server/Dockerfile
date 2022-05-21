FROM ubuntu:latest

RUN mkdir -p /var/run/sshd

RUN apt update && \
    apt install -y openjdk-8-jdk && \
    apt install -y openssh-server

RUN apt install -y python3-pip
RUN pip install ansible

RUN useradd -rm -d /home/remote_user -s /bin/bash remote_user && \
    echo remote_user:password@123 | chpasswd


RUN mkdir /home/remote_user/.ssh  && \
    chmod 700 /home/remote_user/.ssh


RUN chown remote_user:remote_user -R /home/remote_user/.ssh 

USER remote_user

RUN ["/bin/bash", "-c", "ssh-keygen -t rsa -N '' -f /home/remote_user/.ssh/id_rsa <<< y" ]

USER root

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
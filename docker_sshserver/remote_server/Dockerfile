FROM ubuntu:latest

RUN mkdir -p /var/run/sshd

RUN apt update && \
    apt install -y openjdk-8-jdk && \
    apt install -y openssh-server

RUN useradd -rm -d /home/remote_user -s /bin/bash remote_user && \
    echo remote_user:password@123 | chpasswd


RUN mkdir /home/remote_user/.ssh  && \
    chmod 700 /home/remote_user/.ssh

COPY id_rsa.pub /home/remote_user/.ssh/authorized_keys

RUN chown remote_user:remote_user -R /home/remote_user/.ssh &&  \
    chmod 600 /home/remote_user/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
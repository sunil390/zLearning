# Node-red in Kubernetes

## podman image for znext
1. git clone https://github.com/node-red/node-red-docker.git
2. cd node-red-docker/docker-custom
3. Create Containerfile
```.py
#### Stage BASE ########################################################################################################
FROM amd64/node:18-bullseye-slim AS base

# Copy scripts
COPY scripts/*.sh /tmp/

# Install tools, create Node-RED app and data dir, add user and set rights
RUN set -ex && \
    apt-get update && apt-get install -y \
        bash \
        tzdata \
        curl \
        nano \
        wget \
        git \
        openssl \
        openssh-client \
        ca-certificates && \
    mkdir -p /usr/src/node-red/.ssh /data /usr/share/ansible/collections && \
    deluser --remove-home node && \
    useradd --home-dir /usr/src/node-red --uid 1000 node-red && \
    chown -R node-red:root /data && chmod -R g+rwX /data && \
    chown -R node-red:root /usr/src/node-red && chmod -R g+rwX /usr/src/node-red && \
    chown -R node-red:root /usr/share/ansible/collections && chmod -R g+rwX /usr/share/ansible/collections

# Set work directory
WORKDIR /usr/src/node-red

# Setup SSH known_hosts file
COPY known_hosts.sh .
RUN ./known_hosts.sh /etc/ssh/ssh_known_hosts && rm /usr/src/node-red/known_hosts.sh && \
COPY id_rsa /usr/src/node-red/.ssh/id_rsa
RUN echo "PubkeyAcceptedKeyTypes +ssh-rsa" >> /etc/ssh/ssh_config

# package.json contains Node-RED NPM module and node dependencies
COPY package.json .
COPY flows.json /data
COPY scripts/entrypoint.sh .

#### Stage BUILD #######################################################################################################
FROM base AS build

# Install Build tools
RUN apt-get update && apt-get install -y build-essential python && \
    npm install --unsafe-perm --no-update-notifier --no-fund --only=production && \
    npm uninstall node-red-node-gpio && \
    cp -R node_modules prod_node_modules

#### Stage RELEASE #####################################################################################################
FROM base AS RELEASE

COPY --from=build /usr/src/node-red/prod_node_modules ./node_modules

# Chown, install devtools & Clean up
RUN chown -R node-red:root /usr/src/node-red && \
    apt-get update && apt-get install -y build-essential python-dev python3.9 python3-pip && \
    python3 -m pip install --upgrade pip ebcdic tnz ansible && \
    ansible-galaxy collection install community.general ansible.utils ibm.ibm_zos_core:==1.6.0-beta-1 -p /usr/share/ansible/collections && \
    npm install jmespath node-red-contrib-alexa-remote2-applestrudel \
    node-red-contrib-bard \
    node-red-contrib-credentials \
    node-red-contrib-google-sheets \
    node-red-contrib-play-audio \
    node-red-contrib-string \
    node-red-dashboard \
    node-red-contrib-web-worldmap && \
    rm -r /tmp/*

RUN npm config set cache /data/.npm --global

USER node-red

# Env variables
ENV NODE_RED_VERSION=3.0.2 \
    NODE_PATH=/usr/src/node-red/node_modules:/data/node_modules \
    PATH=/usr/src/node-red/node_modules/.bin:${PATH} \
    FLOWS=flows.json

# Expose the listening port of node-red
EXPOSE 1880

ENTRYPOINT ["./entrypoint.sh"]
```
4. podman build -t node-red-znext:v1 .
5. podman tag localhost/node-red-znext:v1 sunil390/node-red-znext:v1
6. podman push sunil390/node-red-znext:v1
7. edit ~/node-red/deployment.yaml and point to node-red-znext:v1
8. kubectl apply -k node-red
9. Restart Server.

## podman image cleanup
1. podman images
2. podman rmi 
3. list external containers -> podman ps -a --external
4. Force remove container -> podman rm f684cd3e44cd --force


## http Basic Auth Enablement

1. sudo npm install -g --unsafe-perm node-red
2. node-red admin hash-pw
3. update /data/nodered/settings.js with the hash-pw
```
    adminAuth: {
        type: "credentials",
        users: [{
            username: "admin",
            password: "hash pw output for adnin ",
            permissions: "*"
        }]
    },

    httpNodeAuth: {user:"zuser",pass:"hash-pw out for the password of zuser"},
    httpStaticAuth: {user:"zuser",pass:"hash-pw out for the password of zuser"},
```

## New container image with pip3 ebcdic and tnz 

1. Create Containerfile
```
FROM nodered/node-red-dev:v3.1.0-beta.2-debian
USER root
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install ebcdic tnz
RUN usermod -aG dialout node-red
USER node-red

Or with Single RUN Command

FROM nodered/node-red-dev:v3.1.0-beta.2-debian
USER root
RUN apt-get update && apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip ebcdic tnz ansible && \
    ansible-galaxy collection install community.general ansible.utils ibm.ibm_zos_core && \
    npm install jmespath node-red-contrib-alexa-remote2-applestrudel \
    node-red-contrib-bard \
    node-red-contrib-credentials \
    node-red-contrib-google-sheets \
    node-red-contrib-play-audio \
    node-red-contrib-string \
    node-red-dashboard \
    node-red-contrib-web-worldmap
USER node-red

```
2. logged on to docker.com as sunil390 and created repository node-red-ati
3. podman login docker.io
4. podman build -t node-red-ati:v3.1.0-v2 . 
5. podman tag localhost/node-red-ati:v3.1.0-v2 sunil390/node-red-ati:v3.1.0-v2
6. podman push sunil390/node-red-ati:v3.1.0-v2

## Working with NodeRed Container

1. kubectl get pods -A
2. kubectl exec -it nodered-5c57c69b9c-n5tpk   -n nodered -- /bin/bash

## Running Nodered in Kubernetes 3rd June 2023
1. NODE_RED="nodered.al8.com"
2. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./tls.crt -keyout ./tls.key -subj "/CN=${NODE_RED}/O=${NODE_RED}" -addext "subjectAltName = DNS:${NODE_RED}"
3. sudo mkdir -p /data/nodered
4. sudo chmod 755 /data/nodered
5. deployment.yaml
```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodered
  labels:
    app: nodered
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nodered
  template:
    metadata:
      labels:
        app: nodered
    spec:
      containers:
        - name: nodered
          image: sunil390/node-red-ati:v3.1.0-v2
          resources:
            limits:
              memory: 512Mi
              cpu: "1"
            requests:
              memory: 256Mi
              cpu: "0.2"  
          ports:
            - name: nodered-http
              containerPort: 1880
          volumeMounts:
            - name: nodered-volume
              mountPath: /data
      volumes:
        - name: nodered-volume
          persistentVolumeClaim:
            claimName: nodered-claim
```
7. ingress.yaml
```
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nodered-ingress
  annotations:
    traefik.ingress.kubernetes.io/router.middlewares: default-redirect@kubernetescrd
spec:
  tls:
    - hosts:
        - nodered.al8.com
      secretName: nodered-secret-tls
  rules:
    - host: nodered.al8.com
      http:
        paths:
          - path: /
            pathType: ImplementationSpecific
            backend:
              service:
                name: nodered-service
                port:
                  number: 1880

```
8. namespace.yaml
```
---
apiVersion: v1
kind: Namespace
metadata:
  name: nodered
```
9. pv.yaml
```
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nodered-volume
spec:
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  capacity:
    storage: 4Gi
  storageClassName: nodered-volume
  hostPath:
    path: /data/nodered
```
10. pvc.yaml
```
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nodered-claim
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 4Gi
  storageClassName: nodered-volume
```
11. service.yaml
```
---
apiVersion: v1
kind: Service
metadata:
  name: nodered-service
spec:
  ports:
    - name: nodered-http
      protocol: TCP
      port: 1880
  selector:
    app: nodered
```
12. kustomization.yaml
```
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: nodered

generatorOptions:
  disableNameSuffixHash: true

secretGenerator:
  - name: nodered-secret-tls
    type: kubernetes.io/tls
    files:
      - tls.crt
      - tls.key

resources:
  - namespace.yaml
  - pv.yaml
  - pvc.yaml
  - ingress.yaml
  - service.yaml
  - deployment.yaml
```
14. kubectl apply -k node-red
15. sudo systemctl restart k3s 

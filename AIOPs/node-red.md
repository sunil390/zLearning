# Node-red in Kubernetes

## https://stackoverflow.com/questions/74809325/node-red-kubernetes-deployment

## Working with NodeRed Container

1. kubectl get pods -A
2. kubectl exec -it nodered-5c57c69b9c-n5tpk   -n nodered -- /bin/bash
3. pip3 install ebcdic tnz

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
          image: nodered/node-red:latest
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
16. 

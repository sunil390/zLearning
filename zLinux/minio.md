# MinIO

## Setup

1. wget https://github.com/minio/operator/releases/download/v4.5.8/kubectl-minio_4.5.8_linux_amd64 kubectl-minio  (curl resulted in exec format error and emply file)
2. mv kubectl-minio_4.5.8_linux_amd64 kubectl-minio
3. chmod +x kubectl-minio
4. sudo mv kubectl-minio /usr/local/bin/
5. kubectl minio init
6. kubectl get all --namespace minio-operator
7. kubectl minio proxy
8. JWT Token : eyJhbGciOiJSUzI1NiIsImtpZCI6ImJUVmZzaEFtTkpUYkxnbkE1RE4tWVV5WDZpU2hMUmx5bUdPUW5EWWkxUUkifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJtaW5pby1vcGVyYXRvciIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJjb25zb2xlLXNhLXNlY3JldCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJjb25zb2xlLXNhIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiM2E5ZTFjMmItNTQ2Yy00ZTc1LWIzZGUtMGU5MDk5YTUzZDFlIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Om1pbmlvLW9wZXJhdG9yOmNvbnNvbGUtc2EifQ.UxPTWmLTp2FuT74C0WWbMKvYlUUEwAwPaaXfJP32U6mqSFlW8tc1obGZx_8R8-uWf5nJxENqCsVptrC1iX6tdZlP8mrkiTx5q5_1wcJRwymyfLyj4z7uZBxoESxP-yS9Ge05o3jxx8wyYTeK5ofEejwzmbn-0P__tO7UatU4UNUwgrDB0Dl35v76v7_BXIxBj6GBHh0qCvu2McsFWkH6hVkY6VLv2qCesS8_OmHicrwK1E8LKnBSxCKiCaMv80H6P-fBXOV46rqL1S8zFaMt3lpLFhGqhDJj4M_Gtl8246NGmF6mIPfAxs4Tq1s140uf8naJDFF47P4JSC8okDU7rQ
9. kubectl get all -n minio-operator
```
[sunil390@al8 ~]$ kubectl get all --namespace minio-operator
NAME                                       READY   STATUS    RESTARTS        AGE
pod/console-7695dd658f-64w8s               1/1     Running   0               4h
pod/znext-log-0                            1/1     Running   0               3h55m
pod/znext-log-search-api-67f556f67-77vqb   1/1     Running   4 (3h54m ago)   3h55m
pod/znext-pool-0-1                         0/1     Pending   0               3h33m
pod/minio-operator-659fd56447-f6w6w        1/1     Running   2 (3h1m ago)    4h
pod/znext-pool-0-0                         1/1     Running   2 (10m ago)     3h55m

NAME                           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
service/operator               ClusterIP      10.43.165.47    <none>        4222/TCP,4221/TCP   4h
service/console                ClusterIP      10.43.189.118   <none>        9090/TCP,9443/TCP   4h
service/minio                  LoadBalancer   10.43.184.129   <pending>     443:30543/TCP       3h55m
service/znext-hl               ClusterIP      None            <none>        9000/TCP            3h55m
service/znext-console          LoadBalancer   10.43.248.114   192.168.2.4   9443:31232/TCP      3h55m
service/znext-log-hl-svc       ClusterIP      None            <none>        5432/TCP            3h55m
service/znext-log-search-api   ClusterIP      10.43.94.107    <none>        8080/TCP            3h55m

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/console                1/1     1            1           4h
deployment.apps/znext-log-search-api   1/1     1            1           3h55m
deployment.apps/minio-operator         1/1     1            1           4h

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/console-7695dd658f               1         1         1       4h
replicaset.apps/znext-log-search-api-67f556f67   1         1         1       3h55m
replicaset.apps/minio-operator-659fd56447        1         1         1       4h

NAME                            READY   AGE
statefulset.apps/znext-log      1/1     3h55m
statefulset.apps/znext-pool-0   1/2     3h55m
```
10. kubectl get statefulsets znext-pool-0 -n minio-operator
11. kubectl scale statefulsets znext-pool-0 --replicas=1 -n minio-operator
12. kubectl edit statefulsets znext-pool-0 -n minio-operator
13. kubectl patch statefulsets znext-pool-0 -p '{"spec":{"replicas":1}}' -n minio-operator
  

## Confifg

1. Name : znext
2. NameSpace : znext-namespace
3. 2,2,20
4. Access Key :8HqRmOBygs2b6LMu
5. Secret Key :FTjiG1rjm4NXWWi6Djvg3oO6GOWkzUxg
6.  

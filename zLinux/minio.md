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

## Confifg

1. Name : znext
2. NameSpace : znext-namespace
3. 1,1,20
4. Access Key :1O1aewTMGycWW4TF
5. Secret Key :UiGEg3DIyRTK2DMGTwJE80fJU8HWBxuh
```
[sunil390@al8 ~]$ kubectl get all --namespace znext-namespace
NAME                                       READY   STATUS    RESTARTS        AGE
pod/znext-pool-0-1                         0/1     Pending   0               4m35s
pod/znext-log-0                            1/1     Running   0               4m34s
pod/znext-pool-0-0                         1/1     Running   0               4m35s
pod/znext-log-search-api-67f556f67-tkgjs   1/1     Running   2 (4m31s ago)   4m33s

6. kubectl delete secret znext
NAME                           TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/minio                  LoadBalancer   10.43.76.43    <pending>     443:30146/TCP    5m35s
service/znext-hl               ClusterIP      None           <none>        9000/TCP         5m35s
service/znext-console          LoadBalancer   10.43.90.70    192.168.2.4   9443:30886/TCP   5m35s
service/znext-log-hl-svc       ClusterIP      None           <none>        5432/TCP         4m34s
service/znext-log-search-api   ClusterIP      10.43.21.222   <none>        8080/TCP         4m33s

NAME                                   READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/znext-log-search-api   1/1     1            1           4m33s

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/znext-log-search-api-67f556f67   1         1         1       4m33s

NAME                            READY   AGE
statefulset.apps/znext-log      1/1     4m34s
statefulset.apps/znext-pool-0   1/2     4m35s
```
6. kubectl get statefulsets znext-pool-0 -n znext-namespace
7. kubectl scale statefulsets znext-pool-0 --replicas=1 -n znext-namespace
8. kubectl edit statefulsets znext-pool-0 -n znext-namespace
9. kubectl patch statefulsets znext-pool-0 -p '{"spec":{"replicas":1}}' -n znext-namespace
10. kubectl delete secret znext-secret -n znext-namespace
11. kubectl delete secret znext-user-0 -n znext-namespace

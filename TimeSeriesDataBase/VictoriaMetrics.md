# Victoria Metrics

## Kubernetes Operator Install

1. sudo snap install microk8s --classic --channel=1.23
2. microk8s start
3. microk8s enable dns storage ingress
4. export VM_VERSION=`basename $(curl -fs -o/dev/null -w %{redirect_url} https://github.com/VictoriaMetrics/operator/releases/latest)`
5. wget https://github.com/VictoriaMetrics/operator/releases/download/$VM_VERSION/bundle_crd.zip
6. unzip  bundle_crd.zip 
7. kubectl apply -f release/crds
8. kubectl apply -f release/operator/
9. k apply -f ./release/examples/vmsingle_with_pvc.yaml


# Victoria Metrics

## Kubernetes Operator Install

1. export VM_VERSION=`basename $(curl -fs -o/dev/null -w %{redirect_url} https://github.com/VictoriaMetrics/operator/releases/latest)`
2. wget https://github.com/VictoriaMetrics/operator/releases/download/$VM_VERSION/bundle_crd.zip
3. unzip  bundle_crd.zip 
4. kubectl apply -f release/crds
5. kubectl apply -f release/operator/

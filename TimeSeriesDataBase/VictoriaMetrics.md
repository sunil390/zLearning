# Victoria Metrics

## 12th June

```
uri
'/api/v1/import/csv?format=3:metric:tb_local,4:metric:tb_mirror,5:metric:gb_alloc,6:metric:gb_free,7:metric:total_tb,8:metric:total_gb,1:label:client,2:label:lpar_grp,9:label:dc,10:label:mgr,11:label:hub,12:time:rfc3339'      

data

```

## Json export import

1. curl http://localhost:8428/api/v1/export -d 'match={__name__!=""}' > exported_data.jsonl

```
import json, yaml 

data = []
with open(r'exported_data.jsonl') as file:
    for line in file:
        data.append(json.loads(line))
    json_out = json.dumps(data, indent = 4)

with open(r'vm_out.yaml','w') as yaml_out:
    yaml.dump(json_out, yaml_out, allow_unicode=True)



Example1:
In case you are using pandas and you will be interested in loading the json file as a dataframe, you can use:
import pandas as pd
df = pd.read_json('file.json', lines=True)
And to convert it into a json array, you can use:
df.to_json('new_file.json')

```

## CheatSheet

1. List labels: curl -G 'http://localhost:8428/prometheus/api/v1/labels'
2. curl -G 'http://138.69.224.85:8428/api/v1/export' -d 'match[]={client!=""}'
3. Series Deletion: curl -G http://138.69.224.85:8428/api/v1/admin/tsdb/delete_series?match[]={capacity} TimeSeriesSelector
4. curl -G http://138.69.224.85:8428/api/v1/admin/tsdb/delete_series?match[]={day_avg}
5. curl -G http://138.69.224.85:8428/api/v1/admin/tsdb/delete_series?match[]={year_avg}
6. curl -G http://138.69.224.85:8428/api/v1/admin/tsdb/delete_series?match[]={pct_change}

## Issue List
1. Alerting :https://github.com/VictoriaMetrics/VictoriaMetrics/issues/1739 , Disabled alerting in Data Source. VMalerting to be explored later.
2. Change Retention : https://snapcraft.io/victoriametrics
3. sudo nano /var/snap/victoriametrics/current/extra_flags 
```
FLAGS="-retentionPeriod=1y"
```
4. sudo snap restart victoriametrics
5. datafolder : /var/snap/victoriametrics/current/var/lib/victoriametrics/



## 26th March - Vanilla VM and Grafana Setup.

### VM
1. sudo apt update
2. sudo apt upgrade
3. snap info victoriametrics
4. sudo snap install victoriametrics
5. curl http://localhost:8428/metrics
6. curl http://localhost:8428/api/v1/query -d 'query={job=~".*"}'

### Grafana

1. sudo apt-get install -y apt-transport-https
2. sudo apt-get install -y software-properties-common wget
3. wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
4. echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
5. sudo apt-get update
6. sudo apt-get install grafana
7. sudo systemctl daemon-reload
8. sudo systemctl start grafana-server
9. sudo systemctl status grafana-server
10. sudo systemctl enable grafana-server.service

#### Grafana Data Source

1. Configuration -> Data Sources -> Prometheus -> HTTP URL :  http://192.168.2.28:8428 , Access : Sever(Default)
2. Save and Test

#### DashBoard

1. + Create -> DashBoard -> Add New Panel -> DataSource : Prometheus -> Metrics Browser -> Select Metric, Label and Values -> Use Query -> Save and Apply 

#### VM Backfilling from Mainframe

1. CSV Data is kept in Dataset as Multiple rows.
2. Submit the JCL from Mainframe using IKJEFT01 and VMLOADER rexx

#### House Keeping Metrics

1. curl -G 'http://192.168.2.28:8428/api/v1/export' -d 'match[]={ticker!=""}'
2. Series Deletion: curl -G http://192.168.2.28:8428/api/v1/admin/tsdb/delete_series?match[]={ask} [TimeSeriesSelector](https://prometheus.io/docs/prometheus/latest/querying/basics/#time-series-selectors) 


## 25th March Kubernetes Operator Install : Incomplete : To Be Continued ...

1. sudo snap install microk8s --classic --channel=1.23
2. microk8s start
3. microk8s enable dns storage ingress
4. export VM_VERSION=`basename $(curl -fs -o/dev/null -w %{redirect_url} https://github.com/VictoriaMetrics/operator/releases/latest)`
5. wget https://github.com/VictoriaMetrics/operator/releases/download/$VM_VERSION/bundle_crd.zip
6. unzip  bundle_crd.zip 
7. kubectl apply -f release/crds
8. kubectl apply -f release/operator/
9. sudo nano ./release/examples/vmsingle_with_pvc.yaml 
```
apiVersion: operator.victoriametrics.com/v1beta1
kind: VMSingle
metadata:
  name: example-vmsingle-pvc
spec:
  # Add fields here
  retentionPeriod: "1"
  removePvcAfterDelete: true
  storage:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
  service_type: nodeport
```
9. k apply -f ./release/examples/vmsingle_with_pvc.yaml

10. https://javamana.com/2021/06/20210619193722982U.html

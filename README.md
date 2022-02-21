# k8s-api-server-base
this repo is a template of k8s api server.  
using a master to call worker in k8s cluster.  

# build and run
```sh
#path in ./k8s-api-server-base

#build
sudo ./run.sh build

#deploy
sudo ./deploy.sh deploy <worker-dir>

#redrploy
sudo ./deploy.sh redeploy <worker-dir>

#uninstall
sudo ./deploy.sh uninstall
```

# test

## step 1

```
kubectl get svc -n kube-system
```

## step 1 get result
```
NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
api-server-base-service   ClusterIP   <cluster-ip>    <none>        80/TCP                   7m9s
```

## step 2
```
# <cluster-ip> in step 1 result
curl --location --request GET 'http://<cluster-ip>/test/GET'
```
    
## step 2 get result
```
{
  "data": "GET",
  "status": "success"
}
```


## other test

### 1
```
curl --location --request GET 'http://<cluster-ip>/worker/GET'
```

#### result
```
{
  "data": {
    "api-server-base-worker-6s282": {
      "namespace": "kube-system",
      "pod_ip": <pod-ip>
    }
  },
  "status": "success"
}
```

---

### 2
    
```
curl --location --request GET 'http://<cluster-ip>/test-worker/GET'
```

#### result
```
{
  "data": {
    "api-server-base-worker-6s282": {
      "namespace": "kube-system",
      "pod_ip": <pod-ip>
    }
  },
  "status": "success"
}
```
---

### 3
```
# <pod-ip> in other test - 1 and 2 result
curl --location --request GET 'http://<pod-ip>:8080/test/GET'
```
#### result
```
{
  "data": "GET",
  "status": "success"
}
```

# debug
## log path
```
#master log path:
/etc/api-server-base/log/master.log

#worker log path:
/etc/api-server-base/log/worker.log
```

## change log path
### method 1 : auto change in deploy
```
./deploy.sh redeploy <worker-path>

than log path is `<worker-path>/log`
```
- https://github.com/cool9203/k8s-api-server-base/blob/master/deploy/worker.yaml#L53
- https://github.com/cool9203/k8s-api-server-base/blob/master/deploy/worker.yaml#L53

# how to add service to master or worker

## step 1

add `<name>.py` in [this](https://github.com/cool9203/k8s-api-server-base/tree/master/pkg/api), using [this template](https://github.com/cool9203/k8s-api-server-base/blob/master/pkg/api/test.py).

## step 2
add `<name>.py` to [master](https://github.com/cool9203/k8s-api-server-base/blob/master/pkg/api/master.py#L5) or [worker](https://github.com/cool9203/k8s-api-server-base/blob/master/pkg/api/worker.py#L5)

## step 3
deploy. [see more](https://github.com/cool9203/k8s-api-server-base#build-and-run)
```sh
sudo ./deploy.sh redeploy <worker-dir>
```

## step 4
test. [see more](https://github.com/cool9203/k8s-api-server-base#test)

# change flask run ip and port
in ./k8s-api-server-base/master.yaml  
if changed, you should change this file too.  
https://github.com/cool9203/k8s-api-server-base/blob/master/deploy/master-svc.yaml#L12

# master call worker service example
https://github.com/cool9203/k8s-api-server-base/blob/master/pkg/api/test-worker.py#L22-L27  

# Jonoperator

## Deployment

### Prerequisites

1. Logged into OCP Cluster

### Setup

```shell
oc apply -f ./operator-deployment.yaml
oc apply -f ./jon.yaml
```

## Local Development

### Prerequisites

1. Python v3.12
2. Logged into OCP Cluster

### Setup

```shell
pip install -r ./requirements.txt
oc apply -f ./crd.yaml
kopf run jon.py --verbose
```

### Running

```shell
oc apply -f ./jon.yaml
```

### Destroying

```shell
oc delete -f ./jon.yaml
kubectl delete crd jons.kopf.dev
```

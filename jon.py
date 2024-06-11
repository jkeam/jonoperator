import kopf
import logging
from kubernetes import client, utils

@kopf.on.create('jons')
def create_fn(spec, name, namespace, logger, **kwargs):
    logging.info(f"Handler is called")

    coolness = spec.get('coolness')
    replicas = spec.get('replicas', 1)
    logger.info(f"coolness: {coolness}")
    logger.info(f"replicas: {replicas}")
    # if not size:
        # raise kopf.PermanentError(f"Size must be set. Got {size!r}.")

    api = client.ApiClient()
    image:str = "quay.io/jkeam/hello-go@sha256:96bd61e4a98f06fb677f9e0ee30a48faa5c2de6c3f9ee967966c76dd549674c3"
    data = {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'metadata': {'name': name, 'namespace': namespace}, 'spec': {'selector': {'matchLabels': {'app': 'nginx'}}, 'replicas': replicas, 'template': {'metadata': {'labels': {'app': 'nginx'}}, 'spec': {'containers': [{'name': 'nginx', 'image': image, 'ports': [{'containerPort': 8080}]}]}}}}
    kopf.adopt(data)
    utils.create_from_dict(api, data)
    return {'name': name}

@kopf.on.update('jons')
def update_fn(spec, status, namespace, logger, **kwargs):

    coolness = spec.get('coolness', None)
    replicas = spec.get('replicas', 1)
    logger.info(f"coolness: {coolness}")
    logger.info(f"replicas: {replicas}")
    # if not size:
        # raise kopf.PermanentError(f"Size must be set. Got {size!r}.")

    api_client = client.ApiClient()
    api = client.AppsV1Api(api_client)
    name:str = status['create_fn']['name']
    image:str = "quay.io/jkeam/hello-go@sha256:96bd61e4a98f06fb677f9e0ee30a48faa5c2de6c3f9ee967966c76dd549674c3"
    body = {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'metadata': {'name': name, 'namespace': namespace}, 'spec': {'selector': {'matchLabels': {'app': 'nginx'}}, 'replicas': replicas, 'template': {'metadata': {'labels': {'app': 'nginx'}}, 'spec': {'containers': [{'name': 'nginx', 'image': image, 'ports': [{'containerPort': 8080}]}]}}}}
    api.patch_namespaced_deployment(name, namespace, body)

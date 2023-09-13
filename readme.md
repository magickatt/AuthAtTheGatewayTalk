# Centralise legacy auth at the ingress gateway

## Installing

https://www.getambassador.io/docs/emissary/latest/topics/install/helm#install-with-helm-1

```
kubectl apply -f https://app.getambassador.io/yaml/emissary/3.7.2/emissary-crds.yaml
kubectl wait --timeout=90s --for=condition=available deployment emissary-apiext -n emissary-system
```

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.11/config/manifests/metallb-native.yaml
```

```
helm install auth-at-the-gateway chart
```

--trusted-host pypi.org --trusted-host files.pythonhosted.org

https://www.docker.com/blog/how-kubernetes-works-under-the-hood-with-docker-desktop/

## Running

### Basic example

This is a basic application which uses Flask route decorators to enforce HTTP header-based authentication/authorization.

```bash
export PYTHONPATH=$PYTHONPATH:$PWD/src
python -m venv .virtualenv
source .virtualenv/bin/active

flask --app api-with-auth run
```

## Testing

### Sample API keys

* psiuedo
* dpmldkp
* nhcbmfd
* ijeytfn
* wybnerw
* lpzxkra
* rpjwqti

## Resources

### Data generation utilities

Could have (and probably should have) done from a REPL, but sometimes it is handy to quickly generator some fake data.

* https://www.uuidgenerator.net/version4
* https://www.fakenamegenerator.com

```
curl --http0.9 -H "x-mycompany-api-key: psiuedo" localhost:8080
```

https://medium.com/@JockDaRock/kubernetes-metal-lb-for-docker-for-mac-windows-in-10-minutes-23e22f54d1c8

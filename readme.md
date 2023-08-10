# Centralise legacy auth at the ingress gateway

## Running

### Basic example

This is a basic application which uses Flask route decorators to enforce HTTP header-based authentication/authorization.

```bash
export PYTHONPATH=$PYTHONPATH:$PWD/src
python -m venv .virtualenv
source .virtualenv/bin/active

flask --app api run
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

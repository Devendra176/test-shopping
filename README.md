# Context

You are a software engineer hired to create online shopping platform for a magical store.

## Task

- Modify `simple_flask/*.py` and `simple_flask/schema.sql` to pass the pytest's testcase
- Edit `Dockerfile` to build container image
- No restrictions on python packages (requirements.txt) or Linux distro as base image
- **DB must remain as SQLite**
- **Base web framework must be Flask**
- **No edit allowed for `*.pl`**
- You can increase the test case to cover possible error scenario **but not modify / remove existing ones in 'test_api.py'**

To run pytest -> `pytest .`


## Test-Task (Shopping)
### Setup
#### Dependency
* Docker -> https://docs.docker.com/engine/install/

##### Run server
```
git clone https://github.com/Devendra176/test-shopping.git
cd test-shopping
```
### Docs Link
swagger: http://127.0.0.1:5000/swagger-ui/

### Makefile
- setup: make setup
- start: make start-server
- logs: make watch-logs
- tests: make start-test
- stop: make stop-server
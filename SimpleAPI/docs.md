# Why

I chose to use Python with Flask because it was one of your popular stacks and I had never worked with Flask before, so it seemed like a fun way to learn a little bit of the tech stack and something new to me. It took me about 90 minutes to get a bare bone understanding of how flask worked and get the service running to a point that seemed to be correct to me. I chose to exclude unit tests because the prompt said to take between one and two hours to complete this and adding unit tests would have taken more time than was allotted. If given more time my approach would have been to build unit tests first and then implement the service to make it more verbose. 

## Dependencies

 1. Built on python 3.9
 2. Flask version 2.0.2
 3. Conda was used as enviorment creation


## Run the service:

 1. Make sure running `Python=3.9` or later
 2. Install `Flask=2.0.2`
 3. `cd` into folder
 4. Run `python basic_api.py` to start the server (Note: I used the default port so it should be 127.0.0.1)

## Example Post request

Specifically for windows:

```
curl -UseBasicParsing http://127.0.0.1:5000 -Method POST -Body "id=MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"
```

Returns:

```
id=MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz&Signature=a84b52c35d26a111264c6c6f923061a95ed5fa43f1a75590a105bfeede1f448d
```

__*Note*__: Not very verbose. Built on a windows 10 machine using anaconda powershell to run post commands. I have no idea if this exact post command will work on a OSX or Linux machine. 

Docs used:

 * [Flask Docs](https://flask.palletsprojects.com/en/2.0.x/#api-reference)
 * [FLask Requests docs](https://tedboy.github.io/flask/generated/generated/flask.Request.html)
 * [hmac docs](https://docs.python.org/3/library/hmac.html)
 * [basic hmac example](https://browse-tutorials.com/snippet/python-generate-hmac-sha-256-string)


# Cisco IM&P REST examples

These files are samples for programming `Presence Web Services` `(PWS)` in Python.

You can download the documentation from here:
(https://developer.cisco.com/site/im-and-presence/documents/presence_web_service/latest_version/)

## HOW TO USE THE SCRIPTS

1. Edit the json and list files to define your server, users, contact, etc.

(see `SET YOUR PARAMETERS` below)

2. Make sure the computer you're using for the endpoint can accept and
respond to TCP port 8080 (generally via firewall settings)

3. Run `python3 pws-delete.py`
4. Run `python3 pws-create.py`
5. Run `python3 endpoint.py`
6. Run `python3 get_subscribed_presence.py 1 RICH_PRESENCE`

## THE PWS SCRIPTS

The API to set up your own presence notification handler is `PWS` or
`Presence Web Services`.  You can use SOAP or REST here, but REST is a
simpler API to work with, so our examples use REST, `pws-create.py`,
`pws-delete.py`, `endpoint.py` and `get_subscribed_presence.py`.

The REST API procedure is generally as follows:

1. Log in an application user with the username and password.
This returns the app user session key

2. Use the app user session key to log in an end user with the end
user username, which returns an end user session key

3. Use the session keys to access the API requests you want.

## `pws-create.py`

1. Log in the application user and end user.

2. Use the app user session key to specify an endpoint URL.  This URL
points to the web service that will receive presence notifications.

3. Use the end user session key to subscribe for presence notifications
of a list of specified contacts.  When the presence for one of these
contacts changes, it will trigger a notification sent to the endpoint.
It is the responsibility of the web service endpoint to fetch the
actual presence status, whether it's BASIC presence or RICH presence.

## `pws-delete.py`

This script is simply an "undo" for `pws-create.py`.  It unsubscribes
presence notifications for the contacts and unregisters the endpoint URL.

Use this script to clear the subscriptions and endpoint when you want
to change anything and try again. This script is purposely overkill, just in case someone accidentally created multiple endpoints and subscriptions.

## `endpoint.py`

This is the web service that listens on port 8080 for REST-initiated
notifications that a contact's presence has changed.  It responds by
using a REST request to fetch the BASIC presence for that contact,
and appends the presence status response to the file `status.txt`.

## HOW TO PREPARE TO USE THE SCRIPTS

### INSTALL PYTHON

Install Python 3, latest version.  Follow the instructions for your OS from here:
(https://docs.python.org/3/)

On Windows, choose the option to add to PATH environment variable.

While we use the commands `pip3` and `python3` which are appropriate for Linux, you may need to substitute them with `pip` and possibly `python` on Windows.

### CREATE A VIRTUAL ENVIRONMENT

It is good practice to create and work with a virtual environment.  This
lets you install a number of Python libraries needed only for your test
project, and not necessarily installed in your default Python setup.
See this link for instructions on how to set up a virtual environment
for your operating system: (https://docs.python.org/3/tutorial/venv.html)

Follow the instructions for entering your virtual environment, and then
proceed to install the necessary Python library dependencies for this
project.

Once you have your virtual environment installed, execute the correct
`activate` procedure for your OS so that you're operating from within
the virtual environment. I created these sampled on Linux, so you would execute `source activate` in the venv/bin directory.

### INSTALL PYTHON DEPENDENCIES

The commands you'll need to install dependencies will vary from OS to OS.
Start with

```
    $ pip3 install requests
```

This should automatically install most libraries you'll need. If you get
a message when you run a script that says your `import` doesn't work,
then try to `pip3 install <that dependency>`.  

Script Dependencies:
    `lxml`
    `requests`
    `json`
    `subprocess`
    `flask`

### SET YOUR PARAMETERS

1. **[REQUIRED]** Edit `serverparams.json` to point to your Cisco IM&P
server and the administrator username and password credentials.  

The file also contains the host IP for the endpoint URL.  This is the
URL for the web service that listens for presence notifications.

The default port for the web service is 5000, but Cisco IM&P won't use 5000, so you'll need to set flask to use `8080` and make sure the PC or server running `endpoint.py` can accept TCP traffic over port 8080.  

```
{
  "params" : [
      {
        "SERVER" : "<your cimp server>",
        "USERNAME" : "<administrator>",
        "PASSWD" : "<password>"
        "HOST": "<host IP of the ENDPOINTURL>"
      }
  ]
}
```

2. **[REQUIRED]** Edit `appuser.json` to include the username and password
of your application user.  

```
{
  "params" : [
      {
        "USERNAME" : "<Application user name>",
        "PASSWD" : "<Application user password>"
      }
  ]
}
```

3. **[REQUIRED]** Edit `enduser.json` to include the username of the user whose contacts you want to add.

You want to specify only the user names, not the full JIDs.  In other words, you want `joe` not `joe@somedomain.com`.  

The `USERNAME` is the name of the end user whose contact's presence you want to monitor.

```
{
  "params" : [
      {
        "USERNAME" : "<Jabber end user name>",
      }
  ]
}
```

4. **[REQUIRED]** Edit `contacts.list` to include contacts for your end user.

For example (don't use these contact names, these are samples):

```
[ "joe", "rita", "carlotta" ]
```

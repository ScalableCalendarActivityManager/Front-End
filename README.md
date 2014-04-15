Front-End
=========

Front end web server for SCAM


To test locally on your machine, run the following once to install the proper packages:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then this to start the development server (You must have already activated the venv by this point):

```bash
foreman start
```

When you're done, you can run the following to exit the virtualenv

```bash
deactivate
```


# Gym Server
*A remote gym-like training environment.*

Inspired by Google Football Research Environment, this OpenAI Gym-like training
environment can function like a local one.

This is designed to be extensible for many types of environments and supports
an instance-based experimentation model that encapsulates model evaluation into
separate environments.

[Definitely a work-in-progress.]


## How It Works
This Gym server comes in two parts: the provision-er which manages experiment
instances and the runtime, which actually runs them.

Eventually, this remote environment will serve as a testbed for asynchronous
communication between an agent and an environment, only sending back new states
after certain periods of time. This will allow RL agents to respond to having
imperfect models of the world. (Like in "[Learning to Predict Without Looking Ahead:
World Models Without Forward Prediction](https://learningtopredict.github.io/)")


## Setup/Development
Install dependencies using pipenv:

```bash
pipenv install
```

Now activate the virtual environment:

```bash
pipenv shell
```

Now you're all set up. Run the Flask development server (Windows/Bash):

```bash
cd gym-server/gym_server
flask run
```


## Deployment
This uses a Docker container. Deploy it to a solution that can handle containers
like Google Kubernetes engine and provision static IPs.

An example is up at [~~gym.williecubed.me~~](https://gym.williecubed.me).
(Use the development server for now.)

### Tidbits on Cloud Providers
If not deploying on Google Cloud, one can safely remove the
`google-cloud-logging` client libraries from the dependencies using pipenv.
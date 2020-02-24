# Architecture
This server is designed to be running persistently in the background, making it
suitable for deployment to a virtual machine or container instance.

## Console
The console is a wrapper for the experiment orchestrator coupled with mechanisms
for authentication and authorization of experiment resources.

The console allows the user to see their actively running experiments.

The console interacts with an `ExperimentOrchestrator` that does most of the
heavy lifting.

## Experiment Orchestrator
The experiment orchestrator manages experiment state. Its primary function is to
keep track of actively running experiments in memory and store handles to them.

To keep track of all past experiments, a separate SQLite database is used.

## Experiment
The experiment contains a handle to an actively running experiment environment.
It uses the handle to send commands to the environment.

Experiments are wrappers for connections to environments.

Experiments can be run synchronously using WebSockets or asynchronously using
step-based HTTP requests.

TODO: Give example.

(Eventually the orchestrator will launch a container using an `EnvSpec`
containing its location.)

## Runtime Connection
The `RuntimeConnection` is the penultimate level of abstraction for an
environment.

It can be used to communicate with anything from a Grid World simulation or a
Minecraft game instance.

Subclasses are ultimately responsible for implementing the runtime connection
API.
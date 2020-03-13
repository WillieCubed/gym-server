# How to Use Gym Server

Gym Server is a REST-based web server that manages actively running experiments.

The process of using Gym Server goes like this:
1. Create experiment configuration.
2. Upload experiment configuration (POST /experiments).
3. Modify experiment status to be "started" (PUT /experiments/<uid>) using UID from (2).
4. Make WebSocket connection to running experiment.
5. Use two-way data flow to send actions and receive observations and rewards.

## PAL Usage
For the AI Lab library, most of this is abstracted away. Instead of sending
direct HTTP requests to the server, you should use PAL like the following:

```python
import polycraft_lab as pal

dqn = ...
config = 'test_config.json'  # Step 1

with pal.setup_env(config) as env:  # Equivalent of step 2 
    observation = env.reset()  # Steps 3-4
    done = False
    for episode in range(1, 10):
        while not done:
            action = dqn.generate_action(observation)
            observation, reward, done, info = env.step(action)
```
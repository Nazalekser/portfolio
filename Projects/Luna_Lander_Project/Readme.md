### The goal
The goal of the Lunar Lander environment (using OpenAI's Gym Library) is to land the lunar lander safely on the landing pad, which is designated by two flag poles and its center is at coordinates (0,0) but the lander is also allowed to land outside of the landing pad. The lander starts at the top center of the environment with a random initial force applied to its center of mass and has infinite fuel. The environment is considered solved if you get 200 points.

### Action Space
The agent has four discrete actions available: do nothing, fire right engine, fire main engine, fire left engine.

### Observation Space
The agent's observation space consists of a state vector with 8 variables: its (𝑥,𝑦) coordinates, linear velocities (𝑥˙,𝑦˙), angle 𝜃, angular velocity 𝜃˙, two booleans, 𝑙 and 𝑟, that represent whether each leg is in contact with the ground or not.

### Rewards
The total reward of an episode is the sum of the rewards for all the steps within that episode. For each step, the reward:
* is increased/decreased the closer/further the lander is to the landing pad.
* is increased/decreased the slower/faster the lander is moving.
* is decreased the more the lander is tilted (angle not horizontal).
* is increased by 10 points for each leg that is in contact with the ground.
* is decreased by 0.03 points each frame a side engine is firing.
* is decreased by 0.3 points each frame the main engine is firing.
The episode receive an additional reward of -100 or +100 points for crashing or landing safely respectively.

### Episode Termination
An episode ends (i.e the environment enters a terminal state) if the lander crashes (i.e if the body of the lander comes in contact with the surface of the moon) or the absolute value of the lander's 𝑥-coordinate is greater than 1 (i.e. it goes beyond the left or right border).

## The standard “agent-environment loop” formalism
The agent interacts with the environment in discrete time steps 𝑡=0,1,2,.... At each time step 𝑡, the agent uses a policy 𝜋 to select an action 𝐴𝑡 based on its observation of the environment's state 𝑆𝑡. The agent receives a numerical reward 𝑅𝑡 and on the next time step, moves to a new state 𝑆𝑡+1.

### Target Network
We can train the 𝑄-Network by adjusting it's weights at each iteration to minimize the mean-squared error in the Bellman equation.
To avoid a constantly moving target (can lead to oscillations and instabilities), we can create a separate neural network for generating the 𝑦 targets and it will have the same architecture as the original 𝑄-Network. We will update the weights 𝑤− of the the target 𝑄-Network using a soft update (the target values change slowly, which greatly improves the stability of our learning algorithm).

### Experience Replay
To avoid correlations (learn from consecutive experiences can run into problems due to the strong correlations), we employ Experience Replay (storing the agent's experiences in a memory buffer and then sampling a random mini-batch of experiences from the buffer) to generate uncorrelated experiences for training our agent.

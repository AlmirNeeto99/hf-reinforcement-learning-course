# Unit 1 - Intro

This Unit is focused on introducing **Reinforcement Learning**.

The main topics covered in this unit is type of tasks, main approaches and more.

## Reinforcement Learning

**RL** is an artificial intelligence framework where the **agent** learns through **trial and error**.

## The RL Process

- The agent receives a **state** - A frame of a game, for example
- The agent takes an **action** - Move to the right
- The action is applied to the **environment** and returns the new state - the character moved
- The **environment** gives a **reward** to the agent

The goal: **maximixe the cumulative reward.**

## State vs Observation

- State: full state of the environment
  - In chess, we can see the whole board
- Observation: only a part of the environment
  - In a 3D game, we can only see what is in front of us

## Action Space

- Discrete: finite set of actions
- Continuous: infinite set of actions

## Tasks

A task is an instance of the RL problem (an execution)

A task can be **episodic** and **continuing**

- Episodic:
  - A list of states, actions, rewards and new states
  - For example, in Mario, an **episode** starts when a new level begins and ends when you are killed or you reach the end of the level.
- Continuing:
  - A task that have no terminal state
  - For example, a stock trader.

## Exploration vs Exploitation

The difference is that in **exploration** the agent can try random actions to find more information about the environment.

In **exploitation** the agent will use information it already knows to try maximizing reward.

## Approaches

There is two main approaches on solving a RL problem: **policy based** and **value based**.

Before diving into each method, I will define **policy**. The **policy** is the "brain" of the agent. It is a function that returns an action given a state $s$

Policy: $action = \pi(s)$

### Policy Based

In policy based methods, the agent learns a function directly. It can be **deterministic**: given a state it can select an action to take.

It can also be **stochastic** where it returns a probability of an action. For example, given a state, it can return [left: 0.5, right: 0.5], a probability of taking each action.

### Value based

In this method, the agent learns a value function to trying reach the state with the highest value.

## The "Deep" in DRL

Deep Reainforcement Learning means we use a Deep Learning model to approximate to a value function.

One of the approach uses traditional algorithm called Q-Learning to find an action to take given a state.

And in the second approach we'll use deep learning to approximate a Q-value.

## Summary

- RL:
  - learns from actions
  - trial and error
  - It tries to maximize a reward
- It's a loop:
  - state
  - action
  - reward
  - next state
- We discount the early rewards (tries to make it more likely to try and "go far from the beggining")
- We want to find an optimal policy, the best action to maximixe our return
- Two ways to finding a policy:
  - train a policy directly: policy based
  - train a value function that tells us the expected return in each state: value based
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

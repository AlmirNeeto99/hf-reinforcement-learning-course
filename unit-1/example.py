import gymnasium as gym

env = gym.make("LunarLander-v2")

observation = env.reset()


for _ in range(20):

    action = env.action_space.sample()

    print("Action: ", action)

    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        print("Agent done!")
        observation, info = env.reset()

env.close()
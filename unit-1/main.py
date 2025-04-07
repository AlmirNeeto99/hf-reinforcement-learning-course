import gymnasium


from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor


env = gymnasium.make("LunarLander-v2")
env.reset()

print("=== Observation Space ===")

print("-> Observation Space shape", env.observation_space.shape)
print("-> Sample observation", env.observation_space.sample())


print("=== Action space ===")

print("-> Action Space shape", env.action_space.shape)
print("-> Sample action", env.action_space.sample())


model = PPO(
    "MlpPolicy",
    env=env,
    n_steps=1024,
    batch_size=64,
    gamma=0.999,
    gae_lambda=0.98,
    ent_coef=0.01,
    verbose=1,
)

model.learn(total_timesteps=1000000)

model_name = "ppo-LunarLander-v2"
model.save(model_name)


eval_env = Monitor(gymnasium.make("LunarLander-v2"))

mean_reward, std_reward = evaluate_policy(
    model, eval_env, n_eval_episodes=10, deterministic=True
)

print("=== Evaluating ===")


print(f"Mean Reward = {mean_reward:.2f} +/- {std_reward}")

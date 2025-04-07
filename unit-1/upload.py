import gymnasium

from huggingface_sb3 import package_to_hub


from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.vec_env import DummyVecEnv

model = PPO.load("ppo-LunarLander-v2.zip")


eval_env = DummyVecEnv(
    [
        lambda: Monitor(gymnasium.make("LunarLander-v2", render_mode="rgb_array")),
    ]
)


package_to_hub(
    model=model,
    model_architecture="PPO",
    model_name="ppo-LunarLander-v2",
    env_id="LunarLander-v2",
    eval_env=eval_env,
    repo_id="almirneeto99/PPO-LunarLander-v2",
    commit_message="Adding PPO Lunar Lander agent",
)

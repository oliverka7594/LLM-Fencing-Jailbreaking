# Red Teaming for Large Language Models (LLM's) - Resources

This repository contains a curated list of resources, papers, datasets, and frameworks related to evaluating red teaming for Large Language Models (LLM's).

## Table of Contents
- [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](#training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback)
- [PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](#promptbench-towards-evaluating-the-robustness-of-large-language-models-on-adversarial-prompts)
- [Explore, Establish, Exploit: Red Teaming Language Models from Scratch](#explore-establish-exploit-red-teaming-language-models-from-scratch)
- [Jailbreaker: Automated Jailbreak Across Multiple Large Language Model Chatbots](#jailbreaker-automated-jailbreak-across-multiple-large-language-model-chatbots)
- [BeaverTails: Towards Improved Safety Alignment of LLM via a Human-Preference Dataset](#beavertails-towards-improved-safety-alignment-of-llm-via-a-human-preference-dataset)
- [VISUAL ADVERSARIAL EXAMPLES JAILBREAK LARGE LANGUAGE MODELS](#visual-adversarial-examples-jailbreak-large-language-models)
- [Red Teaming Language Models with Language Models](#red-teaming-language-models-with-language-models)
- [Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned](#red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned)
- [Safety Assessment of Chinese Large Language Models](#safety-assessment-of-chinese-large-language-models)

### Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
- [GitHub Repository](https://github.com/anthropics/hh-rlhf)
- [arXiv Paper](https://arxiv.org/abs/2204.05862)
- Referenced for methods in [PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts](https://arxiv.org/abs/2306.04528)

### PromptBench: Towards Evaluating the Robustness of Large Language Models on Adversarial Prompts
- [arXiv Paper](https://arxiv.org/abs/2306.04528)
- [HuggingFace Demo](https://huggingface.co/spaces/March07/PromptBench)
- [Evaluation Framework](https://github.com/microsoft/promptbench) - A robustness evaluation framework for LLMs on adversarial prompts
- Revised strategies from [TextAttack](https://github.com/QData/TextAttack) - A Python framework for adversarial attacks, data augmentation, and model training in NLP

### Explore, Establish, Exploit: Red Teaming Language Models from Scratch
- [arXiv Paper](https://arxiv.org/abs/2306.09442)
- [GitHub Repository](https://github.com/thestephencasper/explore_establish_exploit_llms)
- Used the [CommonClaim Dataset](https://github.com/Algorithmic-Alignment-Lab/CommonClaim)

### Jailbreaker: Automated Jailbreak Across Multiple Large Language Model Chatbots
- [arXiv Paper](https://arxiv.org/abs/2307.08715)
- [Accompanying Site](https://sites.google.com/view/ndss-masterkey/masterkey) (Incomplete)

### BeaverTails: Towards Improved Safety Alignment of LLM via a Human-Preference Dataset
- [arXiv Paper](https://arxiv.org/abs/2307.04657)
- [Accompanying Site](https://sites.google.com/view/pku-beavertails)
- [Whole Dataset](https://github.com/PKU-Alignment/beavertails)

### VISUAL ADVERSARIAL EXAMPLES JAILBREAK LARGE LANGUAGE MODELS
- [arXiv Paper](https://arxiv.org/abs/2306.13213)
- [Detoxify GitHub Repository](https://github.com/unitaryai/detoxify) - Trained models & code to predict toxic comments on 3 Jigsaw challenges
- [Real Toxicity Prompts](https://allenai.org/data/real-toxicity-prompts) - Note: This paper focuses on visuals

### Red Teaming Language Models with Language Models
- [arXiv Paper](https://arxiv.org/abs/2202.03286)
- Exploration of red teaming LMs using another LM. Automatically finds cases where a target LM behaves harmfully. No datasets provided.

### Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned
- [arXiv Paper](https://arxiv.org/abs/2209.07858)
- [GitHub Repository](https://github.com/anthropics/hh-rlhf) - Same as the first paper listed

### Safety Assessment of Chinese Large Language Models
- [arXiv Paper](https://arxiv.org/abs/2304.10436)
- [GitHub Repository](https://github.com/thu-coai/Safety-Prompts) - Openly releases a dataset for safety assessment of Chinese LLMs


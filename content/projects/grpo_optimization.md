title: Improving LLMs as Optimizers Using GRPO
date: 2025-04-22
order: 3
description: A novel approach to enhancing language models' ability to solve traveling salesperson problems through guided reinforcement learning.
image: tsp-optimization.jpg
github_url: https://github.com/fahyjo/llm-final-project
paper_url: https://drive.google.com/file/d/1xCPaNX3bneK4-bHEgLM0q7i5QrpgTDxH/view?usp=sharing
tags: [Reinforcement Learning, GRPO, Large Language Models, Optimization, Traveling Salesperson Problem]
technologies: [Python, GRPO, Qwen2.5, TRL, Unsloth, vLLM, LoRA]

## Project Overview

This project explores an innovative approach to enhancing language models' ability to solve optimization problems, specifically the Traveling Salesperson Problem (TSP), using Guided Reinforcement through Policy Optimization (GRPO). By fine-tuning a Qwen2.5-3B-Instruct model, we demonstrate that LLMs can be improved as optimization solvers through targeted reinforcement learning techniques.

## The Challenge of Optimization

While large language models have shown remarkable capabilities across various domains, their application to constrained optimization problems remains challenging:
- Optimization traditionally relies on specialized algorithmic solvers
- LLMs lack the systematic search capabilities of traditional optimizers
- Standard fine-tuning approaches may not effectively improve optimization performance

GRPO offers a promising approach by allowing efficient reinforcement learning on problems with verifiably correct answers, potentially democratizing LLM fine-tuning for specialized applications.

## Data Generation

We developed a custom pipeline to generate standardized TSP datasets:
- Random points with integer x,y coordinates in the range [-100, 100]
- Unique identifiers for each point/city
- Calculated optimal solutions using brute force (for problems ≤10 cities) or simulated annealing (for larger problems)
- Structured prompts containing node coordinates, distance matrices, and example solutions

## Methodology

### GRPO Implementation

We leveraged several advanced techniques to make GRPO training efficient:
- TRL library's GRPO implementation as the core framework
- Unsloth, vLLM, 4-bit quantization, and LoRA for improved speed and reduced memory requirements
- A100 GPUs from the Delta cluster for compute resources
- Qwen2.5-3B-Instruct as our base model after testing various architectures

### Custom Reward Functions

We designed five specialized reward functions to guide the model:
1. **Scaled Accuracy Reward** (weight: 5.0): Variable reward based on proximity to optimal solution
2. **Improvement Reward** (weight: 2.5): Reward for outperforming example solutions
3. **Valid Response Reward**: Reward for routes that satisfy problem constraints
4. **Soft Format Reward**: Reward for including proper reasoning and trace tags
5. **Strict Format Reward**: Reward for adhering to stricter formatting requirements

## Results

Our GRPO-enhanced model (Qwen2.5-TSP) demonstrated significant improvements:

| Problem Size | Baseline Accuracy | GRPO-Enhanced Accuracy |
|--------------|------------------:|------------------------:|
| 5            | 0.46              | 0.79                    |
| 6            | 0.32              | 0.50                    |
| 7            | 0.12              | 0.21                    |
| 8            | 0.11              | 0.13                    |
| 9            | 0.08              | 0.08                    |

### Key Findings

- **Significant Improvement for Small Problems**: Qwen2.5-TSP showed a 71% improvement in solving 5-city problems
- **Moderate Generalization**: Despite training only on 5-city problems, improvements generalized to problems with 6-7 cities
- **Format Compliance**: Format-related rewards were quickly optimized (~100 training steps)
- **Better Reasoning Traces**: Qwen2.5-TSP demonstrated more methodical problem-solving approaches compared to the baseline model

## Limitations and Future Work

While our approach showed promise, several limitations emerged:
- Diminishing returns for larger problems (10+ cities)
- Iterative approaches were challenging to integrate with existing GRPO frameworks
- Limited success with binary reward functions (only rewarding optimal solutions)

Future directions could include:
- Exploring iterative solving approaches with GRPO
- Testing larger, more capable base models
- Developing more sophisticated reward mechanisms for complex optimization problems

## Conclusion

Our project demonstrates that targeted reinforcement learning can enhance LLMs' ability to solve optimization problems. While the improvements are most significant for smaller problems, the generalization to moderately larger problems suggests LLMs can learn transferable optimization strategies.

The project contributes to the emerging field of LLMs as optimization tools, though practical limitations suggest these approaches may complement rather than replace traditional optimization algorithms.

## Team

This project was conducted by Jacob Gottesman and John Fahy as part of advanced coursework in spring 2024.
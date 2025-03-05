# Engineering-Simulation-VLM-Benchmark
This repository provides a benchmark for evaluating the performance of Vision-Language Models (VLMs) on tasks related to engineering simulation data and analysis

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/xxxx.xxxxx)

## Overview

This is a multimodal benchmark dataset for evaluating vision-language models (VLMs) on their ability to understand and reason about engineering simulations. It contains data from 12 distinct simulation examples (6 structural, 6 fluid dynamics) across three modalities (images, videos, and text), paired with 40 domain-specific true/false questions designed by engineering experts.

<p align="center">
<img src="paper/figures/Image Modality.png" alt="Sample structural and fluid simulations" width="800"/>
</p>

This repository contains:
1. The benchmark dataset (questions and answers in JSON format)
2. Simulation outputs in three modalities:
   - Static images of simulation results
   - Videos showing animated visualizations
   - Text reports with simulation parameters and results
3. The academic paper "Simulation vs. Hallucination: Assessing Vision-Language Model Question Answering Capabilities in Engineering Simulations"
4. Documentation on benchmark usage and evaluation guidelines

## Benchmark Description

The benchmark consists of 40 true/false questions (20 for structural simulations, 20 for fluid dynamics) designed to test VLMs' understanding of engineering principles and their ability to interpret simulation outputs.

### Structural Simulations

- **File_1**: Bicycle crank under load
- **File_2**: Pretension bolt assembly
- **File_3**: Thermal stress expansion case
- **File_4**: Point mass system (drone)
- **File_5**: Valve housing under pressure
- **File_6**: Brittle material under bending and torsion

### Fluid Dynamics Simulations

- **File_7**: Airfoil
- **File_8**: Falling-sphere viscometer
- **File_9**: Natural convection model
- **File_10**: High-speed rail aerodynamics
- **File_11**: Heat exchange pipe flow
- **File_12**: Pressure-driven cavitating flow

## Usage

### Benchmark Format

The benchmark is provided in JSON format (`qa-benchmark-with-qids.json`) with the following structure:

```json
{
  "structural": {
    "description": "Questions related to structural simulation analysis",
    "questions": [
      {
        "qid": "a7e94b2c6f1d83052c9e",
        "question": "Are there any stress concentrations exceeding material limits?"
      },
      // Additional questions...
    ],
    "files": {
      "File_1": {
        "answers": {
          "a7e94b2c6f1d83052c9e": false,
          // Additional answers...
        }
      },
      // Additional files...
    }
  },
  "fluid": {
    // Similar structure for fluid dynamics questions and answers
  }
}
```

### Using the Benchmark

Here's a minimal example of how to load and work with the benchmark data:

```python
import json

# Load the benchmark data
def load_benchmark(benchmark_path="benchmark/qa-benchmark-with-qids.json"):
    """Load the SeeSim benchmark questions and answers."""
    with open(benchmark_path, 'r') as f:
        benchmark_data = json.load(f)
    return benchmark_data
    
# Example usage
benchmark = load_benchmark()

# Access questions for a specific domain
structural_questions = benchmark["structural"]["questions"]
fluid_questions = benchmark["fluid"]["questions"]

# Access answers for a specific file
file1_answers = benchmark["structural"]["files"]["File_1"]["answers"]

# Example of evaluating a model (pseudocode)
correct_count = 0
total_count = 0
for qid, true_answer in file1_answers.items():
    # Get the question text
    question_text = next(q["question"] for q in structural_questions if q["qid"] == qid)
    
    # Get model prediction (implement this based on your model)
    # model_answer = your_model_prediction(image_path, question_text)
    
    # Compare with ground truth
    # if model_answer == true_answer:
    #     correct_count += 1
    # total_count += 1

# Calculate accuracy
# accuracy = correct_count / total_count
```

### Models Evaluated in Our Paper

We evaluated the following models in our benchmark paper:

- **Image Models**:
  - Llama-3.2-11B-Vision (`meta-llama/Llama-3.2-11B-Vision`)
  - Qwen2.5-VL-7B-Instruct (`Qwen/Qwen2.5-VL-7B-Instruct`)
  - blip2-opt-2.7b (`Salesforce/blip2-opt-2.7b`)
  - kosmos-2-patch14-224 (`microsoft/kosmos-2-patch14-224`)

- **Video Models**:
  - llava-onevision-qwen2-7b-ov-hf (`llava-hf/llava-onevision-qwen2-7b-ov-hf`)
  - Qwen2.5-VL-7B-Instruct (`Qwen/Qwen2.5-VL-7B-Instruct`)
  - blip2-opt-2.7b and kosmos-2-patch14-224 (frame-by-frame processing)

- **Text Models**:
  - llava-onevision-qwen2-7b-ov-hf (`llava-hf/llava-onevision-qwen2-7b-ov-hf`)
  - Phi-3-small-128k-instruct (`microsoft/phi-3-small-128k-instruct`)
  - Qwen2.5-VL-7B-Instruct (`Qwen/Qwen2.5-VL-7B-Instruct`)
  - Llama-3.2-11B-Vision (`meta-llama/Llama-3.2-11B-Vision`)

## Evaluation Metrics

We encourage using the following metrics for evaluation:

1. **Overall Accuracy**: Percentage of correctly answered questions across all files
2. **Domain-Specific Accuracy**: Separate accuracies for structural and fluid dynamics questions
3. **Logical Consistency**: Rate of contradictions between paired opposing questions
4. **Validation Accuracy**: Performance on questions testing fundamental physical laws

## Paper

The full paper "Simulation vs. Hallucination: Assessing Vision-Language Model Question Answering Capabilities in Engineering Simulations" is available in the `paper/` directory. The paper presents a systematic evaluation of state-of-the-art vision-language models (including LLaVA, Phi-3, Qwen, and BLIP) on engineering simulation interpretation tasks.

Key findings include:
- Text modality consistently outperforms visual modalities
- Models perform better on structural analysis than fluid dynamics
- Current VLMs show significant inconsistencies when answering related questions
- Performance is still far below requirements for reliable engineering applications

## Citation

If you use this benchmark in your research, please cite our paper:

```bibtex
@article{seesim2025,
  title={Simulation vs. Hallucination: Assessing Vision-Language Model Question Answering Capabilities in Engineering Simulations},
  author={Author1 and Author2 and Author3},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year={2025}
}
```

## License

This repository is released under the MIT License. The benchmark dataset is released for research purposes only.

## Acknowledgments

We thank Ansys for providing the simulation examples used in this benchmark.

## Contact

For questions or issues, please open an issue in this repository or contact the authors at [email@example.com].

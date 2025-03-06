# OpenSeeSimE: Engineering Simulation Benchmark for Vision-Language Models

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/xxxx.xxxxx)

## Overview

OpenSeeSimE is a multimodal benchmark for evaluating the capabilities of vision-language models (VLMs) in understanding and reasoning about engineering simulation outputs. This benchmark addresses the growing need for evaluating AI models on domain-specific technical tasks beyond general-purpose visual understanding.

<p align="center">
<img src="paper/SimulationExamples.png" alt="Sample structural and fluid simulations" width="800"/>
</p>

## Dataset Description

The OpenSeeSimE benchmark comprises multimodal data from 12 distinct simulation examples (6 structural, 6 fluid dynamics) generated using standard engineering simulation software (Ansys). Each simulation is represented in three modalities:

- **Images**: Static visualizations of simulation results (.png format)
- **Videos**: Animated visualizations of simulation behavior (.gif for structural, .mp4 for fluid)
- **Text**: Detailed simulation reports and parameters (.txt format)

### Simulation Types

#### Structural Simulations
- **File_1**: Bicycle crank under load
- **File_2**: Pretension bolt assembly
- **File_3**: Thermal stress expansion case
- **File_4**: Point mass system (drone)
- **File_5**: Valve housing under pressure
- **File_6**: Brittle material under bending and torsion

#### Fluid Dynamics Simulations
- **File_7**: Airfoil
- **File_8**: Falling-sphere viscometer
- **File_9**: Natural convection model
- **File_10**: High-speed rail aerodynamics
- **File_11**: Heat exchange pipe flow
- **File_12**: Pressure-driven cavitating flow

## Task Definition

The benchmark defines a binary question-answering task using 40 expert-crafted true/false questions (20 for structural simulations, 20 for fluid dynamics) that test understanding of engineering principles and the ability to interpret simulation outputs.

Example questions include:
- "Are there any stress concentrations exceeding material limits?"
- "Is mass conservation satisfied?"
- "Is the flow regime laminar?" 

These questions are designed to test fundamental engineering concepts while remaining geometry-agnostic to evaluate model generalization capabilities.

## Benchmark Format

The benchmark is provided as a JSON file (`benchmark/qa-benchmark-with-qids.json`) with the following structure:

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

## Usage

### Loading the Benchmark

```python
import json

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
```

### Loading Simulation Data

```python
# Example of loading an image file
def load_image(domain, file_id):
    """Load an image file for a specific domain and file ID."""
    image_path = f"data/{domain}/images/{file_id}.png"
    # Load using your preferred image library
    return image_path

# Example of loading a video file
def load_video(domain, file_id):
    """Load a video file for a specific domain and file ID."""
    ext = "gif" if domain == "structural" else "mp4"
    video_path = f"data/{domain}/videos/{file_id}.{ext}"
    # Load using your preferred video library
    return video_path

# Example of loading a text file
def load_text(domain, file_id):
    """Load a text file for a specific domain and file ID."""
    text_path = f"data/{domain}/text/{file_id}.txt"
    with open(text_path, 'r') as f:
        text_content = f.read()
    return text_content
```

For more detailed evaluation guidelines, see `benchmark/evaluation_guidelines.md`.

## Directory Structure

```
SeeSim-Benchmark/
├── README.md
├── LICENSE
├── data/
│   ├── structural/
│   │   ├── images/      # File_1.png, File_2.png, etc.
│   │   ├── videos/      # File_1.gif, File_2.gif, etc.
│   │   └── text/        # File_1.txt, File_2.txt, etc.
│   └── fluid/
│       ├── images/      # File_7.png, File_8.png, etc.
│       ├── videos/      # File_7.mp4, File_8.mp4, etc.
│       └── text/        # File_7.txt, File_8.txt, etc.
├── benchmark/
│   ├── qa-benchmark-with-qids.json
│   ├── evaluation_guidelines.md
│   ├── benchmark_loader.py
│   └── metadata.json
└── paper/
    ├── simulation_vs_hallucination.pdf
    └── figures/
```

## Evaluation Metrics

We recommend using the following metrics for evaluation:

1. **Overall Accuracy**: Percentage of correctly answered questions across all files
2. **Domain-Specific Accuracy**: Separate accuracies for structural and fluid dynamics questions
3. **Logical Consistency**: Rate of contradictions between paired opposing questions
4. **Validation Accuracy**: Performance on questions testing fundamental physical laws

## Baseline Results

Our paper establishes baseline performance metrics for several state-of-the-art vision-language models across three modalities:

| Model | Text | Video | Image |
|-------|------|-------|-------|
| LLaVA | 66.3% | 53.8% | - |
| Phi-3 | 62.5% | - | - |
| Qwen | 54.6% | 52.9% | 52.9% |
| Llama | 52.1% | - | 54.6% |
| BLIP | - | 52.9% | 52.9% |
| Kosmos | - | 52.9% | 52.9% |

Key findings:
- Text modality consistently outperforms visual modalities
- Models perform better on structural analysis than fluid dynamics
- Performance is still far below requirements for reliable engineering applications
- Models show significant inconsistencies when answering related questions

## Ethical Considerations

This benchmark is released for research purposes only. The ground truth answers are included to enable reproducibility and transparent evaluation. Researchers are encouraged to use these answers only for evaluation and not for fine-tuning models specifically to this benchmark.

## Citation

If you use this benchmark in your research, please cite our paper:

<!-- ```bibtex
@article{seesim2025,
  title={Simulation vs. Hallucination: Assessing Vision-Language Model Question Answering Capabilities in Engineering Simulations},
  author={Author1 and Author2 and Author3},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year={2025}
}
``` -->

Upcoming Citation

## License

This repository is released under the MIT License. The benchmark dataset is released for research purposes.

## Acknowledgments

We thank Ansys for providing the simulation examples used in this benchmark.

## Contact

For questions or issues, please open an issue in this repository.

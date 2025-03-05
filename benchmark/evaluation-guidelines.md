# SeeSim Benchmark Evaluation Guidelines

This document outlines the recommended approach for evaluating vision-language models on the SeeSim engineering simulation benchmark.

## Input Format

For each model evaluation, you should provide:

1. **Model**: The specific model being evaluated (e.g., `meta-llama/Llama-3.2-11B-Vision`)
2. **Modality**: The data modality being used (image, video, or text)
3. **Domain**: The simulation domain (structural or fluid)
4. **Files**: The specific simulation files being evaluated (e.g., File_1 through File_12)

## Task Definition

The task is structured as a binary question-answering problem:

1. Present the model with simulation data (image, video, or text)
2. Ask a true/false question from the benchmark
3. Record the model's response as true or false
4. Compare against the ground truth answer

## Prompting Guidelines

We recommend standardizing prompts to enable fair comparison between models:

### Image/Video Prompts

```
[Image/Video]

Question: {question_text} (True/False)

Answer with only True or False:
```

### Text Prompts

```
[Simulation Text Description]

Question: {question_text} (True/False)

Answer with only True or False:
```

## Response Processing

Model responses should be processed as follows:

1. Convert the response to lowercase
2. If the response contains "true" (and not "false"), classify as True
3. If the response contains "false" (and not "true"), classify as False
4. If the response starts with "t", classify as True
5. If the response starts with "f", classify as False
6. For ambiguous responses, classify based on the presence of "t" vs "f"

## Evaluation Metrics

Calculate the following metrics:

1. **Accuracy**: The percentage of correct answers
   - Overall accuracy across all questions
   - Domain-specific accuracy (structural vs. fluid)
   - Per-file accuracy

2. **Logical Consistency**: For paired opposing questions (e.g., "Is the flow laminar?" vs. "Is the flow turbulent?"), calculate the percentage of consistent answers.

3. **Validation Accuracy**: For questions testing fundamental physical laws (e.g., "Is mass conservation satisfied?"), calculate the percentage of correct answers.

## Aggregating Results

For video evaluation, we recommend:
- Processing multiple frames and using majority voting
- For native video models, process the entire video sequence
- For image-only models, sample frames at regular intervals (e.g., 1 frame per second)

## Reporting Results

When reporting results, include:
1. The model name and version
2. Parameter count
3. Accuracy metrics (overall, by domain, by file)
4. Any modifications to the standard evaluation protocol

## Paired Question Analysis

Our benchmark contains several pairs of questions designed to test logical consistency. The key pairs include:

### Structural Simulation
- "Is the deformation primarily elastic?" vs. "Does the structure experience any plastic deformation?"
- "Are stress concentrations exceeding material limits?" vs. "Is the Factor of Safety greater than 1?"
- "Are thermal stresses negligible?" vs. "Is von Mises stress the appropriate failure criterion?"

### Fluid Simulation
- "Is the flow regime laminar?" vs. "Is the flow regime turbulent?"
- "Is buoyancy negligible?" vs. "Is natural convection significant?"
- "Is the flow fully developed?" vs. "Is there evidence of flow separation?"

Models should provide logically consistent answers to these paired questions.

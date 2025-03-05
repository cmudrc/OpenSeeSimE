import json
import os
from typing import Dict, List, Any, Optional, Tuple

def load_benchmark(benchmark_path: str = "benchmark/qa-benchmark-with-qids.json") -> Dict:
    """
    Load the SeeSim benchmark questions and answers.
    
    Args:
        benchmark_path: Path to the benchmark JSON file
        
    Returns:
        Dictionary containing benchmark data
    """
    try:
        with open(benchmark_path, 'r') as f:
            benchmark_data = json.load(f)
        return benchmark_data
    except FileNotFoundError:
        print(f"Error: Benchmark file not found at {benchmark_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in benchmark file {benchmark_path}")
        return {}

def get_questions_for_domain(benchmark_data: Dict, domain: str) -> List[Dict]:
    """
    Get all questions for a specific domain.
    
    Args:
        benchmark_data: Loaded benchmark data
        domain: Domain name ('structural' or 'fluid')
        
    Returns:
        List of question dictionaries with qid and question text
    """
    if domain not in benchmark_data:
        print(f"Error: Domain '{domain}' not found in benchmark data")
        return []
        
    return benchmark_data[domain]["questions"]

def get_answers_for_file(benchmark_data: Dict, domain: str, file_id: str) -> Dict:
    """
    Get all ground truth answers for a specific simulation file.
    
    Args:
        benchmark_data: Loaded benchmark data
        domain: Domain name ('structural' or 'fluid')
        file_id: File identifier (e.g., 'File_1')
        
    Returns:
        Dictionary mapping question IDs to boolean answers
    """
    if domain not in benchmark_data:
        print(f"Error: Domain '{domain}' not found in benchmark data")
        return {}
        
    if "files" not in benchmark_data[domain]:
        print(f"Error: No files found in domain '{domain}'")
        return {}
        
    if file_id not in benchmark_data[domain]["files"]:
        print(f"Error: File '{file_id}' not found in domain '{domain}'")
        return {}
        
    return benchmark_data[domain]["files"][file_id]["answers"]

def calculate_accuracy(predictions: Dict[str, bool], ground_truth: Dict[str, bool]) -> Tuple[float, int, int]:
    """
    Calculate accuracy of model predictions against ground truth.
    
    Args:
        predictions: Dictionary mapping question IDs to predicted boolean answers
        ground_truth: Dictionary mapping question IDs to ground truth boolean answers
        
    Returns:
        Tuple of (accuracy, correct_count, total_count)
    """
    if not ground_truth:
        return 0.0, 0, 0
        
    correct_count = 0
    total_count = 0
    
    for qid, true_answer in ground_truth.items():
        if qid in predictions:
            if predictions[qid] == true_answer:
                correct_count += 1
            total_count += 1
    
    accuracy = correct_count / total_count if total_count > 0 else 0.0
    return accuracy, correct_count, total_count

def get_question_text(questions: List[Dict], qid: str) -> Optional[str]:
    """
    Get question text for a given question ID.
    
    Args:
        questions: List of question dictionaries
        qid: Question ID to look up
        
    Returns:
        Question text or None if not found
    """
    for q in questions:
        if q["qid"] == qid:
            return q["question"]
    return None

def get_paired_questions() -> Dict[str, List[Tuple[str, str]]]:
    """
    Get the list of paired opposing questions for consistency analysis.
    
    Returns:
        Dictionary mapping domains to lists of qid pairs
    """
    return {
        "structural": [
            # Elastic vs. plastic deformation
            ("b12d8f45e3a670c92178", "n46e2f9ba03e6545205b"),
            # Stress concentration vs. factor of safety
            ("a7e94b2c6f1d83052c9e", "r80c6d90f47c0329649f"),
            # Thermal stresses vs. von Mises criterion
            ("l24c0d81f81c4103083f", "e57f1d63c42a0589b63e")
        ],
        "fluid": [
            # Laminar vs. turbulent
            ("bb0a6b65d47a0320349d", "ee3d9e73a70d3983672a"),
            # Buoyancy vs. natural convection
            ("ii7b3c37e14b7767016e", "x46c2d01f03c6546905f"),
            # Fully developed vs. flow separation
            ("v24a0b19d81a4103783d", "hh6a2b01d03a6546905d")
        ]
    }

def get_validation_questions() -> Dict[str, List[str]]:
    """
    Get the list of validation questions testing fundamental physical laws.
    
    Returns:
        Dictionary mapping domains to lists of qids
    """
    return {
        "structural": [
            "d46c2b17e50f38a4271d",  # Do reaction forces balance external loads?
            "k13b9c27e70b3982172e"   # Does the simulation converge within acceptable error limits?
        ],
        "fluid": [
            "cc1b7c01e58b1541450e"   # Is mass conservation satisfied?
        ]
    }

# Example usage
if __name__ == "__main__":
    # Load the benchmark
    benchmark = load_benchmark()
    
    # Print statistics
    if benchmark:
        for domain in ["structural", "fluid"]:
            if domain in benchmark:
                questions = get_questions_for_domain(benchmark, domain)
                print(f"Domain: {domain}")
                print(f"  Number of questions: {len(questions)}")
                
                files = benchmark[domain].get("files", {})
                print(f"  Number of files: {len(files)}")
                
                for file_id in files:
                    answers = get_answers_for_file(benchmark, domain, file_id)
                    print(f"  File {file_id}: {len(answers)} answers")
                    
                print()
                
        # Example of paired questions
        paired_questions = get_paired_questions()
        for domain, pairs in paired_questions.items():
            print(f"Paired questions in {domain} domain: {len(pairs)}")

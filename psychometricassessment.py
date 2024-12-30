"""
Canonical psychometric assessment code
"""
import json
from dataclasses import dataclass
from typing import List, Dict, Optional, Callable
from enum import Enum
import time
import threading
from queue import Queue
import random

class TestCategory(Enum):
    EMBEDDED_SYSTEMS = "embedded_systems"
    MEDICAL_SOFTWARE = "medical_software"
    INDUSTRIAL_CONTROL = "industrial_control"
    SYSTEM_DESIGN = "system_design"
    PROBLEM_SOLVING = "problem_solving"

@dataclass
class TestQuestion:
    category: TestCategory
    question: str
    code_template: Optional[str]
    time_limit: int  # in seconds
    test_cases: List[Dict]
    scoring_criteria: Dict[str, float]

class PsychometricTest:
    def __init__(self):
        self.questions: List[TestQuestion] = []
        self.responses: Dict = {}
        self.scores: Dict = {}
        
    def add_question(self, question: TestQuestion):
        self.questions.append(question)
        
    def run_test(self, candidate_id: str):
        print(f"Starting assessment for candidate {candidate_id}")
        self.responses[candidate_id] = {}
        self.scores[candidate_id] = {}
        
        for question in self.questions:
            response = self._present_question(question)
            self.responses[candidate_id][question.category.value] = response
            score = self._evaluate_response(question, response)
            self.scores[candidate_id][question.category.value] = score
            
    def _present_question(self, question: TestQuestion) -> Dict:
        print(f"\n{'-'*80}")
        print(f"Category: {question.category.value}")
        print(f"\n{question.question}")
        
        if question.code_template:
            print(f"\nTemplate:\n{question.code_template}")
            
        response = {}
        response['start_time'] = time.time()
        
        # Create a queue for the response
        response_queue = Queue()
        
        def input_thread():
            code = input("Enter your solution (or 'skip' to move on):\n")
            response_queue.put(code)
        
        # Start input thread with timeout
        thread = threading.Thread(target=input_thread)
        thread.daemon = True
        thread.start()
        
        # Wait for response or timeout
        thread.join(timeout=question.time_limit)
        
        if thread.is_alive():
            print("\nTime's up!")
            response['completed'] = False
            response['code'] = None
        else:
            code = response_queue.get()
            response['completed'] = True
            response['code'] = code
            
        response['end_time'] = time.time()
        return response
        
    def _evaluate_response(self, question: TestQuestion, response: Dict) -> Dict:
        score = {
            'technical_score': 0.0,
            'problem_solving_score': 0.0,
            'time_management_score': 0.0
        }
        
        if not response['completed']:
            return score
            
        # Evaluate technical implementation
        if response['code'] and response['code'].lower() != 'skip':
            try:
                for test_case in question.test_cases:
                    # Here you would actually run the code against test cases
                    # For now, we'll simulate evaluation
                    score['technical_score'] += self._evaluate_technical_merit(
                        response['code'], test_case
                    )
            except Exception as e:
                print(f"Error in evaluation: {e}")
                
        # Evaluate problem-solving approach
        score['problem_solving_score'] = self._evaluate_problem_solving(
            response['code'], question.scoring_criteria
        )
        
        # Evaluate time management
        time_taken = response['end_time'] - response['start_time']
        score['time_management_score'] = min(
            1.0, question.time_limit / max(time_taken, 1)
        )
        
        return score
        
    def _evaluate_technical_merit(self, code: str, test_case: Dict) -> float:
        # Simplified scoring for demonstration
        # In practice, you would:
        # 1. Run the code in a sandbox
        # 2. Apply test cases
        # 3. Check output correctness
        # 4. Analyze code quality
        return random.uniform(0.6, 1.0)  # Placeholder
        
    def _evaluate_problem_solving(self, code: str, criteria: Dict) -> float:
        # Analyze problem-solving approach
        # Look for patterns that indicate good problem-solving:
        # - Error handling
        # - Edge cases
        # - Performance considerations
        # - Code organization
        return random.uniform(0.7, 1.0)  # Placeholder

# Example usage
def create_embedded_systems_question() -> TestQuestion:
    return TestQuestion(
        category=TestCategory.EMBEDDED_SYSTEMS,
        question="""
        Design a class for managing a DVD recorder's buffer system.
        Requirements:
        - Handle incoming video stream in chunks
        - Implement circular buffer with configurable size
        - Provide methods for reading and writing frames
        - Include error handling for buffer overflow/underflow
        """,
        code_template="""
class DVDBufferManager:
    def __init__(self, buffer_size: int):
        # Initialize your buffer system here
        pass
        
    def write_frame(self, frame_data: bytes) -> bool:
        # Implement frame writing logic
        pass
        
    def read_frame(self) -> Optional[bytes]:
        # Implement frame reading logic
        pass
        
    def get_buffer_status(self) -> Dict:
        # Return buffer statistics
        pass
""",
        time_limit=900,  # 15 minutes
        test_cases=[
            {
                'input': {'buffer_size': 1024, 'frames': [b'test'*256]*4},
                'expected': {'overflow': False, 'frames_written': 4}
            },
            {
                'input': {'buffer_size': 512, 'frames': [b'test'*256]*3},
                'expected': {'overflow': True, 'frames_written': 2}
            }
        ],
        scoring_criteria={
            'memory_efficiency': 0.3,
            'error_handling': 0.3,
            'performance': 0.2,
            'code_quality': 0.2
        }
    )

def create_medical_software_question() -> TestQuestion:
    return TestQuestion(
        category=TestCategory.MEDICAL_SOFTWARE,
        question="""
        Implement a safety monitoring system for a proton beam treatment system.
        Requirements:
        - Monitor beam intensity in real-time
        - Implement emergency shutdown if values exceed thresholds
        - Log all events with timestamps
        - Provide status updates at configurable intervals
        """,
        code_template="""
class ProtonBeamMonitor:
    def __init__(self, max_intensity: float, update_interval: int):
        # Initialize monitoring system
        pass
        
    def update_beam_reading(self, intensity: float) -> Dict:
        # Process new intensity reading
        pass
        
    def get_status_report(self) -> Dict:
        # Generate status report
        pass
        
    def emergency_shutdown(self) -> bool:
        # Implement shutdown procedure
        pass
""",
        time_limit=1200,  # 20 minutes
        test_cases=[
            {
                'input': {'intensity': 5.0, 'max_intensity': 10.0},
                'expected': {'shutdown': False, 'status': 'normal'}
            },
            {
                'input': {'intensity': 12.0, 'max_intensity': 10.0},
                'expected': {'shutdown': True, 'status': 'emergency'}
            }
        ],
        scoring_criteria={
            'safety_handling': 0.4,
            'real_time_processing': 0.3,
            'logging_quality': 0.2,
            'code_organization': 0.1
        }
    )

# Initialize and run test
def main():
    test = PsychometricTest()
    test.add_question(create_embedded_systems_question())
    test.add_question(create_medical_software_question())
    
    candidate_id = input("Enter candidate ID: ")
    test.run_test(candidate_id)
    
    print("\nTest Results:")
    print(json.dumps(test.scores[candidate_id], indent=2))

if __name__ == "__main__":
    main()
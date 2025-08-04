# Knapsack Optimization with Genetic Algorithm

A comprehensive genetic algorithm implementation for solving the knapsack optimization problem, developed as part of FIAP coursework.

## 🎯 Project Overview

This project implements a genetic algorithm to solve the 0/1 knapsack problem, where the goal is to maximize the total value of selected items while staying within a weight capacity constraint. The implementation includes:

- **Complete genetic algorithm workflow** with population initialization, selection, crossover, mutation, and elitism
- **Real-time visualization** of fitness evolution over generations
- **Comprehensive test suite** with 67 tests including brute force validation
- **Clean, modular architecture** following software engineering best practices

## 📦 Project Structure

```
FIAP-packsack-otimizacao-de-espaco/
├── src/
│   ├── ga/                     # Genetic algorithm modules
│   │   ├── crossover.py        # Crossover operations (one-point)
│   │   ├── fitness.py          # Fitness evaluation and Item class
│   │   ├── mutation.py         # Mutation operations (bit-flip)
│   │   ├── population.py       # Population creation and management
│   │   └── selection.py        # Selection methods (tournament, roulette)
│   └── main.py                 # Main algorithm execution and visualization
├── tests/                      # Comprehensive test suite (67 tests)
│   ├── ga/                     # Unit tests for GA components
│   │   ├── test_crossover.py   # Crossover function tests
│   │   ├── test_fitness.py     # Fitness evaluation tests
│   │   ├── test_mutation.py    # Mutation function tests
│   │   ├── test_population.py  # Population creation tests
│   │   └── test_selection.py   # Selection method tests
│   └── test_main.py           # Integration tests and brute force validation
├── requirements.txt           # Project dependencies
├── pytest.ini               # Test configuration
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd FIAP-packsack-otimizacao-de-espaco
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# or
venv\Scripts\activate          # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Application

Execute the genetic algorithm:
```bash
python src/main.py
```

This will:
- Generate a random knapsack problem (50 items, capacity 200)
- Run the genetic algorithm for 200 generations
- Display real-time progress in the console
- Show a matplotlib visualization of fitness evolution

### Algorithm Parameters

The current configuration in `main.py`:
- **Items**: 50 randomly generated items
- **Population Size**: 100 individuals
- **Generations**: 200
- **Mutation Rate**: 5%
- **Tournament Size**: 5
- **Elitism**: Top 5 individuals preserved
- **Knapsack Capacity**: 200 units

## 🧪 Testing

### Running Tests

Execute the complete test suite:
```bash
pytest tests/ -v
```

Run specific test modules:
```bash
pytest tests/ga/test_fitness.py -v        # Fitness function tests
pytest tests/test_main.py -v              # Integration tests
```

### Test Coverage

The project includes **67 comprehensive tests**:

- **Unit Tests**: Individual GA component validation
- **Integration Tests**: Complete algorithm workflow
- **Brute Force Validation**: Verification against optimal solutions for small instances
- **Edge Case Testing**: Error handling and boundary conditions

**Test Results**: ✅ 67/67 tests passing (100% success rate)

## 🧬 Genetic Algorithm Components

### 1. **Representation**
- **Encoding**: Binary strings where 1 = item selected, 0 = item not selected
- **Item Class**: Each item has value and weight attributes

### 2. **Selection Methods**
- **Tournament Selection**: Selects best individual from random tournament
- **Roulette Selection**: Probability-based selection proportional to fitness

### 3. **Crossover**
- **One-Point Crossover**: Single random crossover point

### 4. **Mutation**
- **Bit-Flip Mutation**: Random bit flipping with configurable probability

### 5. **Fitness Function**
- Maximizes total value of selected items
- Returns 0 for solutions exceeding weight capacity
- Validates against negative values/weights

## 📊 Performance

The genetic algorithm demonstrates excellent performance:

- **Solution Quality**: Finds solutions within 10-20% of optimal for small instances
- **Convergence**: Shows consistent improvement over generations
- **Efficiency**: Handles 50-item problems in under 1 second
- **Scalability**: Tested with up to 100 items successfully

## 🛠️ Development

### Code Quality
- **Clean Architecture**: Modular design with clear separation of concerns
- **Type Safety**: Proper type hints throughout the codebase
- **Documentation**: Self-documenting code with meaningful names
- **Testing**: Comprehensive test coverage with multiple validation approaches

### Dependencies
```
matplotlib==3.8.0    # Visualization
numpy==1.24.3        # Numerical operations
pytest==8.4.1        # Testing framework
```

## 📈 Example Output

```
=== Knapsack Optimization with Genetic Algorithm ===
Knapsack capacity: 200
Population size: 100
Generations: 200
Mutation rate: 0.05
--------------------------------------------------
Generation   0: Best=156, Avg= 89.23
Generation  10: Best=178, Avg=134.56
Generation  20: Best=189, Avg=156.78
...
Generation 200: Best=195, Avg=182.34

==================================================
RESULTS
==================================================
Best fitness achieved: 195
Total weight: 198/200
Weight utilization: 99.0%
Selected items: 23 out of 50
```

## 🎓 Academic Context

This project was developed for **FIAP** coursework, demonstrating:
- Genetic algorithm implementation
- Software engineering best practices
- Comprehensive testing methodologies
- Real-world optimization problem solving

## 📄 License

This project is developed for educational purposes as part of FIAP coursework.

---

**Developed by**: Danilo de Castro  
**Institution**: FIAP  
**Course**: Optimization Algorithms

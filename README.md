# KnapSack - Otimização de Espaço com Algoritmo Genético

Este projeto implementa um algoritmo genético para resolver o problema da mochila (knapsack), com o objetivo de otimizar o uso do espaço e maximizar o valor dos itens selecionados dentro de uma capacidade limitada.

## 📦 Estrutura do Projeto

```
FIAP-packsack-otimizacao-de-espaco/
├── src/
│   ├── ga/                 # Implementação do algoritmo genético
│   │   ├── crossover.py
│   │   ├── fitness.py
│   │   ├── individual.py
│   │   ├── mutation.py
│   │   ├── population.py
│   │   ├── selection.py
│   │   └── utils.py
│   └── main.py             # Ponto de entrada do projeto
├── tests/                  # Testes unitários
│   └── ga/
│       └── test_fitness.py
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## 🚀 Como Executar

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate.bat       # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o projeto:

```bash
python src/main.py
```

## 🧪 Executando os Testes

Para rodar os testes unitários com `pytest`:

```bash
PYTHONPATH=src pytest
```

## 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais. Licença livre para estudo e uso não comercial.

# Otimização da Mochila com Algoritmo Genético

Uma implementação abrangente de algoritmo genético para resolver o problema de otimização da mochila, desenvolvido como parte do curso da FIAP.

## 🎯 Visão Geral do Projeto

Este projeto implementa um algoritmo genético para resolver o problema da mochila 0/1, onde o objetivo é maximizar o valor total dos itens selecionados mantendo-se dentro da restrição de capacidade de peso. A implementação inclui:

- **Fluxo completo de algoritmo genético** com inicialização da população, seleção, cruzamento, mutação e elitismo
- **Visualização em tempo real** da evolução do fitness ao longo das gerações
- **Suíte abrangente de testes** com 67 testes incluindo validação por força bruta
- **Arquitetura modular e limpa** seguindo as melhores práticas de engenharia de software

## 📦 Estrutura do Projeto

```
FIAP-packsack-otimizacao-de-espaco/
├── src/
│   ├── ga/                     # Módulos do algoritmo genético
│   │   ├── crossover.py        # Operações de cruzamento (ponto único)
│   │   ├── fitness.py          # Avaliação de fitness e classe Item
│   │   ├── mutation.py         # Operações de mutação (bit-flip)
│   │   ├── population.py       # Criação e gerenciamento da população
│   │   └── selection.py        # Métodos de seleção (torneio, roleta)
│   └── main.py                 # Execução principal do algoritmo e visualização
├── tests/                      # Suíte abrangente de testes (67 testes)
│   ├── ga/                     # Testes unitários para componentes do AG
│   │   ├── test_crossover.py   # Testes das funções de cruzamento
│   │   ├── test_fitness.py     # Testes de avaliação de fitness
│   │   ├── test_mutation.py    # Testes das funções de mutação
│   │   ├── test_population.py  # Testes de criação da população
│   │   └── test_selection.py   # Testes dos métodos de seleção
│   └── test_main.py           # Testes de integração e validação por força bruta
├── requirements.txt           # Dependências do projeto
├── pytest.ini               # Configuração de testes
└── README.md                 # Documentação do projeto
```

## 🚀 Começando

### Pré-requisitos

- Python 3.10 ou superior
- Gerenciador de pacotes pip

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/rapzodo/FIAP-packsack-otimizacao-de-espaco
cd FIAP-packsack-otimizacao-de-espaco
```

2. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# ou
venv\Scripts\activate          # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### Executando a Aplicação

Execute o algoritmo genético:
```bash
python src/main.py
```

Isso irá:
- Gerar um problema de mochila aleatório (50 itens, capacidade 200)
- Executar o algoritmo genético por 200 gerações
- Exibir o progresso em tempo real no console
- Mostrar uma visualização matplotlib da evolução do fitness

### Parâmetros do Algoritmo

A configuração atual em `main.py`:
- **Itens**: 50 itens gerados aleatoriamente
- **Tamanho da População**: 100 indivíduos
- **Gerações**: 200
- **Taxa de Mutação**: 5%
- **Tamanho do Torneio**: 5
- **Elitismo**: Top 5 indivíduos preservados
- **Capacidade da Mochila**: 200 unidades

## 🧪 Testes

### Executando os Testes

Execute a suíte completa de testes:
```bash
pytest tests/ -v
```

Execute módulos de teste específicos:
```bash
pytest tests/ga/test_fitness.py -v        # Testes das funções de fitness
pytest tests/test_main.py -v              # Testes de integração
```

### Cobertura de Testes

O projeto inclui **67 testes abrangentes**:

- **Testes Unitários**: Validação individual dos componentes do AG
- **Testes de Integração**: Fluxo completo do algoritmo
- **Validação por Força Bruta**: Verificação contra soluções ótimas para instâncias pequenas
- **Testes de Casos Extremos**: Tratamento de erros e condições de contorno

**Resultados dos Testes**: ✅ 67/67 testes aprovados (100% de taxa de sucesso)

## 🧬 Componentes do Algoritmo Genético

### 1. **Representação**
- **Codificação**: Strings binárias onde 1 = item selecionado, 0 = item não selecionado
- **Classe Item**: Cada item possui atributos de valor e peso

### 2. **Métodos de Seleção**
- **Seleção por Torneio**: Seleciona o melhor indivíduo de um torneio aleatório
- **Seleção por Roleta**: Seleção baseada em probabilidade proporcional ao fitness

### 3. **Cruzamento**
- **Cruzamento de Ponto Único**: Ponto de cruzamento aleatório único

### 4. **Mutação**
- **Mutação Bit-Flip**: Inversão aleatória de bits com probabilidade configurável

### 5. **Função de Fitness**
- Maximiza o valor total dos itens selecionados
- Retorna 0 para soluções que excedem a capacidade de peso
- Valida contra valores/pesos negativos

## 📊 Performance

O algoritmo genético demonstra excelente performance:

- **Qualidade da Solução**: Encontra soluções dentro de 10-20% do ótimo para instâncias pequenas
- **Convergência**: Mostra melhoria consistente ao longo das gerações
- **Eficiência**: Lida com problemas de 50 itens em menos de 1 segundo
- **Escalabilidade**: Testado com sucesso com até 100 itens

## 🛠️ Desenvolvimento

### Qualidade do Código
- **Arquitetura Limpa**: Design modular com clara separação de responsabilidades
- **Segurança de Tipos**: Type hints adequados em todo o código
- **Documentação**: Código autodocumentado com nomes significativos
- **Testes**: Cobertura abrangente de testes com múltiplas abordagens de validação

### Dependências
```
matplotlib==3.8.0    # Visualização
numpy==1.24.3        # Operações numéricas
pytest==8.4.1        # Framework de testes
```

## 📈 Exemplo de Saída

```
=== Otimização da Mochila com Algoritmo Genético ===
Capacidade da mochila: 200
Tamanho da população: 100
Gerações: 200
Taxa de mutação: 0.05
--------------------------------------------------
Geração   0: Melhor=156, Média= 89.23
Geração  10: Melhor=178, Média=134.56
Geração  20: Melhor=189, Média=156.78
...
Geração 200: Melhor=195, Média=182.34

==================================================
RESULTADOS
==================================================
Melhor fitness alcançado: 195
Peso total: 198/200
Utilização do peso: 99.0%
Itens selecionados: 23 de 50
```

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido para o curso da **FIAP**, demonstrando:
- Implementação de algoritmos genéticos
- Melhores práticas de engenharia de software
- Metodologias abrangentes de testes
- Resolução de problemas de otimização do mundo real

## 👥 Colaboradores

- **Danilo de Castro** - Desenvolvedor Principal - [danilocastro81@gmail.com]

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso da FIAP.

---

**Desenvolvido por**: Danilo de Castro  
**Instituição**: FIAP  
**Curso**: Algoritmos de Otimização  
**Repositório**: [rapzodo/FIAP-packsack-otimizacao-de-espaco](https://github.com/rapzodo/FIAP-packsack-otimizacao-de-espaco)

# 🎯 Design Patterns em Python

> **Uma coleção completa e interativa de Design Patterns implementados em Python para aprendizado e demonstração**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg)]()

---

## 📋 Índice

- [🎯 Sobre o Projeto](#-sobre-o-projeto)
- [🏗️ Estrutura do Projeto](#️-estrutura-do-projeto)
- [🚀 Como Usar](#-como-usar)
- [📚 Padrões Implementados](#-padrões-implementados)
  - [🏭 Padrões Criacionais](#-padrões-criacionais)
  - [🏛️ Padrões Estruturais](#️-padrões-estruturais)
  - [🎭 Padrões Comportamentais](#-padrões-comportamentais)
- [💡 Exemplos Práticos](#-exemplos-práticos)
- [🔧 Tecnologias](#-tecnologias)
- [📖 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

---

## 🎯 Sobre o Projeto

Este projeto é uma **coleção completa e educativa** de Design Patterns implementados em Python. Cada padrão é demonstrado através de exemplos práticos e contextos reais, facilitando o aprendizado e compreensão dos conceitos fundamentais de design de software.

### ✨ Características

- **📖 Educativo**: Cada padrão inclui explicações detalhadas e exemplos práticos
- **🎯 Contextualizado**: Implementações baseadas em cenários reais de e-commerce
- **🔍 Comparativo**: Demonstração das diferenças entre código com e sem padrões
- **🚀 Executável**: Todos os exemplos podem ser executados e testados
- **📝 Documentado**: Código bem comentado e documentado

---

## 🏗️ Estrutura do Projeto

```
DesignPatternsPy/
├── 📁 creational/          # Padrões Criacionais
│   ├── 🏭 abstract_factory/
│   ├── 🔨 builder/
│   ├── 🏭 factory_method/
│   ├── 🧬 prototype/
│   └── 🎯 singleton/
├── 📁 structural/          # Padrões Estruturais
│   ├── 🔌 adapter/
│   ├── 🌉 bridge/
│   ├── 🌳 composite/
│   ├── 🎨 decorator/
│   ├── 🏢 facade/
│   ├── 🪶 flyweight/
│   └── 🎭 proxy/
├── 📁 behavioral/          # Padrões Comportamentais
│   ├── ⛓️ chain/
│   ├── 📋 command/
│   ├── 🔄 iterator/
│   ├── 🤝 mediator/
│   ├── 💾 memento/
│   ├── 👀 observer/
│   ├── 🔄 state/
│   ├── 🎯 strategy/
│   ├── 📄 template/
│   └── 🚶 visitor/
├── 📁 standard_Code/       # Código sem padrões (comparação)
└── 📄 README.md
```

---

## 🚀 Como Usar

### 📋 Pré-requisitos

- Python 3.8 ou superior
- Conhecimento básico de programação orientada a objetos

### 🔧 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/MuketaUeda/DesignPatternsPy.git
   cd DesignPatternsPy
   ```

2. **Navegue para um padrão específico**:
   ```bash
   cd creational/singleton
   ```

3. **Execute o exemplo**:
   ```bash
   python main.py
   ```

### 🎯 Exemplo de Uso

```bash
# Executar exemplo do Singleton
cd creational/singleton
python main.py

# Executar exemplo do Observer
cd ../behavioral/observer
python main.py

# Executar exemplo do Adapter
cd ../../structural/adapter
python main.py
```

---

## 📚 Padrões Implementados

### 🏭 Padrões Criacionais

Padrões que lidam com a criação de objetos, tornando o sistema mais flexível e reutilizável.

| Padrão | Status | Descrição | Exemplo |
|--------|--------|-----------|---------|
| **Singleton** | ✅ | Garante uma única instância de uma classe | Serviços de pagamento, notificação |
| **Factory Method** | 🔄 | Delega a criação de objetos para subclasses | Criação de produtos |
| **Abstract Factory** | 🔄 | Cria famílias de objetos relacionados | UI components |
| **Builder** | 🔄 | Constrói objetos complexos passo a passo | Configuração de pedidos |
| **Prototype** | 🔄 | Cria novos objetos clonando um protótipo | Templates de produtos |

### 🏛️ Padrões Estruturais

Padrões que lidam com a composição de classes e objetos, formando estruturas maiores.

| Padrão | Status | Descrição | Exemplo |
|--------|--------|-----------|---------|
| **Adapter** | 🔄 | Permite que interfaces incompatíveis trabalhem juntas | Integração de APIs |
| **Bridge** | 🔄 | Separa abstração da implementação | Plataformas de pagamento |
| **Composite** | 🔄 | Compõe objetos em estruturas de árvore | Categorias de produtos |
| **Decorator** | 🔄 | Adiciona responsabilidades dinamicamente | Descontos e taxas |
| **Facade** | 🔄 | Fornece uma interface simplificada | Sistema de checkout |
| **Flyweight** | 🔄 | Compartilha objetos para reduzir memória | Cache de produtos |
| **Proxy** | 🔄 | Controla acesso a outro objeto | Cache de imagens |

### 🎭 Padrões Comportamentais

Padrões que lidam com a comunicação entre objetos e a distribuição de responsabilidades.

| Padrão | Status | Descrição | Exemplo |
|--------|--------|-----------|---------|
| **Chain of Responsibility** | 🔄 | Passa requisições através de uma cadeia | Validação de pedidos |
| **Command** | 🔄 | Encapsula uma requisição como objeto | Histórico de ações |
| **Iterator** | 🔄 | Acessa elementos de uma coleção | Navegação de produtos |
| **Mediator** | 🔄 | Centraliza comunicação entre objetos | Sistema de chat |
| **Memento** | 🔄 | Captura e restaura estado interno | Histórico de carrinho |
| **Observer** | 🔄 | Notifica mudanças para dependentes | Notificações de estoque |
| **State** | 🔄 | Permite que objeto altere comportamento | Status de pedido |
| **Strategy** | 🔄 | Define família de algoritmos | Métodos de pagamento |
| **Template Method** | 🔄 | Define esqueleto de algoritmo | Processamento de pedido |
| **Visitor** | 🔄 | Adiciona operações sem modificar classes | Relatórios de vendas |

---

## 🔧 Tecnologias

- **🐍 Python 3.8+**: Linguagem principal
- **📦 Módulos padrão**: Sem dependências externas
- **🎯 POO**: Programação Orientada a Objetos
- **📝 Type Hints**: Tipagem opcional para clareza

---

## 📖 Contribuindo

Contribuições são bem-vindas! Aqui estão algumas formas de contribuir:

### 🐛 Reportando Bugs

1. Abra uma [Issue](../../issues)
2. Descreva o problema detalhadamente
3. Inclua passos para reproduzir
4. Adicione informações do ambiente

### 💡 Sugerindo Melhorias

1. Abra uma [Issue](../../issues) com label "enhancement"
2. Descreva a funcionalidade desejada
3. Explique o benefício da mudança

### 🔧 Enviando Pull Requests

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### 📋 Diretrizes de Contribuição

- **Código limpo**: Siga PEP 8
- **Documentação**: Comente seu código
- **Testes**: Inclua exemplos executáveis
- **Padrões**: Mantenha consistência com os exemplos existentes

---

## 🎓 Aprendizado

### 📚 Recursos Recomendados

- **Livros**:
  - "Design Patterns" (Gang of Four)
  - "Head First Design Patterns"
  - "Python Design Patterns"


## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- **Gang of Four**: Pelo livro seminal sobre Design Patterns
- **Comunidade Python**: Pelo suporte e recursos

---

## 📞 Contato

- **GitHub**: [@MuketaUeda](https://github.com/MuketaUeda)
- **Email**: gt.rosati@gmail.com
- **LinkedIn**: [Gabriel Rosati](https://www.linkedin.com/in/gabriel-tb-rosati/)

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**

</div>
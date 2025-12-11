## 🌤️ Weather App

Aplicação completa para **consulta de clima em tempo real** utilizando a API pública **Open Meteo**. A arquitetura é dividida em dois serviços principais:

  * **Frontend** em Next.js
  * **Backend** em FastAPI

Ambos os serviços podem ser executados via **Docker** ou **Docker Compose**. O objetivo do projeto é demonstrar boas práticas de organização, comunicação entre serviços e integração com APIs externas.

-----

## Como Rodar o Projeto

Pré requisitos:

  * Docker
  * Docker Compose
  * Porta **3000** livre para o frontend
  * Porta **8000** livre para o backend

A execução via **Docker Compose** é o método principal e recomendado.

### Passo a passo

1.  Na raiz do projeto, execute o build:
    ```bash
    docker compose build
    ```
2.  Suba os containers:
    ```bash
    docker compose up
    ```
3.  Acesse o frontend em:
    ```
    http://localhost:3000
    ```
4.  A API estará disponível em:
    ```
    http://localhost:8000
    ```

-----

## Decisões de Arquitetura e Design

### Separação de Frontend e Backend

O sistema segue uma arquitetura de **dois serviços isolados**.

  * O **backend** centraliza regras de negócio e chamadas externas.
  * O **frontend** funciona como cliente leve consumindo a API interna.

Essa separação simplifica **manutenção**, **escalabilidade** e **deploy**.

### Comunicação entre Containers

O Docker Compose cria a network chamada `weather-net`. Dentro desse ambiente, os containers se comunicam usando seus **nomes**.

Exemplo:
Frontend acessa o backend pela URL:

```
http://backend:8000
```

Isso evita dependências com `localhost` ou IPs fixos.

### Uso de FastAPI

FastAPI foi escolhido por oferecer:

  * Tipagem nativa com **Python**
  * **Alto desempenho**
  * Suporte assíncrono ideal para chamadas externas
  * Documentação de API automática

No backend, responsabilidades foram separadas assim:

  * Um módulo `services` gerencia requisições externas.
  * O arquivo principal concentra rotas e validação.

### Uso de Next.js no Frontend

Next.js foi escolhido por fornecer:

  * **Renderização otimizada**
  * Integração com **Typescript**
  * Componentização reativa

A página principal é um **Client Component** para permitir estados dinâmicos com `useState`.

### CORS e Segurança

O backend habilita **CORS** apenas para:

  * `http://localhost:3000`
  * `http://127.0.0.1:3000`

Isso garante controle sobre quem pode consumir a API.

### Design da Interface

Algumas decisões foram tomadas para tornar a experiência **leve e clara**:

  * Gradiente azul remetendo ao clima
  * Formulário centralizado
  * Feedback visual de carregamento
  * Cartão translúcido estilo **glassmorphism**
  * Ícones e texturas que reforçam a condição do clima

-----

## Sugestões de Melhorias Futuras

### Melhorias de UX e UI

  * Renderizar imagens baseadas no clima atual
  * Alterar paleta de cores dependendo da condição climática
  * Exibir uma barra de previsão para as próximas horas
  * Incluir mensagens adaptadas ao clima
  * Adicionar suporte simples à internacionalização

### Melhorias Técnicas

  * Criar camada de **cache** para reduzir chamadas à Open Meteo
  * Adicionar testes unitários com **pytest**
  * Melhorar a validação das entradas
  * Criar tipagem automática com **zod** no frontend
  * Separar o serviço de coordenadas em um módulo dedicado


### Possíveis Extensões

  * Adicionar mapa interativo com **Leaflet** ou **Mapbox**
  * Criar sistema de favoritos persistido no `localStorage`
  * Disponibilizar histórico de buscas
  * Adicionar endpoint para previsão semanal

<h1 align="left">🌤️ Weather App</h1>
<p align="left"> Aplicação completa para consulta de clima em tempo real utilizando a API pública Open Meteo. A arquitetura é dividida em dois serviços principais:<br> Frontend em Next.js<br> Backend em FastAPI<br><br> Ambos os serviços podem ser executados via Docker ou Docker Compose. O objetivo do projeto é demonstrar boas práticas de organização, comunicação entre serviços e integração com APIs externas. </p>
<h2 align="left">Como Rodar o Projeto</h2>
<p align="left"> Pré requisitos:<br> Docker<br> Docker Compose<br> Porta 3000 livre para o frontend<br> Porta 8000 livre para o backend<br><br>

Execução via Docker Compose é o método principal e recomendado.

</p>
<h3 align="left">Passo a passo</h3> <p align="left"> 1. Na raiz do projeto, execute o build<br> docker compose build<br><br>

Suba os containers<br>
docker compose up<br><br>

Acesse o frontend<br>
http://localhost:3000
<br><br>

A API estará disponível em<br>
http://localhost:8000

</p>
<h2 align="left">Decisões de Arquitetura e Design</h2>
<h3 align="left">Separação de Frontend e Backend</h3> <p align="left"> O sistema segue uma arquitetura de dois serviços isolados.<br> O backend centraliza regras de negócio e chamadas externas.<br> O frontend funciona como cliente leve consumindo a API interna.<br> Essa separação simplifica manutenção, escalabilidade e deploy. </p>
<h3 align="left">Comunicação entre Containers</h3> <p align="left"> O Docker Compose cria a network chamada weather-net.<br> Dentro desse ambiente, os containers se comunicam usando seus nomes.<br><br>

Exemplo:<br>
Frontend acessa o backend pela URL:<br>
http://backend:8000
<br><br>

Isso evita dependências com localhost ou IPs fixos.

</p>
<h3 align="left">Uso de FastAPI</h3> <p align="left"> FastAPI foi escolhido por oferecer:<br> Tipagem nativa com Python<br> Alto desempenho<br> Suporte assíncrono ideal para chamadas externas<br> Documentação de API automática<br><br>

No backend, responsabilidades foram separadas assim:<br>
Um módulo services gerencia requisições externas.<br>
O arquivo principal concentra rotas e validação.

</p>
<h3 align="left">Uso de Next.js no Frontend</h3> <p align="left"> Next.js foi escolhido por fornecer:<br> Renderização otimizada<br> Integração com Typescript<br> Componentização reativa<br><br>

A página principal é um Client Component para permitir estados dinâmicos com useState.

</p>
<h3 align="left">CORS e Segurança</h3> <p align="left"> O backend habilita CORS apenas para:<br> http://localhost:3000<br> http://127.0.0.1:3000<br><br>

Isso garante controle sobre quem pode consumir a API.

</p>
<h3 align="left">Design da Interface</h3> <p align="left"> Algumas decisões foram tomadas para tornar a experiência leve e clara:<br> Gradiente azul remetendo ao clima<br> Formulário centralizado<br> Feedback visual de carregamento<br> Cartão translúcido estilo glassmorphism<br> Ícones e texturas que reforçam a condição do clima </p>
<h2 align="left">Sugestões de Melhorias Futuras</h2>
<h3 align="left">Melhorias de UX e UI</h3> <p align="left"> Renderizar imagens baseadas no clima atual<br> Alterar paleta de cores dependendo da condição climática<br> Exibir uma barra de previsão para as próximas horas<br> Incluir mensagens adaptadas ao clima<br> Adicionar suporte simples à internacionalização </p>
<h3 align="left">Melhorias Técnicas</h3> <p align="left"> Criar camada de cache para reduzir chamadas à Open Meteo<br> Adicionar testes unitários com pytest<br> Melhorar a validação das entradas<br> Criar tipagem automática com zod no frontend<br> Separar o serviço de coordenadas em um módulo dedicado </p>
<h3 align="left">Possíveis Extensões</h3> <p align="left"> Adicionar mapa interativo com Leaflet ou Mapbox<br> Criar sistema de favoritos persistido no localStorage<br> Disponibilizar histórico de buscas<br> Adicionar endpoint para previsão semanal </p>
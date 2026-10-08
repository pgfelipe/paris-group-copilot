# Arquitetura — Paris Group Copilot

Cada componente da stack é justificado por três critérios de venture studio:

1. **Velocidade de MVP:** chegar mais rápido à primeira versão testável da hipótese.
2. **Reutilização:** o que é feito aqui serve para o próximo MVP do studio.
3. **Manutenção simples:** o mesmo time cuida de vários produtos ao mesmo tempo, então cada um precisa dar pouco trabalho depois que sobe.

Referência de produto: [enquadramento.md](enquadramento.md).

## Visão geral

```
paris-group-copilot/
├── src/app/            Next.js (App Router): páginas /projeto e /hipotese
├── api/                FastAPI: contrato OpenAPI de Projeto e Hipótese
├── docker-compose.yml  PostgreSQL + API com um único comando
└── docs/               Enquadramento e arquitetura
```

## Componentes

### Next.js (em vez de Remix)

- **Velocidade de MVP:** cada pasta em `src/app/` vira uma rota. As páginas `/projeto` e `/hipotese` nasceram só com pastas e arquivos, sem configurar roteamento.
- **Reutilização:** é o framework do chassi do studio (`pg-starter`) e do design system compartilhado (PageShell). Um componente feito para o Copilot pode servir para o próximo MVP sem adaptação.
- **Manutenção:** os Server Components leem dados no servidor, no mesmo projeto da interface. Não existe um terceiro serviço só para montar telas.

### FastAPI (em vez de Express)

- **Velocidade de MVP:** os schemas Pydantic (`ProjetoIn`, `HipoteseIn`) validam a entrada e geram o contrato OpenAPI em `/docs` automaticamente. O Express precisaria de bibliotecas extras e de documentação escrita à mão para o mesmo resultado.
- **Reutilização:** o padrão `schemas.py` + `models.py` + rotas se copia para qualquer MVP que precise de uma API com contrato. O Python também dá acesso direto ao ecossistema de IA e dados, útil quando o Copilot passar a consultar e resumir fontes de conhecimento.
- **Manutenção:** valores inválidos (ex.: `status` fora de `discovery | mvp | validado | encerrado`) são rejeitados na borda com erro `422`, antes de chegar ao banco. Menos dado inconsistente para investigar depois.

### PostgreSQL (em vez de SQLite)

- **Velocidade de MVP:** o MVP já nasce com o banco de produção. Quando a hipótese valida, não há migração de SQLite para Postgres. E subir o banco custa um único `docker compose up`.
- **Reutilização:** todo MVP do studio usa Postgres, então ao mudar de projeto o contexto do banco de dados é o mesmo.
- **Manutenção:** o Postgres persiste os dados independentemente de o disco do container da aplicação ser limpo a cada deploy.

### Docker Compose (em vez de instalar tudo na máquina)

- **Velocidade de MVP:** `docker compose up` sobe o banco e a API juntos, já esperando o Postgres ficar saudável antes de iniciar a API.
- **Reutilização:** o mesmo `docker-compose.yml` serve de molde para o próximo MVP. Quem entra no projeto não precisa instalar Python ou Postgres para rodar.
- **Manutenção:** as versões ficam fixas no arquivo (`postgres:17`, `python:3.12`). Exemplo real: a máquina de desenvolvimento tem Python 3.9, e a API roda em 3.12 sem conflito.

### Monorepo (`api/` no mesmo repositório)

- **Velocidade de MVP:** uma mudança no contrato (ex.: novo campo em Hipótese) altera API e interface no mesmo commit e no mesmo PR.
- **Reutilização:** o repositório inteiro (interface, API, compose e docs) pode ser clonado como ponto de partida do próximo MVP.
- **Manutenção:** um só lugar para documentação, CI e histórico. O enquadramento e o código evoluem juntos.

## Comparação com o padrão Full-TS da Paris Group

Este exercício usa FastAPI + OpenAPI. O padrão da frota Paris Group é o oposto: TypeScript de ponta a ponta (Next.js + tRPC + Drizzle). A comparação:

| Ponto | Esta stack (Next.js + FastAPI) | Full-TS (Next.js + tRPC + Drizzle) |
|---|---|---|
| Linguagens | Duas (TypeScript e Python) | Uma (TypeScript) |
| Contrato front ↔ back | OpenAPI gerado pelo FastAPI. O front precisa gerar ou escrever tipos a partir dele | Tipos compartilhados direto pelo tRPC, sem geração de código |
| Mudança de campo | Altera o schema Pydantic e depois os tipos do front. Se esquecer o segundo passo, quebra em runtime | Altera o schema Drizzle e o `pnpm typecheck` aponta o erro na tela antes do deploy |
| Agentes de IA | Mais chance de errar o formato do payload entre as duas camadas | O tipo serve de trilho do banco até a interface |
| Ecossistema de IA e dados | Acesso nativo às bibliotecas Python | Chamadas de IA via LiteLLM Gateway, sem depender de Python |

**Conclusão:** para um studio que cria vários MVPs com o mesmo time e com agentes de IA escrevendo código, o Full-TS vence em reutilização e manutenção, porque elimina a divergência silenciosa de contrato. O FastAPI se justifica quando o produto depende de processamento que só existe bem servido em Python (ex.: modelos de ML próprios, pipelines de dados pesados). Esse não é o caso do MVP do Copilot, que é uma ferramenta de consulta. Por isso, numa versão para a frota, a API migraria para tRPC + Drizzle.

## Fora do MVP (decisões conscientes)

- **Migrations versionadas (Alembic):** as tabelas são criadas no boot da API. Suficiente para 1 PM durante 8 semanas, e evita configurar ferramenta antes de validar a hipótese.
- **Autenticação e controle de acesso:** fora de escopo, conforme o enquadramento (apenas 1 PM no MVP).

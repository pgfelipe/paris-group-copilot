# Handoff — Sprint 1 · Paris Group Copilot

> Atualização assíncrona para stakeholders. Demo em vídeo: **[Loom — Sprint 1 (3 min)](https://www.loom.com/share/8b98cc56f2d844a28c59df04eef44d65)**

## Contexto

**O que o produto resolve:** a PM de um venture studio perde 10 horas por semana procurando decisões e aprendizados de MVPs anteriores em fontes diferentes. O Paris Group Copilot consulta esse conhecimento por ela. Hipótese: reduzir de 10 para 1 hora por semana, validada se o tempo ficar em até 1 hora em 7 de 8 semanas de teste com 1 PM. Detalhes em [`docs/enquadramento.md`](../enquadramento.md).

**O que foi entregue nesta sprint:**
- Aplicação Next.js com as páginas **Projeto** (`/projeto`) e **Hipótese** (`/hipotese`).
- API com o contrato de Projeto e Hipótese (`GET/POST /projetos` e `/hipoteses`) sobre PostgreSQL, subindo com um comando (`docker compose up`).
- Governança: repositório travado em modo PR e template de PR padronizado ([PR #1](https://github.com/pgfelipe/paris-group-copilot/pull/1)).
- Rede de segurança: `pnpm typecheck` e `pnpm test` com o primeiro teste automatizado ([PR #2](https://github.com/pgfelipe/paris-group-copilot/pull/2)).
- Documentação de produto e arquitetura em [`docs/`](../).

## Decisões técnicas

| Decisão | Justificativa |
|---|---|
| **PostgreSQL desde o MVP** (e não SQLite) | Sem migração de banco quando o produto crescer: o MVP já roda no banco de produção, o mesmo de todos os produtos do studio. Menos risco e menos custo na escala. |
| **Full-TS como padrão** (FastAPI como exceção temporária) | A dívida técnica foi identificada e tem data para sair: a API em FastAPI foi uma exceção consciente, e a migração para o padrão (tRPC + Drizzle) está planejada antes de novas features dependerem dela. |
| **Governança por PR** | Nenhum código chega à produção sem revisão e sem testes automáticos. Cada mudança é rastreável até a tarefa que a originou. |

## Bloqueios ativos

| Bloqueio | Impacto | Owner | Prazo |
|---|---|---|---|
| Fontes de conhecimento do MVP indefinidas | O mecanismo da hipótese depende delas; sem isso não há como construir as integrações | Felipe (depende da PM) | 15/10 |
| API fora do padrão Full-TS | Novas features ficam travadas até a migração, para não espalhar a dívida | Felipe | 19/10 |

## Próximos passos

| Ordem | Passo | Owner | Prazo |
|---|---|---|---|
| 1º | Merge dos PRs #1 e #2 | Felipe | 13/10 |
| 2º | Definir as fontes do MVP com a PM | Felipe (depende da PM) | 15/10 |
| 3º | Migrar a API para tRPC + Drizzle, protegida por `typecheck` e `test` | Felipe | 19/10 |
| 4º | Teste E2E da rota `/projeto` | Felipe | após a migração |

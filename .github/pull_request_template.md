## Contexto

<!-- O que mudou no código e por quê. Explique a motivação técnica ou de produto, não só a lista de arquivos. -->

## Evidência

<!-- Prova de que funciona. Marque cada item e cole a saída relevante abaixo. -->

- [ ] `pnpm typecheck` com 0 erros
- [ ] Testes verdes (`pnpm test`)
- [ ] Demo em vídeo (Loom, 2–3 min), quando houver mudança visual: <!-- link -->

## Rastreabilidade

<!-- Issue do GitHub (ex.: Closes #12) ou TaskNote (ex.: FEAT-001) que originou este PR. -->

## Integridade de Contratos

<!-- Confirme o alinhamento com o chassi Full-TS da Paris Group. Se algum item não se aplicar, explique o motivo. -->

- [ ] Contratos front ↔ back via tRPC, sem cliente OpenAPI gerado à mão
- [ ] Nenhum backend ou serviço desacoplado novo fora do chassi
- [ ] Schema de dados declarado em Drizzle (PostgreSQL)

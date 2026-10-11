# Fontes e acesso: decisões de coleta

[Voltar ao início](../README.md) · [Pré-conferência automática](access-preflight.json)

**Conferência em 11/10/2026.** O relatório técnico registra o agente usado, os caminhos examinados, a data e o hash de robots.txt. Consultas a essas regras não baixam o corpus. Caminhos terminados em `contrato.pdf` no cadastro são sondas de regra; sua existência não foi afirmada nem testada.

| Candidato | Evidência inicial | Decisão de lote |
|---|---|---|
| Itaú | Os [termos do site](https://www.itau.com.br/termos-de-uso) vedam sistemas automatizados para consultas ou acessos massificados sem autorização. O [robots.txt](https://www.itau.com.br/robots.txt) também restringe PDFs para agentes gerais. | Suspender coleta automatizada em lote até resolver a condição de uso; não promover a aprovado |
| Banco do Brasil | O [robots.txt](https://www.bb.com.br/robots.txt) restringe `/docs/pub/`, `/docs/portal/` e `/portalbb/`. Páginas fora desses caminhos exigem exame próprio de termos. | Avaliar fontes compatíveis; permissão pendente |
| Inter | Central pública `ajuda.inter.co`, política de privacidade, segurança e regras de acesso examinadas. | Liberação operacional assistida somente dos endereços cadastrados; 12 documentos coletados; sem licença de redistribuição |
| Bradesco | Política institucional e termos do internet banking examinados, com distinção entre páginas públicas e serviços autenticados. | Liberação operacional assistida de páginas públicas cadastradas; 5 documentos coletados; 4 acessos bloqueados ou redirecionados excluídos |
| C6 | Os [termos de uso](https://www.c6bank.com.br/termos-de-uso/) restringem reprodução e uso sem autorização, nas cláusulas 2.1.10 e 16.1. | Coleta com cópias suspensa |
| Caixa | [Termos de uso](https://www.caixa.gov.br/termos-de-uso/Paginas/default.aspx) localizados; a leitura integral ficou bloqueada por redirecionamento nesta conferência. | Alternativa em análise |
| Santander | [Página institucional de política e termos](https://www.santander.com.br/institucional/relacionamento/politica-de-privacidade) examinada; a seção de propriedade intelectual restringe cópias e reproduções sem consentimento prévio. | Coleta com cópias suspensa até resolver a restrição |
| Nubank | [Contratos públicos](https://nubank.com.br/contratos) candidatos; definir escopo institucional e modalidade da conta. | Alternativa condicionada ao escopo e às condições de coleta |

A conferência inicial não aprovou fontes. A revisão complementar de 11/10/2026 liberou operacionalmente um lote limitado do Inter e do Bradesco, identificado nos cadastros, sem atribuir autorização expressa aos bancos. A revisão assistida não encontrou restrição específica aplicável a esses endereços e não produz licença de uso ou redistribuição. O [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) esclarece que robots.txt não substitui autorização de acesso. Direitos de redistribuição exigem decisão separada.

O cadastro de candidatos serve à pré-conferência. A primeira coleta usou os [cadastros completos](../configs/sources-20261011.json) com termos, decisão, evidência e origem da revisão. [Veja o relatório](execucao-20261011.md). Uma falha de rede na conferência fica pendente; não prova que o banco proíbe o acesso.

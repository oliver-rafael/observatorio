# ExtractProposicoes: Coletando Informações sobre Proposições Legislativas

!Legislative Process

## Visão Geral

O **ExtractProposicoes** é um projeto Python empolgante que permite a você explorar e coletar informações sobre proposições legislativas. Se você é um entusiasta da política, um estudante de direito ou apenas alguém curioso, este é o lugar certo para começar!

## Sobre o Observatório Social do Brasil (OSB)

O **Observatório Social do Brasil (OSB)** é uma instituição não governamental, sem fins lucrativos, que dissemina uma metodologia padronizada para a criação e atuação de uma rede de organizações democráticas e apartidárias do terceiro setor. O OSB promove a capacitação e oferece suporte técnico aos **Observatórios Sociais (OS)** em todo o país. Além disso, estabelece parcerias estaduais e nacionais para o melhor desempenho das ações locais.

O OSB contribui para a melhoria da gestão pública por meio do **controle social**. Seus voluntários estão engajados na causa da justiça social, monitorando e fiscalizando as ações dos gestores públicos. O objetivo é garantir a **transparência**, a **eficiência** e a **responsabilidade** na administração pública.

## Como Funciona o ExtractProposicoes?

1. **Consulta Personalizada**: Você pode especificar o tipo de proposição (por exemplo, PL, PEC, PR, etc.) e o intervalo de datas de interesse. O ExtractProposicoes irá buscar as informações relevantes para você.
2. **Extração de Dados**: O programa faz uma solicitação HTTP para um site específico que contém dados sobre proposições. Ele analisa o HTML da página e extrai detalhes como o número da proposição, data de apresentação, autor e muito mais.
3. **Organização Inteligente**: Os dados coletados são organizados em uma estrutura de dados fácil de usar. Você terá acesso a informações como o tipo de proposição, seu número, a situação atual, o assunto e até mesmo o texto completo da proposição.

## Por que Usar o ExtractProposicoes?

- **Transparência**: Entenda o que está acontecendo no cenário legislativo. Fique por dentro das propostas e decisões que afetam a sociedade.
- **Engajamento**: Compartilhe os dados com seus amigos, colegas e redes sociais. Mostre que você está antenado nas questões políticas.
- **Aprendizado**: Aprenda sobre o processo legislativo e como as propostas são apresentadas, debatidas e votadas.

# Como Começar

1. **Instalação**:
    - Certifique-se de ter o Python instalado em sua máquina.
    - Execute `pip install requests beautifulsoup4 pandas` para instalar as bibliotecas necessárias.

2. **Configuração**:
    - Abra o arquivo `ExtractProposicoes.py`.
    - Defina os parâmetros: `tipo_proposicao`, `data_inicio` e `data_final`.

3. **Execução**:
    - Execute o programa: `python ExtractProposicoes.py`.
    - Veja os resultados organizados no console ou salve-os em um arquivo.

## Contribua!

Se você é um desenvolvedor apaixonado por política ou apenas quer se envolver em um projeto interessante, junte-se a nós! Contribua com melhorias, adicione novos recursos e ajude a tornar o **ExtractProposicoes** ainda mais incrível.

## Saiba Mais

- Site Oficial do Observatório Social do Brasil
- O que é um Observatório Social do Brasil (OSB)?
- Como Funciona o OSB?

---

**Nota**: Este projeto é puramente educativo e não tem nenhuma afiliação oficial com órgãos legislativos. Use-o com responsabilidade e curiosidade saudável! 🇧🇷📜🤝

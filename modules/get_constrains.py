#!/usr/bin/env python
# -*- coding: utf-8 -*-
def getConstrains(tab):
    constrains = [['A.1', 3, 0, 9, "População total e sua distribuição proporcional" ],
                    ['A.2', 3, 0, 6, "Homens por 100 mulheres" ],
                    ['A.3', 3, 0, 4, u"Taxa de crescimento da populacão(%)"],
                    ['A.4', 3, 0, 6, u"Grau de Urbanização(%)"],
                    ['A.13', 3, 0, 8, u"Proporção (%) de menores de 5 anos de idade na população"],
                    ['A.15', 3, 0, 8, "Índice de envelhecimento"],
                    ['A.17', 3, 0, 8, "Razão entre nascidos vivos informados e estimados"],
                    ['A.7', 3, 0, 9, "Taxa de natalidade"],
                    ['A.5', 3, 0, 8, 'Taxa de fecundidade total'],
                    ['A.18', 3, 0, 8, u"Razão entre óbitos informados e estimados" ],
                    ['A.8', 3, 0, 5, u"Mortalidade proporcional (%) por idade"],
                    ['A.9', 3, 0, 5, u"Mortalidade proporcional (%) por idade, em menores de 1 ano de idade"],
                    ['A.10', 3, 0, 10, u" Taxa bruta e padronizada de mortalidade"],
                    ['A.11', 3, 0, 6, u"Esperança de vida ao nascer"],
                    ['A.12', 3, 0, 6, u"Esperança de vida aos 60 anos"],
                    ['B.1', 3, 0, 9, u"Taxa de analfabetismo(Homens e Mulheres)"],
                    ['B.3', 3, 0, 8, u"Escolaridade (%) da população de 18 a 24 anos"],
                    ['B.8', 4, 0, 13, u"Renda média domiciliar per capita"],
                    ['B.9', 4, 0, 7, u"Índice de Gini da renda domiciliar per capita"],
                    ['B.4', 3, 0, 5, u"Razão de renda"],
                    ['B.5.1', 3, 0, 11, u"Proporção (%) de pessoas de baixa renda"],
                    ['B.5.2', 3, 0, 11, u"Proporção (%) de crianças em situação domiciliar de baixa renda, por ano, segundo região e renda média domiciliar per capita"],
                    ['B.6', 4, 0, 9, u"Taxa de desemprego"],
                    ['B.7', 4, 0, 9, u"Taxa de trabalho infantil"],
                    ['B.10', 3, 0, 8, u"Proporção (%) de idosos residentes em domicílios na condição de outro parente"],
                    ['C.1.1', 3, 0, 6, u"Taxa de mortalidade neonatal precoce"],
                    ['C.1.2', 3, 0, 6, u"Taxa de mortalidade neonatal tardia"],
                    ['C1.4', 3, 0, 5, u"Taxa de mortalidade neonatal"],
                    ['C1.3', 3, 0, 6, u"Taxa de mortalidade pós-neonatal"],
                    ['C.2', 3, 0, 5, u"Taxa de mortalidade perinatal"],
                    ['C16', 3, 0, 7, u"Taxa de mortalidade na infância"],
                    ['C.3', 3, 0, 13, u"Razão de mortalidade materna"],
                    ['C.18', 3 ,0, 5, u"Distribuição (%) de óbitos maternos"],
                    ['C.6', 3, 0, 5, u"Proporção (%) de óbitos por doença diarreica aguda em menores de 5 anos de idade"],
                    ['C.7', 3, 0, 5, u"Proporção (%) de óbitos por infecção respiratória aguda em menores de 5 anos de idade"],
                    ['C.8', 3, 0, 7, u"Taxa de mortalidade específica por doenças do aparelho circulatório"],
                    ['C.11', 3, 0, 11, u"Taxa de mortalidade específica por acidentes de trabalho em Segurados da Previdência Social"],
                    ['C.12', 3, 0, 7, u"Taxa de mortalidade específica por diabete melito"],
                    ['C.15', 3, 0, 6, u"Taxa de mortalidade específica por afecções originadas no período perinatal"],
                    ['C.17', 3, 0, 7, u"Taxa de mortalidade específica por doenças transmissíveis"],
                    ['D.1.1', 3, 0, 9, u"Incidência de sarampo"],
                    ['D.1.2', 3, 0, 7, u"Incidência de difteria"],
                    ['D.1.3', 3, 0, 8, u"Incidência de coqueluche"],
                    ['D.1.4', 3, 0, 6, u"Incidência de tétano neonatal"],
                    ['D.1.5', 3, 0, 9, u"Incidência de tétano (exceto o neonatal)"],
                    ['D.1.6', 3, 0, 7, u"Incidência de febre amarela"],
                    ['D.1.7', 3, 0, 7, u"Incidência de raiva humana"],
                    ['D.1.8', 3, 0, 10, u"Incidência de hepatite B"],
                    ['D.1.14', 3, 0, 9, u"Incidência de hepatite C"],
                    ['D.1.9', 3, 0, 8, u"Incidência de cólera"],
                    ['D.1.10', 3, 0, 8, u"Incidência de febre hemorrágica da dengue"],
                    ['D.1.11', 3, 0, 7, u"Incidência de sífilis congênita"],
                    ['D.1.12', 3, 0, 8, u"Incidência de rubéola"],
                    ['D.1.13', 3, 0, 7, u"Incidência da síndrome da rubéola congênita"],
                    ['D.1.15', 3, 0, 9, u"Incidência de doença meningocócia"],
                    ['D.1.16', 3, 0, 6, u"Incidência de meningite"],
                    ['D.1.17', 3, 0, 6, u"Incidência de leptospirose"],
                    ['D.2.1', 3, 0, 13, u"Taxa de incidência de aids"],
                    ['D.2.2', 3, 0, 11, u"Taxa de incidência de tuberculose(casos por 100.000 habitantes)"],
                    ['D.2.3', 3, 0, 9, u"Taxa de incidência de dengue(casos por 100.000 habitantes)"],
                    ['D.2.4', 3, 0, 9, u"Taxa de incidência de leishmaniose tegumentar americana(casos por 100.000 habitantes)"],
                    ['D.2.5', 3, 0, 10, u"Taxa de incidência de leishmaniose visceral(casos por 100.000 habitantes)"],
                    ['D.2.6', 3, 0, 11, u"Taxa de incidência de hanseníaseTaxa de incidência de hanseníase(casos por 100.000 habitantes)"],
                    ['D.4', 3, 0, 12, u"Índice parasitário anual (IPA) de malária(exames positivos por 1.000 habitantes)"],
                    ['D.5', 3, 0, 5, u"Taxa de incidência de neoplasias malignas por 100.000 habitantes"],
                    ['D.6', 3, 0, 11, u"Taxa de incidência de acidentes e doenças do trabalho em segurados da Previdência Social(casos por 10.000 trabalhadores com cobertura contra incapacidade laborativa decorrente de riscos  do trabalho)"],
                    ['D.9', 3, 0, 7, u"Prevalência de hanseníase(casos existentes no registro ativo por 10.000 habitantes)"],
                    ['D.23', 3, 0, 5, u"Proporção (%) de internações hospitalares (SUS) por afecções originadas no período perinatal"],
                    ['D.22', 3, 0, 7, u"Prevalência de pacientes em diálise (SUS) ( pacientes por 100.000 habitantes)"],
                    ['E.1', 3, 0, 5, u"Número de profissionais de saúde por habitante"],
                    ['E.15', 3, 0, 6, u"Número de concluintes de cursos de graduação em saúde"],
                    ['E.16', 3, 0, 7, u"Distribuição (%) de postos de trabalho de nível superior em estabelecimentos de saúde"],
                    ['E.17', 3, 0, 5, u"Número de postos de trabalho de enfermagem por 100 leitos hospitalares"],
                    ['E.2', 3, 0, 2, u"Número de leitos hospitalares por 1.000 habitantes"],
                    ['E.3', 3, 0, 10, u"Número de leitos hospitalares por 1.000 habitantes"],
                    ['E.22', 3, 0, 6, u"Distribuição (%) de leitos hospitalares, por ano e vinculação ao SUS"],
                    ['E.5', 3, 0, 5, u"Gasto per capita com consumo de bens e serviços de saúde"],
                    ['E.6.1', 3, 0, 10, u"Gasto com ações e serviços públicos de saúde como proporção do PIB(Valores dos gastos e do PIB em milhões de reais correntes)"],
                    ['E6.2', 3, 0, 9, u"Gasto per capita com ações e serviços públicos de saúde(Valores brutos dos gastos em milhões de reais correntes; valores per capita em reais correntes)"],
                    ['E.7', 3, 0, 7, u"Gasto federal com saúde como proporção do PIB(Valores em milhões de reais correntes)"],
                    ['E.8', 3, 0, 6, u"Gasto federal com saúde, despesas federais totais, despesas federais não financeiras, proporção (%) sobre despesas totais e proporção (%) sobre despesas não financeiras"],
                    ['E.9.1', 3, 0, 2, u"Despesa familiar autorreferida com saúde como proporção (%) da renda familiar, por classes de rendimento monetário e não monetário mensal familiar"],
                    ['E9.2', 3, 0, 4, u"Despesa familiar estimada com saúde como proporção da renda familiar"],
                    ['E.19', 3, 0, 2, u"Participação (%) das importações na oferta total por bens e serviços de saúde"],
                    ['E.11', 3, 0, 7, u"Valor médio pago por internação hospitalar no SUS (AIH)"],
                    ['E.20', 3, 0, 5, u"Gasto do Ministério da Saúde com atenção à saúde como proporção (%) do gasto total do Ministério da Saúde, por componente"],
                    ['E.21', 3, 0, 6, u"Gasto per capita do Ministério da Saúde com atenção à saúde(Valores em reais correntes)"],
                    ['E.13', 3, 0, 6, u"Gasto federal com saneamento como proporção (%) do PIB"],
                    ['E.14', 3, 0, 8, u"Gasto federal com saneamento, despesas federais totais e não-financeiras e proporção (%) do gasto federal com saneamento sobre as despesas totais e não financeiras"],
                    ['F.1', 3, 0, 6, u"Número de consultas médicas por habitante"],
                    ['F.20', 3, 0, 5, u"Proporção (%) da população que refere ter consultado médico nos últimos 12 meses"],
                    ['F.21.1', 3, 0, 6, u"Proporção (%) da população que refere ter realizado a última consulta odontológica a menos de 1 ano"],
                    ['F.21.2', 3, 0, 6, u"Proporção (%) da população que refere nunca ter realizado consulta odontológica"],
                    ['F.2', 3, 0, 6, u"Número de procedimentos diagnósticos por consulta médica (SUS)"],
                    ['F.22.1', 3, 0, 5, u"Proporção (%) da população feminina de 25 a 64 anos que refere ter utilizado o último exame preventivo do câncer do colo do útero em até 3 anos"],
                    ['F.22.2', 3, 0, 5, u"Proporção (%) da população feminina de 25 a 65 anos que refere nunca ter realizado exame preventivo do câncer do colo do útero"],
                    ['F.23.1', 3, 0, 6, u"Proporção da população feminina de 50 a 69 anos que refere ter realizado a última mamografia em até 2 anos"],
                    ['F.23.2', 3, 0, 5, u"Proporção (%) da população feminina de 50 a 69 anos que refere nunca ter realizado mamografia"],
                    ['F.3', 3, 0, 7, u"Número de internações hospitalares (SUS) por 100 habitantes"],
                    ['F.24', 3, 0, 4, u"Proporção da população que refere internação hospitalar nos últimos 12 meses"],
                    ['F.6', 3, 0, 4, u"Proporção (%) de nascidos vivos por número de consultas"],
                    ['F.7', 3, 0, 6, u"Proporção (%) de partos hospitalares"],
                    ['F.8', 3, 0, 6, u"Proporção (%) de partos cesáreos"],
                    ['F.13', 3, 0, 12, u"Proporção da população vacinada por faixa etária recomendada"],
                    ['F.14', 3, 0, 6, u"Percentual (%) da população feminina em uso de métodos anticonceptivos"],
                    ['F.15', 3, 0, 4, u"Proporção (%) da população coberta por planos de saúde – IBGE"],
                    ['F.16', 3, 0, 7, u"Proporção (%) da população coberta por planos privados de saúde – ANS"],
                    ['F.17', 3, 0, 7, u"Proporção (%) da população servida por rede de abastecimento de água"],
                    ['F.18', 3, 0, 7, u"Proporção (%) da população servida por esgotamento sanitário"],
                    ['F.19', 3, 0, 7, u"Proporção (%) da população servida por coleta de lixo"],
                    ['G.1', 3, 0, 8, u"Prevalência de diabete melito(percentual de adultos (35 anos ou mais de idade))"],
                    ['G.2', 3, 0, 8, u"Prevalência de hipertensão arterial( percentual de adultos (18 anos ou mais de idade) que referem diagnóstico médico prévio de hipertensão arterial)"],
                    ['G.4', 3, 0, 8, u"Prevalência de fumantes atuais por ano(percentual de adultos (18 anos ou mais de idade))"],
                    ['G.19', 3, 0, 7, u"Prevalência de ex-fumantes( percentual de adultos (18 anos ou mais de idade))"],
                    ['G.5', 3, 0, 8, u"Prevalência de consumo abusivo de bebidas alcoólicas(percentual de adultos (18 anos ou mais de idade))"],
                    ['G.6', 3, 0, 8, u"Prevalência de indivíduos dirigindo veículos motorizados após consumir bebida alcoólica( percentual de adultos (18 anos ou mais de idade))"],
                    ['G.7', 3, 0, 9, u"Prevalência de excesso de peso em adultos(percentual de adultos (18 anos ou mais de idade))"],
                    ['G.8', 3, 0, 6, u"Prevalência (%) de excesso de peso em crianças menores de 5 anos de idade"],
                    ['G.10', 3, 0, 6, u"Prevalência de déficit ponderal para a idade em crianças menores de 5 anos de idade"],
                    ['G.11', 3, 0, 6, u"Prevalência de déficit estatural para a idade em crianças menores de 5 anos de idade"],
                    ['G.12', 3, 0, 2, u"Participação diária per capita das calorias de frutas, verduras e legumes no total de calorias da dieta"],
                    ['G.13', 3, 0, 5, u"Prevalência de aleitamento materno"],
                    ['G.14', 3, 0, 4, u"Prevalência (%) de aleitamento materno exclusivo"],
                    ['G.15.1', 3, 0, 4, u"Proporção de nascidos vivos de mães adolescentes (10 a 19 anos e 10 a 14 anos)"],
                    ['G.15.2', 3, 0, 4, u"Proporção de nascidos vivos de mães tardias (40 anos ou mais)"],
                    ['G.16', 3, 0, 8, u"Proporção de nascidos vivos com baixo peso ao nascer"],
                    ['G.17', 3, 0, 5, u"Número médio de dentes cariados, perdidos e obturados aos 12 anos de idade"],
                    ['G.18', 3, 0, 4, u"Proporção (%) de crianças de 5 a 6 anos de idade com número de dentes decíduos cariados, extração indicada, perdidos devido à cárie e obturados (ceo-d) igual a 0"]]
    for element in constrains:
            if element[0] == (tab):
                return element[0], element[1], element[2], element[3], element[4]
    return 0, 0, 0, 0 , 0
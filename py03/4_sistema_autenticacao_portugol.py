# VERSÃO EM PORTUGOL - SISTEMA DE AUTENTICAÇÃO
#
# senha_correta <- "python123"
# tentativas <- 0
# acesso_liberado <- FALSO
#
# ENQUANTO tentativas < 3 FACA
#     LEIA senha
#
#     SE senha = senha_correta ENTAO
#         acesso_liberado <- VERDADEIRO
#         ESCREVA "Acesso liberado!"
#         PARE
#     SENAO
#         tentativas <- tentativas + 1
#         ESCREVA "Senha incorreta."
#     FIM_SE
# FIM_ENQUANTO
#
# SE acesso_liberado = FALSO ENTAO
#     ESCREVA "Acesso bloqueado após 3 tentativas."
# FIM_SE

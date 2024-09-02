def analisar_periodo(periodo_inicio, periodo_fim, ruido):
    resultado = []

    # Até 05/03/1997, ruído acima de 80 dB
    if periodo_inicio <= '1997-03-05':
        fim = min(periodo_fim, '1997-03-05')
        if ruido > 80:
            resultado.append(f"Período {periodo_inicio} a {fim} com ruído de {ruido} dB está enquadrado como especial (limite 80 dB).")
        else:
            resultado.append(f"Período {periodo_inicio} a {fim} com ruído de {ruido} dB não está enquadrado como especial (limite 80 dB).")
        periodo_inicio = '1997-03-06'

    # De 06/03/1997 a 18/11/2003, ruído acima de 90 dB
    if periodo_inicio <= '2003-11-18':
        fim = min(periodo_fim, '2003-11-18')
        if ruido > 90:
            resultado.append(f"Período {periodo_inicio} a {fim} com ruído de {ruido} dB está enquadrado como especial (limite 90 dB).")
        else:
            resultado.append(f"Período {periodo_inicio} a {fim} com ruído de {ruido} dB não está enquadrado como especial (limite 90 dB).")
        periodo_inicio = '2003-11-19'

    # A partir de 19/11/2003, ruído acima de 85 dB
    if periodo_inicio > '2003-11-18':
        if ruido > 85:
            resultado.append(f"Período {periodo_inicio} a {periodo_fim} com ruído de {ruido} dB está enquadrado como especial (limite 85 dB).")
        else:
            resultado.append(f"Período {periodo_inicio} a {periodo_fim} com ruído de {ruido} dB não está enquadrado como especial (limite 85 dB).")

    return "\n".join(resultado)

# Teste simples (você pode remover ou ajustar conforme necessário)
print(analisar_periodo('1992-01-01', '2018-08-05', 87))

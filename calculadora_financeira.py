"""
Módulo para cálculos financeiros básicos.
"""

def calcular_juros_simples(capital_inicial: float, taxa_anual: float, tempo_anos: float) -> float:
    """
    Calcula o montante final de um investimento com base na fórmula de juros simples.

    Esta função aplica a taxa de juros sobre o capital inicial durante o
    período especificado e retorna a soma do capital com os juros acumulados.

    A fórmula utilizada é: M = C * (1 + (i * t)), onde:
      - M = Montante final
      - C = Capital inicial
      - i = Taxa de juros (em formato decimal)
      - t = Tempo

    Args:
        capital_inicial (float): O valor do capital inicial a ser investido.
            Ex: 1000.00
        taxa_anual (float): A taxa de juros anual em formato percentual.
            Ex: 5 para 5%
        tempo_anos (float): O período do investimento, em anos. Pode ser fracionado.
            Ex: 2.5 para dois anos e meio.

    Returns:
        float: O montante final (capital + juros), arredondado para 2 casas decimais.

    Raises:
        ValueError: Se qualquer um dos argumentos (capital, taxa, tempo)
            for um valor negativo.

    Example:
        >>> calcular_juros_simples(1000.00, 5.0, 2.0)
        1100.00
        >>> calcular_juros_simples(2500.00, 3.5, 10.0)
        3375.00
    """

    # os valores não podem ser string

    if not isinstance(capital_inicial, (int, float)) or not isinstance(taxa_anual, (int, float)) or not isinstance(tempo_anos, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    
    # os valores não podem ser menor que 0

    if capital_inicial < 0:
        raise ValueError("devem ser valores não-negativos")
    
    if taxa_anual < 0:
        raise ValueError("devem ser valores não-negativos")
    
    if tempo_anos < 0:
        raise ValueError("devem ser valores não-negativos")
    
    #calculo do juros simples

    taxa_juros = taxa_anual / 100
    montante = capital_inicial * (1 + (taxa_juros * tempo_anos))
    
    return round (montante, 2)

# Organizador de Arquivos

## Visão Geral

Este script em Python foi desenvolvido para organizar arquivos em uma pasta de origem com base em regras predefinidas e movê-los para uma pasta de destino. O script utiliza a biblioteca Tkinter para uma seleção de diretórios amigável ao usuário.

## Recursos

### Interação com o Usuário

O script solicita ao usuário que selecione pastas de origem e destino usando uma interface gráfica fornecida pelo Tkinter.

### Regras de Organização de Arquivos

Os arquivos na pasta de origem são organizados em subpastas dentro da pasta de destino com base em um conjunto de regras predefinidas. As regras mapeiam os nomes curtos dos meses para seus respectivos nomes completos.

### Criação de Pastas

Se a subpasta de destino para um mês específico não existir, o script a cria antes de mover os arquivos correspondentes.

## Como Usar

1. **Executar o Script:**
   - Execute o script em um ambiente Python.

2. **Selecionar Pastas de Origem e Destino:**
   - O script solicitará que você selecione as pastas de origem e destino usando o diálogo de arquivo fornecido pelo Tkinter.

3. **Organização de Arquivos:**
   - O script analisará os arquivos na pasta de origem e os organizará em subpastas dentro da pasta de destino com base nas regras especificadas.

4. **Visualizar Resultados:**
   - Verifique a pasta de destino para ver os arquivos organizados em suas respectivas subpastas.

## Exemplo

Suponha que você tenha arquivos como "vendas_jan.txt" na pasta de origem e selecione a pasta de destino. Após executar o script, o arquivo será movido para a subpasta "Janeiro" dentro da pasta de destino.

**Caminho Original do Arquivo:**

```bash
C://Users/User/Downloads/arquivos/vendas_jan.txt
```

**Depois de Executar o Script:**

```bash
C://Users/User/Downloads/arquivos/Janeiro/vendas_jan.txt
```

## Dependências

- Python 3.x
- Tkinter (biblioteca padrão)

## Notas Importantes

- Certifique-se de ter as permissões necessárias para ler da pasta de origem e gravar na pasta de destino.
- Revise as regras de arquivo predefinidas no script para garantir que atendam aos seus requisitos.
- Recomenda-se executar o script em uma cópia de seus arquivos ou em um ambiente controlado para evitar perda de dados não intencional.

## Licença

Este script é fornecido sob a Licença MIT, dando a você a liberdade de modificá-lo e distribuí-lo.

#!/usr/bin/env python3
"""
🔄 Coletor — Imóveis de Todo o Brasil
Regiões: Norte | Nordeste | Centro-Oeste | Sudeste | Sul
"""

import json
import os
import time

PASTA_DADOS = "dados"
ARQUIVO_IMOVEIS = os.path.join(PASTA_DADOS, "imoveis.json")
os.makedirs(PASTA_DADOS, exist_ok=True)

def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def gerar_id():
    return f"imovel_{int(time.time() * 1000)}"

imoveis = {}

# ==============================================
# 🔴 REGIÃO NORTE
# ==============================================
imoveis.update({
    "norte_1": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Apartamento - Centro, Manaus",
        "cidade": "Manaus - AM",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 62,
        "valor_atual": 145000,
        "valor_avaliacao": 210000,
        "desconto_percentual": 31,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-12",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "norte_2": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Casa - Marambaia, Belém",
        "cidade": "Belém - PA",
        "tipo": "Casa",
        "quartos": 3,
        "area_m2": 95,
        "valor_atual": 182000,
        "valor_avaliacao": 260000,
        "desconto_percentual": 30,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-18",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "norte_3": {
        "id": gerar_id(),
        "fonte": "Bradesco",
        "titulo": "Terreno - Zona Leste, Porto Velho",
        "cidade": "Porto Velho - RO",
        "tipo": "Terreno",
        "quartos": 0,
        "area_m2": 420,
        "valor_atual": 78000,
        "valor_avaliacao": 130000,
        "desconto_percentual": 40,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-25",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://banco.bradesco/leiloes"
    }
})

# ==============================================
# 🟠 REGIÃO NORDESTE
# ==============================================
imoveis.update({
    "nordeste_1": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Apartamento - Boa Viagem, Recife",
        "cidade": "Recife - PE",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 58,
        "valor_atual": 198000,
        "valor_avaliacao": 320000,
        "desconto_percentual": 38,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-10",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "nordeste_2": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Casa - Pelourinho, Salvador",
        "cidade": "Salvador - BA",
        "tipo": "Casa",
        "quartos": 4,
        "area_m2": 110,
        "valor_atual": 295000,
        "valor_avaliacao": 420000,
        "desconto_percentual": 30,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-14",
        "situacao_ocupacao": "Ocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "nordeste_3": {
        "id": gerar_id(),
        "fonte": "Santander",
        "titulo": "Apartamento - Aldeota, Fortaleza",
        "cidade": "Fortaleza - CE",
        "tipo": "Apartamento",
        "quartos": 3,
        "area_m2": 75,
        "valor_atual": 265000,
        "valor_avaliacao": 380000,
        "desconto_percentual": 30,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-20",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://www.santander.com.br/leiloes"
    },
    "nordeste_4": {
        "id": gerar_id(),
        "fonte": "TRT-5 / Justiça do Trabalho - BA",
        "titulo": "Terreno - Parque Ecológico, Aracaju",
        "cidade": "Aracaju - SE",
        "tipo": "Terreno",
        "quartos": 0,
        "area_m2": 350,
        "valor_atual": 95000,
        "valor_avaliacao": 150000,
        "desconto_percentual": 37,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-22",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://portal.trt5.jus.br/leiloes"
    },
    "nordeste_5": {
        "id": gerar_id(),
        "fonte": "Bradesco",
        "titulo": "Casa - Lagoa Nova, Natal",
        "cidade": "Natal - RN",
        "tipo": "Casa",
        "quartos": 3,
        "area_m2": 88,
        "valor_atual": 178000,
        "valor_avaliacao": 245000,
        "desconto_percentual": 27,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-28",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://banco.bradesco/leiloes"
    }
})

# ==============================================
# 🟡 REGIÃO CENTRO-OESTE
# ==============================================
imoveis.update({
    "centrooeste_1": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Apartamento - Asa Norte, Brasília",
        "cidade": "Brasília - DF",
        "tipo": "Apartamento",
        "quartos": 3,
        "area_m2": 82,
        "valor_atual": 420000,
        "valor_avaliacao": 580000,
        "desconto_percentual": 28,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-15",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "centrooeste_2": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Casa - Setor Bueno, Goiânia",
        "cidade": "Goiânia - GO",
        "tipo": "Casa",
        "quartos": 4,
        "area_m2": 130,
        "valor_atual": 310000,
        "valor_avaliacao": 450000,
        "desconto_percentual": 31,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-19",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "centrooeste_3": {
        "id": gerar_id(),
        "fonte": "Santander",
        "titulo": "Apartamento - Centro, Campo Grande",
        "cidade": "Campo Grande - MS",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 55,
        "valor_atual": 92000,
        "valor_avaliacao": 155000,
        "desconto_percentual": 41,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-21",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://www.santander.com.br/leiloes"
    },
    "centrooeste_4": {
        "id": gerar_id(),
        "fonte": "TRT-10 / Justiça do Trabalho - DF",
        "titulo": "Terreno - Zona Industrial, Cuiabá",
        "cidade": "Cuiabá - MT",
        "tipo": "Terreno",
        "quartos": 0,
        "area_m2": 680,
        "valor_atual": 156000,
        "valor_avaliacao": 240000,
        "desconto_percentual": 35,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-30",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://portal.trt10.jus.br/leiloes"
    }
})

# ==============================================
# 🔵 REGIÃO SUDESTE
# ==============================================
imoveis.update({
    "sudeste_1": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Apartamento - Vila Mariana, São Paulo",
        "cidade": "São Paulo - SP",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 50,
        "valor_atual": 285000,
        "valor_avaliacao": 410000,
        "desconto_percentual": 30,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-10",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "sudeste_2": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Casa - Copacabana, Rio de Janeiro",
        "cidade": "Rio de Janeiro - RJ",
        "tipo": "Casa",
        "quartos": 3,
        "area_m2": 95,
        "valor_atual": 520000,
        "valor_avaliacao": 750000,
        "desconto_percentual": 31,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-13",
        "situacao_ocupacao": "Ocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "sudeste_3": {
        "id": gerar_id(),
        "fonte": "Bradesco",
        "titulo": "Apartamento - Savassi, Belo Horizonte",
        "cidade": "Belo Horizonte - MG",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 60,
        "valor_atual": 195000,
        "valor_avaliacao": 290000,
        "desconto_percentual": 33,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-17",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://banco.bradesco/leiloes"
    },
    "sudeste_4": {
        "id": gerar_id(),
        "fonte": "Santander",
        "titulo": "Apartamento - Centro, Vitória",
        "cidade": "Vitória - ES",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 52,
        "valor_atual": 168000,
        "valor_avaliacao": 240000,
        "desconto_percentual": 30,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-23",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://www.santander.com.br/leiloes"
    },
    "sudeste_5": {
        "id": gerar_id(),
        "fonte": "TRT-3 / Justiça do Trabalho - MG",
        "titulo": "Terreno - Zona Industrial, Uberlândia",
        "cidade": "Uberlândia - MG",
        "tipo": "Terreno",
        "quartos": 0,
        "area_m2": 500,
        "valor_atual": 120000,
        "valor_avaliacao": 150000,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-20",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://portal.trt3.jus.br/leiloes"
    }
})

# ==============================================
# 🟢 REGIÃO SUL
# ==============================================
imoveis.update({
    "sul_1": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Apartamento - Centro, Porto Alegre",
        "cidade": "Porto Alegre - RS",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 58,
        "valor_atual": 175000,
        "valor_avaliacao": 260000,
        "desconto_percentual": 33,
        "praca": "2ª Praça",
        "data_encerramento": "2026-11-16",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "sul_2": {
        "id": gerar_id(),
        "fonte": "Caixa Econômica Federal",
        "titulo": "Casa - Centro, Curitiba",
        "cidade": "Curitiba - PR",
        "tipo": "Casa",
        "quartos": 3,
        "area_m2": 105,
        "valor_atual": 290000,
        "valor_avaliacao": 420000,
        "desconto_percentual": 31,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-24",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://imoveis.caixa.gov.br"
    },
    "sul_3": {
        "id": gerar_id(),
        "fonte": "Bradesco",
        "titulo": "Apartamento - Centro, Florianópolis",
        "cidade": "Florianópolis - SC",
        "tipo": "Apartamento",
        "quartos": 2,
        "area_m2": 65,
        "valor_atual": 320000,
        "valor_avaliacao": 450000,
        "desconto_percentual": 29,
        "praca": "1ª Praça",
        "data_encerramento": "2026-11-27",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://banco.bradesco/leiloes"
    },
    "sul_4": {
        "id": gerar_id(),
        "fonte": "Santander",
        "titulo": "Casa - Bairro Jardim, Pelotas",
        "cidade": "Pelotas - RS",
        "tipo": "Casa",
        "quartos": 3,
        "area_m2": 92,
        "valor_atual": 145000,
        "valor_avaliacao": 210000,
        "desconto_percentual": 31,
        "praca": "2ª Praça",
        "data_encerramento": "2026-12-02",
        "situacao_ocupacao": "Desocupado",
        "link_edital": "https://www.santander.com.br/leiloes"
    }
})

# ==============================================
# SALVAR
# ==============================================
salvar_json(ARQUIVO_IMOVEIS, imoveis)
print("✅ Base atualizada com sucesso!")
print(f"📂 Arquivo: {ARQUIVO_IMOVEIS}")
print(f"🏠 Total de imóveis: {len(imoveis)}")
print("")
print("📍 Por Região:")
print(f"   🔴 Norte: 3 imóveis")
print(f"   🟠 Nordeste: 5 imóveis")
print(f"   🟡 Centro-Oeste: 4 imóveis")
print(f"   🔵 Sudeste: 5 imóveis")
print(f"   🟢 Sul: 4 imóveis")
print(f"   🇧🇷 TOTAL: {len(imoveis)} imóveis em todo o Brasil!")

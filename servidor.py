#!/usr/bin/env python3
"""
🏠 Leilões Fáceis — Servidor Completo e Corrigido
Porta: 8080
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import hashlib
import uuid
from urllib.parse import parse_qs, urlparse

PORTA = 8080
PASTA_DADOS = "dados"
ARQUIVOS = {
    "usuarios": "usuarios.json",
    "favoritos": "favoritos.json",
    "alertas": "alertas.json",
    "imoveis": os.path.join(PASTA_DADOS, "imoveis.json")
}

os.makedirs(PASTA_DADOS, exist_ok=True)
sessoes = {}

def carregar_json(caminho, padrao=None):
    if not os.path.exists(caminho):
        return padrao or {}
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def hash_senha(senha):
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

class ServidorLeiloes(BaseHTTPRequestHandler):
    def log_message(self, formato, *args):
        pass

    def enviar_arquivo(self, caminho, tipo="text/html; charset=utf-8"):
        try:
            if os.path.isfile(caminho):
                with open(caminho, "rb") as f:
                    self.send_response(200)
                    self.send_header("Content-Type", tipo)
                    self.end_headers()
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"<h1>404 - P&aacute;gina n&atilde;o encontrada</h1>")
        except:
            pass

    def definir_cookie(self, chave, valor, caminho="/"):
        try:
            self.send_header("Set-Cookie", f"{chave}={valor}; Path={caminho}; HttpOnly")
        except:
            pass

    def usuario_logado(self):
        cookie = self.headers.get("Cookie", "")
        for parte in cookie.split(";"):
            if "sessao=" in parte:
                id_sessao = parte.split("=")[-1].strip()
                return sessoes.get(id_sessao)
        return None

    def resposta_json(self, dados):
        try:
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(dados, ensure_ascii=False).encode("utf-8"))
        except:
            pass

    def redirecionar(self, destino):
        self.send_response(302)
        self.send_header("Location", destino)
        self.end_headers()

    def do_GET(self):
        caminho = urlparse(self.path).path
        usuario = self.usuario_logado()

        # === ROTAS DA API — PRIMEIRO, SEMPRE! ===
        if caminho == "/api/lista-imoveis":
            dados = carregar_json(ARQUIVOS["imoveis"], {})
            self.resposta_json([v for v in dados.values()])
            return

        if caminho == "/api/dados-usuario":
            if not usuario:
                self.send_response(401)
                self.end_headers()
                return
            fav = carregar_json(ARQUIVOS["favoritos"], {}).get(usuario["email"], [])
            alrt = carregar_json(ARQUIVOS["alertas"], {}).get(usuario["email"], [])
            self.resposta_json({"nome": usuario["nome"], "email": usuario["email"], "favoritos": fav, "alertas": alrt})
            return

        # === PÁGINAS ===
        paginas_publicas = {
            "/": "index.html",
            "/index.html": "index.html",
            "/login.html": "login.html",
            "/cadastro.html": "cadastro.html",
            "/aprenda.html": "aprenda.html",
            "/imoveis.html": "imoveis.html",
            "/calculadora.html": "calculadora.html",
            "/estilo.css": ("estilo.css", "text/css")
        }

        if caminho in paginas_publicas:
            arq = paginas_publicas[caminho]
            if isinstance(arq, tuple):
                self.enviar_arquivo(arq[0], arq[1])
            else:
                self.enviar_arquivo(arq)
            return

        if caminho == "/area_usuario.html":
            self.enviar_arquivo("area_usuario.html" if usuario else "login.html")
            return

        if caminho == "/sair":
            cookie = self.headers.get("Cookie", "")
            for p in cookie.split(";"):
                if "sessao=" in p:
                    sessoes.pop(p.split("=")[-1].strip(), None)
            self.redirecionar("/index.html")
            self.definir_cookie("sessao", "")
            return

        # Arquivo genérico
        self.enviar_arquivo(caminho.lstrip("/"))

    def do_POST(self):
        caminho = urlparse(self.path).path
        tamanho = int(self.headers.get("Content-Length", 0))
        corpo = self.rfile.read(tamanho).decode("utf-8")
        dados = parse_qs(corpo)
        usuario = self.usuario_logado()
        usuarios = carregar_json(ARQUIVOS["usuarios"], {})

        if caminho == "/cadastro":
            nome = dados.get("nome", [""])[0].strip()
            email = dados.get("email", [""])[0].strip().lower()
            senha = dados.get("senha", [""])[0]
            if not nome or not email or not senha:
                return self.redirecionar("/cadastro.html?msg=vazios")
            if email in usuarios:
                return self.redirecionar("/cadastro.html?msg=existe")
            usuarios[email] = {"nome": nome, "senha_hash": hash_senha(senha)}
            salvar_json(ARQUIVOS["usuarios"], usuarios)
            return self.redirecionar("/login.html?msg=sucesso")

        if caminho == "/login":
            email = dados.get("email", [""])[0].strip().lower()
            senha = dados.get("senha", [""])[0]
            u = usuarios.get(email)
            if u and u["senha_hash"] == hash_senha(senha):
                id_sessao = str(uuid.uuid4())
                sessoes[id_sessao] = {"email": email, "nome": u["nome"]}
                self.send_response(302)
                self.send_header("Location", "/area_usuario.html")
                self.definir_cookie("sessao", id_sessao)
                self.end_headers()
            else:
                self.redirecionar("/login.html?msg=erro")
            return

        if caminho == "/favoritar":
            if not usuario:
                return self.redirecionar("/login.html")
            favs = carregar_json(ARQUIVOS["favoritos"], {})
            favs.setdefault(usuario["email"], [])
            imovel_id = dados.get("imovel_id", [""])[0]
            if imovel_id in favs[usuario["email"]]:
                favs[usuario["email"]].remove(imovel_id)
            else:
                favs[usuario["email"]].append(imovel_id)
            salvar_json(ARQUIVOS["favoritos"], favs)
            self.redirecionar("/imoveis.html")
            return

        if caminho == "/criar-alerta":
            if not usuario:
                return self.redirecionar("/login.html")
            alertas = carregar_json(ARQUIVOS["alertas"], {})
            alertas.setdefault(usuario["email"], [])
            alertas[usuario["email"]].append({
                "id": str(uuid.uuid4())[:8],
                "imovel": dados.get("imovel_nome", [""])[0].strip(),
                "valor_alvo": dados.get("valor_alvo", [""])[0].strip(),
                "data_criacao": "Hoje"
            })
            salvar_json(ARQUIVOS["alertas"], alertas)
            self.redirecionar("/area_usuario.html?alerta=criado")
            return

        if caminho == "/remover-alerta":
            if not usuario:
                return self.redirecionar("/login.html")
            alertas = carregar_json(ARQUIVOS["alertas"], {})
            if usuario["email"] in alertas:
                alertas[usuario["email"]] = [a for a in alertas[usuario["email"]] if a["id"] != dados.get("alerta_id", [""])[0].strip()]
                salvar_json(ARQUIVOS["alertas"], alertas)
            self.redirecionar("/area_usuario.html?alerta=removido")
            return

if __name__ == "__main__":
    print("=" * 50)
    print("🏠 SERVIDOR RODANDO — Leilões Fáceis")
    print(f"👉 Porta: {PORTA} | Acesse: http://localhost:{PORTA}")
    print(f"🔗 API: http://localhost:{PORTA}/api/lista-imoveis")
    print("=" * 50)
    servidor = HTTPServer(("0.0.0.0", PORTA), ServidorLeiloes)
    servidor.serve_forever()

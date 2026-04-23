import pygame, sys, random

pygame.init()

LARGURA = 800
ALTURA = 600

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Sobrevivência")

CLOCK = pygame.time.Clock()

fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_normal = pygame.font.SysFont("Arial", 28)


# ==========================================
# Classe base
# ==========================================

class EntidadeBase:

    def __init__(self, x, y, largura, altura, cor):

        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def desenhar(self, tela):

        pygame.draw.rect(tela, self.cor, self.rect)

    def colidiu_com(self, outra):

        return self.rect.colliderect(outra.rect)


# ==========================================
# Jogador
# ==========================================

class Jogador(EntidadeBase):

    def __init__(self, x, y):

        super().__init__(x, y, 50, 50, (50,150,255))
        self.velocidade = 5

    def mover(self, teclas):

        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidade

        if teclas[pygame.K_RIGHT] and self.rect.x < LARGURA - 50:
            self.rect.x += self.velocidade

        if teclas[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocidade

        if teclas[pygame.K_DOWN] and self.rect.y < ALTURA - 50:
            self.rect.y += self.velocidade


# ==========================================
# Projétil
# ==========================================

class Projetil(EntidadeBase):

    def __init__(self, x, y):

        super().__init__(x, y, 10, 10, (255,255,0))
        self.velocidade = 8

    def mover(self):

        self.rect.y -= self.velocidade


# ==========================================
# Inimigo base
# ==========================================

class Inimigo(EntidadeBase):

    def __init__(self, x, y, velocidade=3):

        super().__init__(x, y, 40, 40, (255,120,0))
        self.velocidade = velocidade
        self.vida = 3

    def perseguir(self, alvo):

        if self.rect.x < alvo.rect.x:
            self.rect.x += self.velocidade

        if self.rect.x > alvo.rect.x:
            self.rect.x -= self.velocidade

        if self.rect.y < alvo.rect.y:
            self.rect.y += self.velocidade

        if self.rect.y > alvo.rect.y:
            self.rect.y -= self.velocidade


# ==========================================
# Inimigo rápido
# ==========================================

class InimigoRapido(Inimigo):

    def __init__(self, x, y):

        super().__init__(x, y, velocidade=6)
        self.cor = (255,0,255)


# ==========================================
# Inimigo gigante
# ==========================================

class InimigoGigante(Inimigo):

    def __init__(self, x, y):

        super().__init__(x, y, velocidade=2)

        self.rect.width = 80
        self.rect.height = 80

        self.cor = (120,0,255)

        self.vida = 5


# ==========================================
# HUD
# ==========================================

def desenhar_hud(tela, estado):

    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255,255,255))
    texto_vidas = fonte_normal.render(f"Vidas: {estado['vidas']}", True, (255,255,255))
    texto_nivel = fonte_normal.render(f"Nível: {estado['nivel']}", True, (255,255,255))

    tela.blit(texto_pont, (10,10))
    tela.blit(texto_vidas, (10,40))
    tela.blit(texto_nivel, (10,70))


def desenhar_game_over(tela):

    overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
    overlay.fill((0,0,0,160))

    tela.blit(overlay,(0,0))

    texto = fonte_grande.render("GAME OVER", True, (255,60,60))
    tela.blit(texto, texto.get_rect(center=(400,300)))


# ==========================================
# Sistema de níveis
# ==========================================

niveis = {

    1: {"velocidade":2, "quantidade":4},
    2: {"velocidade":3, "quantidade":6},
    3: {"velocidade":4, "quantidade":8}

}


# ==========================================
# Inicialização
# ==========================================

jogador = Jogador(375,275)

inimigos = []
projeteis = []

for _ in range(3):
    inimigos.append(Inimigo(random.randint(0,750),random.randint(0,100)))

for _ in range(2):
    inimigos.append(InimigoRapido(random.randint(0,750),random.randint(0,100)))

for _ in range(1):
    inimigos.append(InimigoGigante(random.randint(0,750),random.randint(0,100)))


estado = {

    "pontuacao":0,
    "vidas":5,
    "nivel":1,
    "rodando":True

}

mostrar_msg_nivel = 0


# ==========================================
# Loop principal
# ==========================================

while estado["rodando"]:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.KEYDOWN:

            if ev.key == pygame.K_SPACE:

                projeteis.append(
                    Projetil(
                        jogador.rect.centerx,
                        jogador.rect.y
                    )
                )

    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)


    # mover projeteis
    for p in projeteis[:]:

        p.mover()

        if p.rect.y < 0:
            projeteis.remove(p)


    # mover inimigos
    for ini in inimigos:

        ini.perseguir(jogador)

        if jogador.colidiu_com(ini):

            estado["vidas"] -= 1

            ini.rect.topleft = (random.randint(0,750),0)

            if estado["vidas"] <= 0:

                estado["rodando"] = False


    # colisão projétil x inimigo
    for p in projeteis[:]:

        for ini in inimigos[:]:

            if p.colidiu_com(ini):

                ini.vida -= 1

                if p in projeteis:
                    projeteis.remove(p)

                if ini.vida <= 0:

                    inimigos.remove(ini)
                    estado["pontuacao"] += 100

                break


    # pontuação por sobrevivência
    estado["pontuacao"] += 1


    # sistema de nível
    novo_nivel = estado["pontuacao"] // 500 + 1

    if novo_nivel > estado["nivel"] and novo_nivel in niveis:

        estado["nivel"] = novo_nivel
        mostrar_msg_nivel = 120


    # aplicar dificuldade
    config = niveis.get(estado["nivel"], niveis[3])

    while len(inimigos) < config["quantidade"]:

        tipo = random.choice(["normal","rapido","gigante"])

        if tipo == "normal":
            inimigos.append(Inimigo(random.randint(0,750),0,config["velocidade"]))

        elif tipo == "rapido":
            inimigos.append(InimigoRapido(random.randint(0,750),0))

        else:
            inimigos.append(InimigoGigante(random.randint(0,750),0))


    # ==========================================
    # Renderização
    # ==========================================

    TELA.fill((20,20,40))

    jogador.desenhar(TELA)

    for ini in inimigos:
        ini.desenhar(TELA)

    for p in projeteis:
        p.desenhar(TELA)

    desenhar_hud(TELA, estado)


    # mensagem de nível
    if mostrar_msg_nivel > 0:

        texto = fonte_grande.render(f"Nível {estado['nivel']}", True, (255,255,0))
        TELA.blit(texto, texto.get_rect(center=(400,200)))

        mostrar_msg_nivel -= 1


    pygame.display.flip()
    CLOCK.tick(60)


# ==========================================
# Game Over
# ==========================================

desenhar_game_over(TELA)

pygame.display.flip()

pygame.time.wait(3000)

pygame.quit()
sys.exit()
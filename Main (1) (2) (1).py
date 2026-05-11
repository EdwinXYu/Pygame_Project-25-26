from gamelib import *

def positionObjects(objects, lane):
    y = -100
    for i in range(len(objects)):
        # Space notes apart vertically
        y -= randint(80, 140)
        objects[i].moveTo(lane, y)

def spawnbullet(enemy, target):
    bullet = Image("sprites/Bullet_E.png",game)
    bullet.moveTo(enemy.x, enemy.y)
    bullet.resizeBy(-70)
    # Aim toward player
    angle = bullet.angleTo(target)
    bullet.setSpeed(6, angle)
    enemyBullets.append(bullet)


# Game settings and stuff
game = Game(781, 604, "DeltaRythem")
GSSBG = Image("sprites/Fountain.jpg", game)
# GSSBG = Game Starter Screen Backround\
GBG = Image("sprites/Game_BG.png", game)
# Game Backround

#Sprites

Chart = Image("sprites/Note_Chart.png",game)
Chart.moveTo(390,170)
Chart.resizeBy(-40)

Bar1=Image("sprites/Bar_1.png",game,use_alpha=False)
Bar1.moveTo(430,293)
Bar1.resizeBy(-70)

Bar2=Image("sprites/Bar_2.png",game,use_alpha=False)
Bar2.moveTo(358,291)
Bar2.resizeBy(-70)

BNotes = []
for i in range(110):
    BN = Animation("sprites/B_Note.png",8,game,934/8,230,6)
    BNotes.append(BN)
    BNotes[i].width *= 0.8
    BNotes[i].height *= 0.8
positionObjects(BNotes,358)

    
RNotes=[]
for i in range (110):
    RN = Animation("sprites/R_Note.png",8,game,934/8,230,6)
    RNotes.append(RN)
    RNotes[i].width *=0.8
    RNotes[i].height *=0.8
positionObjects(RNotes,430)
   
#Kris
KrisI=Image("sprites/Kris_Idle.png",game, use_alpha=False)
KrisI.moveTo(100,300)
KrisI.resizeBy(60)

KrisNH = Animation("sprites/Kris_NoteHit.png",4,game,150/4,42,4)
KrisNH.moveTo(100,300)
KrisNH.resizeBy(300)

#Susie
SusieI=Image("sprites/Susie_Idle.png",game, use_alpha=False)
SusieI.moveTo(200,400)
SusieI.resizeBy(50)

SusieNH = Animation("sprites/Susie_NoteHit.png",6,game,431/6,61,3)
SusieNH.moveTo(200,400)
SusieNH.resizeBy(200)

attackProj = Image("sprites/Attack.png", game)
attackProj.visible = False
attackProj.moveTo(SusieI.x, SusieI.y)
 
#Ralsie
RalsieI=Image("sprites/Ralsie_Idle.png",game)
RalsieI.moveTo(100,500)
RalsieI.resizeBy(100)
RalsieI.rotateTo(180)

RalsieNH=Animation("sprites/Ralsie_NoteHit.png",4,game,270/4,90,6)
RalsieNH.moveTo(100,500)
RalsieNH.resizeBy(110)
RalsieNH.rotateTo(180)

#Enemy
Enemy1=Animation("sprites/Enemy_1.png",8,game,724/8,96,8)
Enemy1.moveTo(600,400)
Enemy1.resizeBy(20)

Enemy2=Animation("sprites/Enemy_1.png",8,game,724/8,96,8)
Enemy2.moveTo(700,500)
Enemy2.resizeBy(20)

# -------------------------------
# COMBINED ENEMY HEALTH BAR ENEMIES
# -------------------------------

# Total health for both enemies together
enemyHealth = 200
maxEnemyHealth = 200

# Health bar settings
healthBarX = 500
healthBarY = 40
healthBarWidth = 220
healthBarHeight = 25

# -------------------------------
# PARTY HEALTH BAR
# -------------------------------

partyHealth = 300
maxPartyHealth = 300

partyHealthBarX = 20
partyHealthBarY = 60
partyHealthBarWidth = 220
partyHealthBarHeight = 25

# -----------------
# STAMINA SYSTEM
# -----------------

stamina = 0
maxStamina = 100

# -----------------
# NOTE HIT COUNTER
# -----------------
noteHits = 0
bullet = Image("sprites/Bullet_E.png",game)
enemyBullets = []


# -----------------
# ATTACK SYSTEM
# -----------------

attackCost = 25
attackDamage = 25
attackCooldown = 0

#Title Part
Title = Image("sprites/Title.png", game)

Play = Image("sprites/play_On.png",game)
Play.y = 500
PlayO = Image("sprites/Play_On.png", game)
PlayF = Image("sprites/Play_Off.png", game)

story = Image("sprites/Story_Off.png", game)
story.y = 300
storyF = Image ("sprites/story_Off.png",game)
storyO = Image ("sprites/Story_On.png",game)
StoryText = Image("sprites/Story_Text.png",game)
StoryText.visible = False

controls = Image("sprites/Controls_Off.png",game)
controls.y = 400
controlsF = Image("sprites/Controls_Off.png",game)
controlsO = Image ("sprites/Controls_On.png",game)
ControlText = Image("sprites/Controls_Text.png",game)
ControlText.visible = False

End_Screen=Image("sprites/EndingScreen.png",game)
End_Screen.moveTo(390, 302)
End_Screen.resizeBy(30)

Death_Screen=Image("sprites/Death_Screen.png",game)
Death_Screen.moveTo(390,302)

Heart1 = Image("sprites/Mouse.png", game)
Heart1.resizeBy(-92)
mouse.visible = False

#Music
New_Death=Sound("music/New_Death.wav",0)
Menu_Theme=Sound("music/Menu_Theme.wav",1)
RYB = Sound("music/Raise_Your_Bat.wav",2)
Ruder_Buster= Sound("music/Ruder_Buster.wav",3)
Black_Knife=Sound("music/Black_Knife.wav",4)
Flame=Sound("music/Flame.wav",5)
#Sounds
Death_SFX=Sound("music/Death_SFX.wav",6)
Rude_Buster=Sound("music/Rude_Buster_attack.wav",7)



game.setMusic("music/Menu_Theme.wav")
game.playMusic()
# Game starting screen
game.setBackground(GSSBG)
while not game.over:
    game.processInput()
    GSSBG.draw()
    Heart1.moveTo(mouse.x, mouse.y)
    Heart1.draw()
    Title.draw()
    Title.moveTo(400, 150)
    story.draw()
    controls.draw()
    Play.draw()

    StoryText.draw()
    ControlText.draw()

# Display

    if Heart1.collidedWith(Play, "rectangle"):
        Play.setImage(PlayO.image)
    else:
        Play.setImage(PlayF.image)

    if Heart1.collidedWith(story,"rectangle"):
        story.setImage(storyO.image)
    else:
        story.setImage(storyF.image)

    if Heart1.collidedWith(controls,"rectangle"):
        controls.setImage(controlsO.image)
    else:
        controls.setImage(controlsF.image)


    if Heart1.collidedWith(story,"rectangle") and mouse.LeftClick:
        StoryText.visible = True

    if Heart1.collidedWith(controls,"rectangle") and mouse.LeftClick:
        ControlText.visible = True

    if Heart1.collidedWith(Play, "rectangle") and mouse.LeftClick:
        game.over = True
        game.stopMusic()

    if keys.Pressed[K_SPACE]:
        StoryText.visible = False
        ControlText.visible = False
       
   
    game.update(60)


# Game - Level 1
game.over = False

game.setMusic("music/New_Death.wav")
game.playMusic()
while not game.over:
    targetX = (Enemy1.x + Enemy2.x) / 2
    RalsieI.flipH = RalsieI.x < targetX
    RalsieNH.flipH = RalsieNH.x < targetX
    
    game.processInput()
    GBG.draw()

    Chart.draw()
    Bar1.draw()
    Bar2.draw()
    KrisI.draw()
    KrisNH.draw(False)
    SusieI.draw()
    SusieNH.draw(False)
    RalsieI.draw()
    RalsieNH.draw(False)
    Enemy1.draw()
    Enemy2.draw()

# -----------------
# DRAW STAMINA BAR
# -----------------

# Background
    pygame.draw.rect(game.screen, dark_gray, (20, 20, 200, 25))
# Current stamina
    currentStaminaWidth = (stamina / maxStamina) * 200
    pygame.draw.rect(game.screen, yellow,
                 (20, 20, currentStaminaWidth, 25))
# Border
    pygame.draw.rect(game.screen, white,
                 (20, 20, 200, 25), 3)
# Text
    game.drawText("TP", 60, 22)
    # Draw health bar background
    pygame.draw.rect(game.screen, red,
                     (healthBarX, healthBarY,
                      healthBarWidth, healthBarHeight))


# -----------------
# PARTY HEALTH BAR
# -----------------

# Background
    pygame.draw.rect(game.screen,red,
        (partyHealthBarX,
         partyHealthBarY,
         partyHealthBarWidth,
         partyHealthBarHeight))

# Current HP
    currentPartyWidth = (partyHealth / maxPartyHealth) * partyHealthBarWidth

    pygame.draw.rect(game.screen,green,
        (partyHealthBarX,
         partyHealthBarY,
         currentPartyWidth,
         partyHealthBarHeight))

# Border
    pygame.draw.rect(game.screen,white,
                     (partyHealthBarX,
                      partyHealthBarY,
                      partyHealthBarWidth,
                      partyHealthBarHeight),3)
# Text
    game.drawText("Party HP",70,62)


#-------
#Health
#-------

# Current health amount
    currentBarWidth = (enemyHealth / maxEnemyHealth) * healthBarWidth

# Draw remaining health
    pygame.draw.rect(game.screen,green,(healthBarX,
                                        healthBarY,
                                        currentBarWidth,
                                        healthBarHeight))

# Optional border
    pygame.draw.rect(game.screen,white,(healthBarX,
                                        healthBarY,
                                        healthBarWidth,
                                        healthBarHeight),3)



    for i in range(len(BNotes)):
        if BNotes[i].visible:
            BNotes[i].draw()
            BNotes[i].y += 4
        if Bar2.collidedWith(BNotes[i], "rectangle"):
            if keys.Pressed[K_a]:
                BNotes[i].visible = False
                stamina +=5
                enemyHealth +=3.5
                noteHits += 1
                partyHealth +=4
       
    for i in range(len(RNotes)):
        if RNotes[i].visible:
            RNotes[i].draw()
            RNotes[i].y += 4
            if Bar1.collidedWith(RNotes[i], "rectangle"):
                if keys.Pressed[K_d]:
                    RNotes[i].visible = False
                    stamina += 5
                    enemyHealth +=3.5
                    noteHits += 1
                    partyHealth +=4
                    
    if keys.Pressed[K_a] or keys.Pressed [K_d]:
        KrisNH.visible = True        
        KrisI.visible = False
    else:
        KrisNH.visible=False
        KrisI.visible=True


    if keys.Pressed[K_a] or keys.Pressed [K_d]:
        SusieNH.visible = True        
        SusieI.visible = False
    else:
        SusieNH.visible=False
        SusieI.visible=True

    if keys.Pressed[K_a] or keys.Pressed [K_d]:
        RalsieNH.visible = True        
        RalsieI.visible = False
    else:
        RalsieNH.visible=False
        RalsieI.visible=True

# -----------------
# ENEMY ATTACK
# -----------------

    if noteHits >= 10:
        spawnbullet(Enemy1, KrisI)
        spawnbullet(Enemy2, KrisI)
        noteHits = 0

    for bullet in enemyBullets:
        bullet.move()
        bullet.draw()
        # Remove offscreen bullets
    if bullet.isOffScreen():
        bullet.visible = False
        # Hit player
    if bullet.collidedWith(KrisI, "rectangle"):
        bullet.visible = False
        partyHealth -= 20
        print("Player Hit!")

        enemyBullets = [b for b in enemyBullets if b.visible]
    if bullet.collidedWith(KrisNH,"rectangle"):
        bullet.visible=False
        partyHealth -= 20
        print("Player Hit!")
        
        enemyBullets = [b for b in enemyBullets if b.visible]

#------
#ATTACK
#------
    if stamina > maxStamina:
        stamina = maxStamina
# -----------------
# ATTACK COOLDOWN
# -----------------
    if attackCooldown > 0:
        attackCooldown -= 1
# -----------------
# RUDE BUSTER ATTACK
# -----------------

    if keys.Down == K_SPACE and attackCooldown == 0:
    # Check stamina
        if stamina >= attackCost:
        # Use stamina
            stamina -= attackCost
        # Damage combined enemy HP
            enemyHealth -= attackDamage
        # Play attack sound
            Rude_Buster.play(True)
        # Cooldown
            attackCooldown = 30
        # Image
            attackProj.draw()
            attackProj.moveTo(Enemy1.x,Enemy1.y)
        if attackProj.collidedWith(Enemy1):
            attackProj.visible=False

    if enemyHealth < 1:
        enemyHealth = 0
        game.over=True

    if partyHealth <= 1:
        partyHealth = 0
        playerDead = True
        game.over = True

    
    game.update(80)

# -----------------
# END SCREEN
# -----------------

# -----------------
# END / DEATH SCREEN
# -----------------

game.over = False
game.stopMusic()

while not game.over:
    game.processInput()
    if playerDead:
        Death_Screen.draw()
    else:
        End_Screen.draw()
    if keys.Pressed[K_ESCAPE]:
        game.over = True

    game.update(60)

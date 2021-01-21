import os
import pygame
#기본 초기화 (반드시 해야 하는 것들)################################
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pang game")

# FPS
clock = pygame.time.Clock()
####################################################################


# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표 , 폰트 등)###################
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 이벤트 루프
running = True  # 게임 진행 상태
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 설정

    # 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생항였는지 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 확인
            running = False  # 게임 종료

    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # 게임화면 다시그리기 (필수)

# 게임 종료후 잠시 대기

pygame.quit()

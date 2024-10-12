import pygame.image
from PIL import Image, ImageSequence


class Explosion:
    gif: Image

    def __init__(self, position: tuple = (0, 0)):
        self.gif = Image.open("assets/Explosão/explosao.gif")
        self.frames = []
        self.frame_durations = []
        for frame in ImageSequence.Iterator(self.gif):
            frame = frame.convert("RGBA")
            frame_image = pygame.image.fromstring(frame.tobytes(), frame.size, "RGBA")
            self.frames.append(frame_image)
            self.frame_durations.append(self.gif.info.get('duration', 100))
        self.position = position
        self.current_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.active = True

    def update(self):
        now = pygame.time.get_ticks()
        if self.active:
            if now - self.last_update_time > self.frame_durations[self.current_frame]:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.last_update_time = now
                if self.current_frame >= len(self.frames)-1:
                    self.active = False

    def draw(self, surface):
        if self.active:
            surface.blit(self.frames[self.current_frame], self.position)

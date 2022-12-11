# Intro Tutorial
Follow the practice lesson below with the code in this repo. Try to do as much on your own as you can.

# Pre-Steps
Download this repo with the following command.
```bash
git clone https://github.com/theisen1337/PygameTutorials.git
```

open the `PygameTutorials\Lesson_1\Problem` folder in Pycharm.
The game should be able to run at the beginning of the problem set. 
Make sure it runs and you see a green sqaure in Pygame Window.
You won't be able to move or anything.

# Step 1 - Add movement to Player
Look at the `Player` class object, there is no movement setup. To get the player to respond to the input to move. Some design decisions need to be taken. Like how will be control, move, speed, and math for the movement.
The method below follows 2d vector movement with acceleration and velocity. A little bit more advanced process, but allows for smooth movement of the player and objects.

Add the Math parameters to the Player initializer.
```python
def __int__(self):

    # ...

    # Add parameters for movement.
    self.pos = vector((10, 385))
    self.vel = vector(0, 0)
    self.acc = vector(0, 0)

```

Add the move Function to the Player Class, to do the movement logic.
```python
    def move(self):
        # reset acceleration
        self.acc = vector(0, 0)

        # retrieve all keys pressed.
        pressed_keys = pygame.key.get_pressed()

        # Update Acceleration
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC  # Change acceleration in the left direction
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC   # Change acceleration in the right direction

        # Do the Vector math to apply acceleration and Friction to the velocity
        self.acc.x += self.vel.x * FRIC         # Multiple friction with velocity add it to acceleration
        self.vel += self.acc                    # Add Acceleration to velocity
        self.pos += self.vel + 0.5 * self.acc   # Add velocity, constant times acceleration to position

        # Translate the position value calculated above to the player object accords.
        self.rect.midbottom = self.pos
```

Now if you run the program you are still unable to move. That is becuase the code is not being called in the main loop of the game. Add `P1.move()` to the main loop of the game and now you should be able to move. Call the move function pirior to drawing the player sprite or you will notice some jittering.
```python
    # Call player move calculations during the game loop.
    P1.move()
```
Now test it out, you should be able to move left and right. You can even move off the screen.


# Step 2 - Add bounds to the player.
Since you can move. You will have to add bounds so the player object does not fall off the screen.

In the `move` function add bound controls to limit the player from going off the screen, by wraping around to the other side of the sreen.
```python
# Player Bounds to the window, wrapping the player to the opposite side when they try to go off.
if self.pos.x > WIDTH:
    self.pos.x = 0
if self.pos.x < 0:
    self.pos.x = WIDTH
```

Now when you play the game notice how you teleport to the other side of the window when you try to move off.

# Step 3 - Cardinal directions 
Now is a good time to look at [documentation](https://www.pygame.org/docs/ref/key.html) to help you out. Documentation can sometimes really help.
Get Familiar with the keys you already are using and others. Update movement to use `AWSD` which feels more comfortable for PC players.
```python
    # Try to update movement yourself before looking at the answer.
```

---------------------
<details><summary>Answer</summary>
<p>

#### Cardinal directions movement, using `AWSD`

```python
    # Update Acceleration on key press
    if pressed_keys[K_a]:
        self.acc.x = -ACC  # Change acceleration in the left direction
    if pressed_keys[K_d]:
        self.acc.x = ACC   # Change acceleration in the right direction
    if pressed_keys[K_w]:
        self.acc.y = -ACC  # Change acceleration in the Up direction
    if pressed_keys[K_s]:
        self.acc.y = ACC   # Change acceleration in the Down direction
```

</p>
</details>
---------------------

Now if you run the game you should notice that you can move left,right,up, and down.
You will also notice that when moving up, and down you glide across the screen, alot like astroids.
You will have to update Vector math to handle 2d and not just 1d.

Update the math logic, try yourself first.
```python
    # Do the Vector math to apply acceleration and Friction to the velocity
    self.acc.x += self.vel.x * FRIC         # Multiple friction with velocity add it to acceleration
    self.vel += self.acc                    # Add Acceleration to velocity
    self.pos += self.vel + 0.5 * self.acc   # Add velocity, constant times acceleration to position
```

---------------------
<details><summary>Answer</summary>
<p>

#### Cardinal direction Friction

```python
    # Do the Vector math to apply acceleration and Friction to the velocity
    self.acc.x += self.vel.x * FRIC         # Multiple friction with velocity add it to acceleration
    self.acc.y += self.vel.y * FRIC         # Multiple friction with velocity add it to acceleration
    self.vel += self.acc                    # Add Acceleration to velocity
    self.pos += self.vel + 0.5 * self.acc   # Add velocity, constant times acceleration to position
```

</p>
</details>
---------------------

Now if you run the program you will be able to move correctly in all directions. But there is no wrapping on the top and bottem.
Add the bounds yourself.

```python
    # Player Bounds to the window, wrapping the player to the opposite side when they try to go off.
    if self.pos.x > WIDTH:
        self.pos.x = 0
    if self.pos.x < 0:
        self.pos.x = WIDTH
    # Attempt your updates here.
```

You should be able to add the bounds, yourself then test them. You might notice that the sprite cut off for the player is different for `Left-Right` and `Up-Down` this is because the window toolbar takes up some of the canvas this is caused by the Windows Gui API that gives that overlays the toolbar.
To fix this issue of cutting the sprite weirdly just move the bounds inward on both directions by half the size of the sprite (`15px`).

---------------------
<details><summary>Answer</summary>
<p>

#### Cardinal direction Bounds

```python
    # Player Bounds to the window, wrapping the player to the opposite side when they try to go off.
    if self.pos.x > WIDTH:
        self.pos.x = 0
    if self.pos.x < 0:
        self.pos.x = WIDTH

    if self.pos.y > HEIGHT + 15:
        self.pos.y = 15
    if self.pos.y < 15:
        self.pos.y = HEIGHT + 15
```

</p>
</details>
---------------------

# Step 4 - Add a new game object

Now that player movement is flushed out, lets give the player something to do. Lets add a `coin` object. Initialize it the same way as the player, but skip the movement vector parameters.

---------------------
<details><summary>Answer</summary>
<p>

#### Coin Game Object.

```python
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.surf = pygame.Surface((8, 8))  # patch 30px x 30px of the display.
        self.surf.fill((228, 255, 40))  # color patch
        self.rect = self.surf.get_rect(center=(50, 420))  # get positioning and rectangle parameters
```

</p>
</details>
---------------------

If you play the game you will not see any new sprites.
Create the coin sprite by declaring it, then add it to `all_sprites`. You should be able to run the game and see it.

---------------------
<details><summary>Answer</summary>
<p>

#### Coin Game Object creation.

```python
    # Create Sprites
    C1 = Coin()
    P1 = Player()


    all_spirtes = pygame.sprite.Group()
    all_spirtes.add(P1)
    all_spirtes.add(C1)
```

</p>
</details>
---------------------

You will notice a gold sqaure about 1/5 smaller then the player sprite. If you run over it, nothing will happen. If you added the coin to the sprite group before the player the coin will disappear under the player sprite, and vis versa if you added the coin after the player in the sprite group.

Before we move on from this step, lets add some point value to the coin object.

```python
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.surf = pygame.Surface((8, 8))  # patch 30px x 30px of the display.
        self.surf.fill((228, 255, 40))  # color patch
        self.rect = self.surf.get_rect(center=(50, 420))  # get positioning and rectangle parameters

        self.points = 1

    def give_points(self):
        return self.points
```

# Step 5 - UI
User interface is used to let the player know different game states, values, progress. Health, quest log, ammo are ui details you find in many different games. Some games are cleaver and have non-invasive user interfaces such as red boarder around screen when player is hurt.
Lets add some text to our game overlay. to let the player know how many coins they have collected.

This is a pretty good time to try researching something you don't know. 
Sometimes the documentation fails at showing you how to put multiple pieces together. 
This is a great time to use a search engine to learn by example.

Here are some websites that I used to create code for this section.
* https://www.geeksforgeeks.org/pygame-working-with-text/ (You might hit a login wall if not using an Ad-blocker)
* https://pygame.readthedocs.io/en/latest/4_text/text.html
* https://stackoverflow.com/a/52972742

What I settled on. Placed before all the game sprite classes we created.
```python
font1 = pygame.font.SysFont('chalkduster.ttf', 16)
text1 = font1.render('coins: ', True, (50, 205, 50))
textRect1 = text1.get_rect()
textRect1.center = (100, 10)
```

Draw the font to the screen after drawing all the sprites to the screen, so it is the most top drawn thing.
```python
    # Draw font to screen.
    display.blit(text1, textRect1)
```

Play the game and checkout the text at the top. Feel free to change the position, size, color, font of the text. As it stands its the same color as the player.


*Note* The `SysFont` is a built in font that exist somewhere either in your Os, Python, or Pygame. 
But it exist and if you are using pygame you should be able to use this font. 
Making tutorials like this easy to implement. 
If you want to use a custom font which you should do if your going to ever sell your game. 
It is easy enough to place a custom font in your project folders and call it directly instead of using `SysFont`.

# Step 6 - Collision!
Now lets programmically add what happens when the player runs into a coin.

Add a new sprite group called `coins`, and add coin to it. A sprite can belong to one or many sprite groups at once.

---------------------
<details><summary>Answer</summary>
<p>

#### New sprite group.

```python
# Create Sprites
C1 = Coin()
P1 = Player()

all_spirtes = pygame.sprite.Group()
all_spirtes.add(P1)
all_spirtes.add(C1)

coins = pygame.sprite.Group()
coins.add(C1)
```

</p>
</details>
---------------------

lets add a function to check for collision on the player object.
```python
    def update(self):
        # Check the sprite group "coins" for collisions
        hits = pygame.sprite.spritecollide(P1, coins, False)
        if hits:
            print("hit!")
```

Add the call to the function under player move call.

After you add it and run the game, you notice when you run over the coin the console prints "hit!"

So at this point to get continue on and attempt to debug the code to see what is getting set. 
You should put a break point on `hits = pygame.sprite.spritecollide(P1, coins, False)` and check out what `hits` is set too.

Before we add code to the update method under player, we need to add a couple functions to the coin class.


```python
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        
        #...

        self.points = 1

    def give_points(self):
        return self.points

```

Add the following functions to Player Class, and add `self.score` to the constructor method.
```python
    def get_score(self):
        return self.score

    def add_points(self, points_add):
        self.score += points_add
```

lets go back to the `update` method under player class, now we can grab the `coin` object within `hits` list.
You can grab the points of the coin, then add the coins on the player, then return the current player score.
```python
def update(self):
    hits = pygame.sprite.spritecollide(P1, coins, False)
    if hits:
        # Get points
        points = hits[0].give_points()
        # Update score
        self.add_points(points)
    return self.get_score()
```

Then we need to update the game loop to draw the points from the player.
```python
    P1.move()
    points_to_display = P1.update()

    # Clearing the screen and setting to black.
    display.fill((0, 0, 0))

    # sprites draw
    for entity in all_spirtes:
        display.blit(entity.surf, entity.rect)  # drawing

    text1 = font1.render('coins: ' + str(points_to_display), True, (50, 205, 50))
    display.blit(text1, textRect1)
```

Now when you should be able to play the game. When you walk over the coin, your coin score should shoot up!
We will fix that in the next step.

# Step 7 - move coin location.

Add a call to randomly place the coin after being hit.

start here
```python
    def update(self):
    hits = pygame.sprite.spritecollide(P1, coins, False)
    if hits:
        # Get points
        points = hits[0].give_points()
        # Update score
        self.add_points(points)


        """
            Call a function under the coin object to change positions.
        """

        # Update random position of coin
        hits[0].update_position()


    return self.get_score()
```

Give it a try, check out the answer when your done.

---------------------
<details><summary>Answer</summary>
<p>

#### New random location.

Add import
```Python
from random import *
```

Add the function to the coin.
```Python
    def update_position(self):
        self.rect.x = randint(10, WIDTH - 10)
        self.rect.y = randint(10, HEIGHT - 10)
```

Now make sure the call is in the "if hit" condition under player object.

</p>
</details>
---------------------

You are now done, check it out. Play around see what you can add.
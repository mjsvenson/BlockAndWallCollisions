# Block and Wall Collisions

A Python/pygame physics sim of two blocks colliding with each other and a wall, with a cool surprise: the digits of pi show up.

![Block and Wall Collisions simulation](BlockAndWallCollisions.jpg)

## What it does

This program simulates two blocks on a frictionless surface next to a wall with infinite mass and zero velocity. You enter the mass and velocity for each block, and the sim plays out every elastic collision while counting them.

The cool part: when the first block starts at rest with a mass of 1 kg and the second block has a mass of 100^n kg (1, 100, 10000, ...), the total collision count gives you the digits of pi. 3, 31, 314, 3141, and so on.

## How to run it

You need Python 3 and pygame.

```bash
pip install -r requirements.txt
python main.py
```

Enter the mass and velocity for each block when asked, then watch the collisions and the counter play out.

## How it works

- Elastic collision physics between the two blocks and the wall
- Real time collision counter
- Adjustable masses and velocities, so you can try any setup you want, not just the pi digit cases

## Known limitations

At large scales (masses over ~10,000) the sim gets inconsistent and the counts are usually wrong. I tried tweaking collision tolerance but it did not fix it. Since the sim is GUI driven, some argument combos are impossible to run. Fixing the numerical stability at scale would be the natural next step.

## License

Public domain under the Unlicense. See [LICENSE](LICENSE).

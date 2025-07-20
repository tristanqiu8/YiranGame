# Mathematical Curves Demo

This project contains two programs that demonstrate mathematical curves using animated turtle graphics.

## Programs

### 1. heart_curve.py - Heart Curve Animation
A dedicated program for drawing a beautiful heart shape using parametric equations.

**Features:**
- Animated turtle drawing the heart curve
- Gradient trail effect
- Interactive controls for size and speed
- Shows mathematical equations

**Heart Curve Equations:**
```
x(t) = 16 * sin³(t)
y(t) = 13*cos(t) - 5*cos(2t) - 2*cos(3t) - cos(4t)
where t ∈ [0, 2π]
```

### 2. math_curves.py - Multiple Curves Explorer
An interactive program to explore various mathematical curves.

**Available Curves:**

1. **Heart Curve** - The romantic heart shape
2. **Rose Curve (4 petals)** - A beautiful flower pattern
   - Equation: r = cos(4θ)
3. **Lissajous Curve** - Complex harmonic motion pattern
   - Equations: x = sin(3t), y = sin(2t)
4. **Archimedean Spiral** - A classic spiral pattern
   - Equation: r = t
5. **Infinity/Lemniscate** - Figure-eight pattern
   - Equations: x = cos(t), y = sin(2t)/2

## How to Run

```bash
# For heart curve only
python heart_curve.py

# For multiple curves
python math_curves.py
```

## Controls

- **SPACE** - Pause/Resume animation
- **R** - Reset the current curve
- **1-5** - Select different curves (in math_curves.py)
- **UP/DOWN** - Adjust curve size (in heart_curve.py)
- **E** - Toggle equation display (in heart_curve.py)

## Mathematical Background

### Parametric Equations
These curves use parametric equations where both x and y coordinates are functions of a parameter t:
- x = f(t)
- y = g(t)

This allows for complex curves that would be difficult to express as y = f(x).

### Why These Curves?

1. **Heart Curve** - Perfect for romantic applications, cards, or Valentine's Day projects
2. **Rose Curves** - Beautiful symmetric patterns, great for decorative designs
3. **Lissajous Curves** - Used in physics to visualize harmonic motion
4. **Spirals** - Found throughout nature (shells, galaxies)
5. **Infinity Curves** - Symbol of infinity, used in mathematics and physics

## Customization Ideas

1. **Add New Curves:**
   - Butterfly curve
   - Cardioid
   - Astroid
   - Cycloid

2. **Visual Enhancements:**
   - Rainbow gradient trails
   - Particle effects at turtle position
   - Multiple turtles drawing simultaneously

3. **Interactive Features:**
   - Real-time parameter adjustment
   - Save curves as images
   - Combine multiple curves

## Educational Uses

These programs are excellent for:
- Teaching parametric equations
- Visualizing mathematical concepts
- Introduction to computer graphics
- Programming with Pygame

Enjoy exploring the beauty of mathematics through code!
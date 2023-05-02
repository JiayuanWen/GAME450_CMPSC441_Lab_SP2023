# CMPSC 441 and GAME 450 Lab Repository: Oillill's Advanture

## Abstract
Oillill's Advanture is a advanture game about a young elf's journeys and encounters during his travel between cities. The game utilized multiple Artificial Intelligence techniques to generate a more detailed world to the game, as well as to provide a more engaging experience to the player. 

Oillill's Advanture follows the journey of a young elf named Oillill. He makes money as they travels across the world and build their life once he reached his destination. He crossed many cities and treacherous roads to reach their destination, and encountered many enemies along the way. 

In this game, you play as the elf Oillill. At the beginning, you are randomly placed in one of the ten cities of the world, and is assigned a destination city you must reach to finish the game. Cities are connected to each other by a route. Depending on the geography, a route may cost more or less Rubys to travel, routes on mountains and waterways are more expensive than routes on flatlands. You must traverse carefully to reach your destination before running out of Rubys. Along some routes, enemies may emerge to challenge you in a battle, you must defeat them to continue your journey, and to earn more Rubys to traverse further. 

The game is programmed in Python, utilizes many different AI techniques and libraries for its world generation and for enhancing experience during gameplay. It uses a combination of random generation and conditional reflex to generate a landscape, place cities, and assign travel costs to routes base on routes' overlapping landscape. The enemies of the game uses reflex-based AI to provide more challenges to the player, as well as giving them more characters. The game also uses speech synthesis to give player a better understanding of their current situation.

## AI components
* Perlin Noise (Procedural Content Generation)
* GA City Placement (Goal-base AI)
* TTS (Speech synthesis)

## Solution to Problems
### Perlin Noise
Perlin noise is a type of procedural noise used in computer graphics to create natural-looking textures and terrain. It was invented by Ken Perlin in the 1980s and has since become a widely used technique in the field of computer graphics and game development.

To generate a landscape map using Perlin noise, the following steps are typically taken:
1. Generate a grid of random gradient vectors: These gradient vectors should be uniformly distributed across the grid and should have random directions.

2. Divide the landscape into smaller tiles: These tiles should be of equal size and cover the entire landscape.

3. For each tile, calculate a noise value at each of its corner points: To do this, take the dot product of the gradient vector at each corner with the vector from the corner to the point being evaluated.

4. Interpolate between these corner noise values: Use a smoothing function such as cubic interpolation to generate a smooth noise value across the tile.

5. Repeat steps 3-4 for each tile in the landscape: This will generate a noise map that can be used as a height map for the landscape.

6. Apply threshold values to the noise map: Set different threshold values to create different terrain features. For example, areas with high noise values can be used to create mountains, while areas with low noise values can be used to create valleys.

7. Smooth the terrain: Use a smoothing algorithm to remove sharp edges and create a more natural-looking landscape.

By following these steps, it is possible to generate a realistic and visually appealing landscape map using Perlin noise. 

Hand crafting a landscape can be a time-consuming and labor-intensive task. To ease such task, the game uses Perlin noise to procedurally generate a landscape for its world map. An additional benefit of using procedurally generated landscape is that the landscapes generated are always different, which means we can make the gameplay experience different every time by letting the game generate a different landscape on start. 

### Goal-base AI
Goal-based AI is a type of artificial intelligence that is designed to achieve a specific objective or task. This type of AI operates on the basis of predefined goals, which are programmed by humans. Goal-based AI can be used in a wide range of applications, including robotics, gaming, and decision-making systems.

The goal-based AI system consists of three main components: a set of goals, a set of actions, and a set of rules. The goals define what the AI system aims to achieve, while the actions represent the different ways in which the system can act to achieve those goals. The rules determine how the system selects which actions to take to achieve the goals.

To achieve its goals, the goal-based AI system needs to be able to reason and plan. This involves the use of algorithms and logical reasoning to determine the best course of action to achieve a given goal. The system needs to be able to evaluate the potential outcomes of different actions and select the one that is most likely to lead to the desired result.

One of the key advantages of goal-based AI is that it can be very efficient. By focusing on a specific goal, the system can avoid getting distracted by irrelevant information or tasks. This makes it particularly useful for tasks that require a high degree of precision or that involve complex decision-making.

However, goal-based AI also has some limitations. It can struggle with tasks that involve a lot of uncertainty or that require the system to adapt to changing circumstances. In addition, because the goals are predefined by humans, the system may not be able to handle tasks that were not anticipated by its programmers.

To place the ten cities of the world realistic (i.e. No cities placed underwater or too high above the mountains), we wrote pre-defined rules to a goal-based AI algorithm to place the cities for us.

### Text-to-Speech Speech Synthesis
TTS (Text-to-Speech) speech synthesis is a technology that converts written text into spoken audio output. This process involves using a computer program that analyzes the text, generates a phonetic transcription, and then produces the audio output in a way that mimics human speech.

There are several different approaches to TTS speech synthesis, but they all generally involve breaking down the text into smaller components, such as individual words or phonemes, and then using various algorithms and techniques to produce the final audio output. Some TTS systems use pre-recorded audio samples of human speech, while others use synthesized speech generated by algorithms.

One of the key challenges in TTS speech synthesis is producing natural-sounding speech that is free from robotic-sounding artifacts. To achieve this, TTS systems may use techniques such as prosody modeling, which involves analyzing the intonation and rhythm of natural speech and then applying those patterns to synthesized speech.

Not everyone want to pause and read long paragraphs to understand what is going on in the game, having scenarios speak out to players allows for a more fluent gameplay experience. For this case, we use TTS speech synthesis system to read the game scenarios out loud to the players, specifically Google's GTTS (Google Text-to-Speech) which is commonly used in Google Translate. A unintended benefit of using TTS is that blink people can now also enjoy the game.

## Appendix
### Appendix 1: ChatGPT transcript on Perlin Noise:
```
How perlin noise is used to generate landscape map?
```

```
Perlin noise is a type of procedural noise used in computer graphics to create natural-looking textures and terrain. It was invented by Ken Perlin in the 1980s and has since become a widely used technique in the field of computer graphics and game development.

To generate a landscape map using Perlin noise, the following steps are typically taken:

Generate a grid of random gradient vectors: These gradient vectors should be uniformly distributed across the grid and should have random directions.

Divide the landscape into smaller tiles: These tiles should be of equal size and cover the entire landscape.

For each tile, calculate a noise value at each of its corner points: To do this, take the dot product of the gradient vector at each corner with the vector from the corner to the point being evaluated.

Interpolate between these corner noise values: Use a smoothing function such as cubic interpolation to generate a smooth noise value across the tile.

Repeat steps 3-4 for each tile in the landscape: This will generate a noise map that can be used as a height map for the landscape.

Apply threshold values to the noise map: Set different threshold values to create different terrain features. For example, areas with high noise values can be used to create mountains, while areas with low noise values can be used to create valleys.

Smooth the terrain: Use a smoothing algorithm to remove sharp edges and create a more natural-looking landscape.

By following these steps, it is possible to generate a realistic and visually appealing landscape map using Perlin noise. The resulting map can then be used as a basis for creating 3D models of the terrain or for generating other types of visualizations.
```

### Appendix 2: ChatGPT transcript on Goal-based AI:
```
Describe goal-based AI.
```

```
Goal-based AI is a type of artificial intelligence that is designed to achieve a specific objective or task. This type of AI operates on the basis of predefined goals, which are programmed by humans. Goal-based AI can be used in a wide range of applications, including robotics, gaming, and decision-making systems.

The goal-based AI system consists of three main components: a set of goals, a set of actions, and a set of rules. The goals define what the AI system aims to achieve, while the actions represent the different ways in which the system can act to achieve those goals. The rules determine how the system selects which actions to take to achieve the goals.

To achieve its goals, the goal-based AI system needs to be able to reason and plan. This involves the use of algorithms and logical reasoning to determine the best course of action to achieve a given goal. The system needs to be able to evaluate the potential outcomes of different actions and select the one that is most likely to lead to the desired result.

One of the key advantages of goal-based AI is that it can be very efficient. By focusing on a specific goal, the system can avoid getting distracted by irrelevant information or tasks. This makes it particularly useful for tasks that require a high degree of precision or that involve complex decision-making.

However, goal-based AI also has some limitations. It can struggle with tasks that involve a lot of uncertainty or that require the system to adapt to changing circumstances. In addition, because the goals are predefined by humans, the system may not be able to handle tasks that were not anticipated by its programmers.

Overall, goal-based AI is a powerful tool for achieving specific objectives and can be used in a wide range of applications. Its effectiveness depends on the clarity and specificity of the goals that are programmed into the system, as well as the ability of the system to reason and plan effectively.
```

### Appendix 2: ChatGPT transcript on TTS:
```
Describe TTS speech synthesis.
```

```
TTS (Text-to-Speech) speech synthesis is a technology that converts written text into spoken audio output. This process involves using a computer program that analyzes the text, generates a phonetic transcription, and then produces the audio output in a way that mimics human speech.

There are several different approaches to TTS speech synthesis, but they all generally involve breaking down the text into smaller components, such as individual words or phonemes, and then using various algorithms and techniques to produce the final audio output. Some TTS systems use pre-recorded audio samples of human speech, while others use synthesized speech generated by algorithms.

One of the key challenges in TTS speech synthesis is producing natural-sounding speech that is free from robotic-sounding artifacts. To achieve this, TTS systems may use techniques such as prosody modeling, which involves analyzing the intonation and rhythm of natural speech and then applying those patterns to synthesized speech.

TTS speech synthesis is used in a variety of applications, such as in assistive technologies for people with visual impairments, in automated customer service systems, and in voice assistants such as Siri and Alexa.
```
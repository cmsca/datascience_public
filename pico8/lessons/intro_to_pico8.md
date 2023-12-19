# Intro to Pico-8

## Desired outcomes from this session

The purpose of this lesson is to ensure each participant is comfortable enough with Pico-8 to enjoy and learn from the course. 

## This lesson will cover:

- [ ] **What is Pico-8?**

- [ ] **Using Pico-8**

	- When you first start Pico-8, you are in a mode where you can type commands. Use the ESC key to toggle back and forth between editor mode and command mode. 

- [ ] **The Code Editor**

	- All of your code is written here

	- Each game ('cart') has a token limit of 8192 tokens

	- Add comments using `--`

- [ ] **The Sprite Editor**

	- Sprites are the pieces of art that make up your game. They might be characters, map tiles, pickups, backgrounds... anything!

	- Pico-8 allows you to have 256 8x8 sprites. These are spread across 4 tabs labeled 0-3. The last two tabs share the same spaces as the map editor, however. 

- [ ] **The Map Editor**

	- Pico-8's map tiles use the 8x8 sprites from the sprite editor.

	- You can have a max map size of 128 tiles wide and 64 tiles tall. 

- [ ] **The Sound Editor**

	- A Pico-8 card can have up to 64 sounds. 

	- Each sound has 32 notes.

- [ ] **The Music Editor**

	- The music editor allows you to create patterns of music using sounds from the sound editor. 

- [ ] **Coordinates**

	- Pico-8's screen is 128 x 128.

	- The coordinate 0,0 is in the top left corner and 127, 127 is in the bottom right.

- [ ] **Programming Basics**

	- Variables
		
		Do not use sprite reserved keywords like `spr`

		**Types of variables:**

		Numbers: 
		`x = 100`

		Strings: 
		`phrase = 'Hello World'`
		
		Tables: 

		```lua
		grades = {}
		grades.chemistry = 95
		grades.math = 93
		grades.english = 99
		```

	- If Statements
		
		Example if statement:

		```lua
		if player.x > 200 then
			player.x = 0
		end
		```

		Example else-if statement:

		```lua
		if player.jumping then
			player.sp = 7
		elseif player.falling then 
			player.sp = 8
		elseif player.sliding then
			player.sp = 9
		else 
			player.sp = 1
		end
		```
		

	- Functions
	
	Components of functions:
	- [ ] function keyword
	- [ ] function name
	- [ ] parameters
	- [ ] end keyword


	Example:

	```lua
	function print_text(text)
	print(text)
	end
	```
	Calling the `print_text` function:

	`print_text('hello world')`


	Other examples of functions:
	
	`circfill(x,y,radius,color)`

- [ ] **The Game Loop**

	- Init - the code here happens one time when the game starts

	- Update - code here happens 30 times every second

	- Draw - code here also happens 30 times every second, but after update happens

## If we have time, we'll:

- [ ] Make sprites for the 'Fruit Drop' game

- [ ] Begin the 'Fruit Drop' tutorial


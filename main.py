# When coding, we typically call text that people might see when they run our code a string
#A string can contain letters, numbers and symbols

# We put quotes around text that our code should treat as a string. Otherwise it might look like a variable name 

# You can use regular quotes
print("Is it hot out?")

# Or single quotes
print('What is the temperature today?')

# Things can get confusing if your text has an apostrophe
#If you remove the # symbol below and try to run the code, you will get an error
#print('It's hot')

# Use a slash in front of the apostrophe to tell Python not to treat it like it would normally treat a single quote
print('It\'s hot')

# If you use regular quotes around your string, Python will know your apostrophe in the middle of the text is an apostrophe
print("It's REALLY hot!")

# But what if you want quote marks in your string? Use single quotes around the text
print('She said "It is hot!"')

# But what if you want quote marks AND an apostrophe in your text??
# Use triple quotes!
print('''He said "It's too hot!"''')

# Triple quotes are also used for multiline strings, meaning text that you hit enter in the middle of
joke = '''Knock Knock
Who's there?
Spell.
Spell who?
Ok. W H O.'''

print(joke)

# Sometimes you want to put a value in your text, but you don't know what the value will be when you write the code
# You can use %s as a placeholder for the value and then use a % sign before the value you want to replace in the text
temp_today = 85
print("Today's temperature is %s degrees." % temp_today)

# If you have more than one blank you need to fill in, put as many values as you need inside parentheses and seprate them by commas, after the % sign
joke = """%s rhymes with %s?
No it doesn't!"""

print(joke % ('What','orange'))

#Note you can use 3 double quotes as well as 3 single quotes to create a multi-line string

# You can also multiply strings by a number
print(2 * 'choo ')
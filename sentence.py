from time import sleep
import user_input 


def get_sentence():
    time = user_input.get_time()
    noun = user_input.get_noun()
    name= user_input.get_name()
    sentence = user_input.get_sentence()
    verb = user_input.get_verb()


    print("\n")
    print("The story goes...")
    print("\n")
    sleep(3)
    print(
        f'''It was {time} o'clock when I heard a knock at the door.\nI opened the door and there was a box full of {noun} with a note saying \"From Mr. {name}.\"\nJust as I closed the door I heard a scream \"{sentence}.\"\nI froze in place and all I could do was {verb}.''')
    print("\n")

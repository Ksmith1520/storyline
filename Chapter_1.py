import time
import webbrowser
import random

maze_images = [
    "https://i.imgur.com/cAAWORg.jpeg",
    "https://i.imgur.com/tFS4qg6.jpeg",
    "https://i.imgur.com/Q3eLaY4.jpeg",
    "https://i.imgur.com/zATugwJ.jpeg",
    "https://i.imgur.com/piocq7O.jpeg"
]

forest_images = [
    "https://i.imgur.com/RGIle7k.jpeg",
    "https://i.imgur.com/BcFwSrI.jpeg",
    "https://i.imgur.com/sf5sY2s.jpeg",
    "https://i.imgur.com/spnoaMZ.jpeg",
    "https://i.imgur.com/3WkWs21.jpeg"
]

monster_images = [
    "https://i.imgur.com/wADxYt2.jpeg",
    "https://i.imgur.com/MJrHyCw.jpeg",
    "https://i.imgur.com/aANKFcU.jpeg",
    "https://i.imgur.com/Dk1NDLs.jpeg",
    "https://i.imgur.com/mvdeDVz.jpeg"
]

def show_random_image(image_list):
    image_url = random.choice(image_list)
    print(f"Opening this image for you to see: {image_url}")
    webbrowser.open(image_url)

points = 0
def intro():
    print("Welcome to our interactive story where the choices you make WILL affect the outcome of your story.")
    print("During the story, you will have to make choices")
    print("Each choice will be worth a certain amount of points")
    print("Depending on how many points you earn, your story will end a particular way")
    print("There are three possible endings to this story and you can play it as many times as you want")
    print("We wish you the best of luck")
    input("Press Enter to continue...")
    

def background():
    print("You work as an EMT at your station and one of your coworkers is on vacation.")
    print("You decide to pick up their shift for them to help out")
    print("It is Halloween and the entire day at the station has been crazy and wild")
    print("During your first hour at work, you receive a call about children horseplaying around at a haunted house when two of them collide and hit their heads")
    print("You rush to the scene with your partner, Will, and when you step on scene you see one small child with a bump on his head")
    print("After asking the child about the situation, you learn that he collided heads with another one of his friends inside of the haunted maze")
    print("The child informs you that the other kid is still inside the maze somewhere")
    input("Press Enter to continue...")
    

def start():
    global points
    intro()
    print()
    background()
    print()

    print("You must decide your next step...")
    print("1. You decide to have your partner check out the boy while you go in and try to find the other boy")
    print("2. You let the boy go in and find the other kid and bring him to you")
    print("3. You and your partner both tend to the boy and wait to see if the other boy comes out")
    print("Choose a number")
    choice = input("> ")

    if choice == "1":
        print("Congratulations!!! This is the best choice! By leaving your partner with the other boy, you are making the best use of your time by truing to save the other kid")
        print("You earned 3 points")
        input("Press Enter to continue...")

        points += 3
    elif choice == "2":
        print("NOOO!!! This is the worst choice that you could make. Now you have lost both children and you must go into the maze now. You leave your partner outside just in case the boys come out.")
        print("You earned 1 point")
        input("Press Enter to continue...")

        points += 1
    elif choice == "3":
        print("This was not the best choice. The other boy never came out, but the first kid seems fine. Now the other boy has been left alone for several minutes with a head injury. Your partner stays outside while you rush into the maze.")
        print("You earned 2 points")
        input("Press Enter to continue...")

        points += 2
    else:
        print("Please choose 1, 2, or 3")
        return start(points)

   
    print()
    print(f"You have {points} point(s).")
    print()
    maze()
    print()
    print(f"You have {points} point(s).")
    print()
    forest()
    print()
    print(f"You have {points} point(s).")
    print()
    print("Congratulations. You have reached the end of chapter 1")

def maze():
    global points
    show_random_image(maze_images)
    print("You enter into the maze but it is super dark. Luckily, you have a flashlight in your bag.")
    print("You shine the flashlight around and follow through the maze, looking for any signs of a hurt child")
    print("You find drops of blood on the ground that you assume to be from the kid. You start to hurry through the maze knowing that every second might count")
    print("You follow the trail to the back of the maze when suddenly the footprints go through a small opening in the maze and into the forest")
    input("Press Enter to continue...")
    print()

    print("Make a choice")
    print("1. Go into the forest alone")
    print("2. Recruit people to help you search")
    print("3. Leave the scene")
    print("Choose a number")
    choice = input("> ")

    if choice == "1":
        print("You enter into the forest alone, not really knowing where to start. The forest is too big and it would have been nice to have some help...")
        print("You earned 2 points")
        points += 2
    elif choice == "2":
        print("Success! You ask several people to help you search the woods for the missing boy. You all spread out and search different areas.")
        print("You earned 3 points")
        points += 3
    elif choice == "3":
        print("LEAVE THE SCENE?!? NOO!! You completely abandon the boy and head back to your partner. He seems mad at you and forces you back into the forest. You separate in the forest to cover more ground.")
        print("You earned 1 point")
        points += 1
    else:
        print("Please choose 1, 2, or 3")
        return maze()

def forest():
    global points
    show_random_image(forest_images)
    print("You find yourself deep in the forest all alone.")
    print("You are surrounded by thick trees and you hear little noise")
    print("Suddenly, you hear the voice of a child calling out for help")
    print("You rush towards the sound, when you see a large shadow running in the distance")
    input("Press Enter to continue...")
    show_random_image(monster_images)
    print()

    print("Make a choice")
    print("1. Chase the shadow")
    print("2. Run from the shadow")
    print("3. Fight the shadow")
    print("Choose a number")
    choice = input("> ")

    if choice == "1":
        print("You decide to chase the big shadow to find out where he is going. He leads you towards a cave and you accidentally step on a stick, making noise. The shadow hears you and turns around and captures you.")
        print("You earned 1 point")
        points += 1
    elif choice == "2":
        print("You decide that the shadow is not what you are looking for and you decide to go a different way. You keep following the sound of the boy's voice and come to a clearing. Just as you see the boy, you are hit over the head.")
        print("You earned 2 points")
        points += 2
    elif choice == "3":
        print("You notice that the shadow is running towards the sound of the boy. You think he must have taken the boy and you decide to fight the shadow. You charge him, knocking into his back and " \
        "he howls out in pain. He turns around, knocking you unconscious with his arm.")
        print("You earned 3 points")
        points += 3
    else:
        print("Please choose 1, 2, or 3")
        return forest()





if __name__ == "__main__":
    start()
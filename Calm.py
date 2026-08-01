import time


def clear_line():
    print("\r" + " " * 80 + "\r", end="", flush=True)


def breathing():
    for _ in range(3):
        clear_line()
        print("\rBreathe in...", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r1", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r2", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r3", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r4", end="", flush=True)
        time.sleep(1)

        clear_line()
        print("\rHold...", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r1", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r2", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r3", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r4", end="", flush=True)
        time.sleep(1)

        clear_line()
        print("\rAnd out...", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r1", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r2", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r3", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r4", end="", flush=True)
        time.sleep(1)

        clear_line()
        print("\rHold...", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r1", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r2", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r3", end="", flush=True)
        time.sleep(1)
        clear_line()
        print("\r4", end="", flush=True)
        time.sleep(1)

    clear_line()
    print("Breathing session complete.")


def meditation():
    print()
    print("Think of a place where you feel happiest...")
    time.sleep(2)
    print("Now put yourself into that place, feel the air around you, hear the wind whispering, be there...")
    time.sleep(2)
    print("Get somewhere comfy, or if you are in a busy place block all of the noise and movement out...")
    time.sleep(2)
    input("Are you ready? Press Enter to continue.")
    print("Close your eyes, after that I will not guide you. Meditation is not something others do for you. Go ahead...")


def yoga():
    poses = [
        ("Mountain Pose", "Stand tall, feet together, arms by your sides, and breathe slowly."),
        ("Chair Pose", "Sit back as if lowering into a chair, knees bent, arms reaching forward."),
        ("Downward Dog", "Hands and feet on the floor, lift your hips high, and lengthen your spine."),
        ("Crescent Stretch", "Step forward, rise up through your chest, and reach your arms overhead."),
        ("Warrior II", "Step one foot back, bend the front knee, and open your arms wide."),
        ("Tree Pose", "Press one foot into your ankle and lift it to your calf, balancing with calm breath."),
        ("Child's Pose", "Sit back onto your heels and stretch your arms forward to soften and relax."),
    ]

    print("\nA gentle yoga flow will begin.")
    time.sleep(1)

    for name, instruction in poses:
        clear_line()
        print(f"{name}", end="", flush=True)
        time.sleep(1)
        clear_line()
        print(f"{name}: {instruction}", end="", flush=True)
        time.sleep(2)
        clear_line()
        print(f"Hold {name} for 3 breaths...", end="", flush=True)
        time.sleep(2)

    clear_line()
    print("Yoga flow complete. You should feel calmer now.")


def main():
    print("Welcome to Calm.py, where you will find your inner zen.")
    print()

    while True:
        choice = input("Do you want to do breathing, meditation, or yoga? ").strip().lower()
        if choice == "breathing":
            breathing()
            break
        elif choice == "meditation":
            meditation()
            break
        elif choice == "yoga":
            yoga()
            break
        else:
            print("Please choose breathing, meditation, or yoga.")


if __name__ == "__main__":
    main()